import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from app.analytics import analyze_performance, kpis
from app.ai import generate_ai_summary

st.set_page_config(page_title="AI API SLA Monitoring Assistant", page_icon="📊", layout="wide")
st.title("AI-Powered API SLA Monitoring & Business Incident Assistant")
st.caption("Business Analyst portfolio project — SLA monitoring, business impact analysis and AI-assisted reporting.")

base = Path(__file__).resolve().parents[1]
perf = pd.read_csv(base / "data/api_performance.csv")
sla = pd.read_csv(base / "data/api_sla_config.csv")

uploaded = st.file_uploader("Upload API performance CSV (optional)", type=["csv"])
if uploaded:
    perf = pd.read_csv(uploaded)

df = analyze_performance(perf, sla)
summary = kpis(df)

c1,c2,c3,c4 = st.columns(4)
c1.metric("APIs Monitored", summary["APIs Monitored"])
c2.metric("SLA Breaches", summary["SLA Breaches"])
c3.metric("Critical Breaches", summary["Critical Breaches"])
c4.metric("SLA Compliance", f'{summary["SLA Compliance"]}%')

st.subheader("API SLA Status")
display_cols = ["date","api_name","availability","response_time_ms","error_rate_pct","business_process","criticality","severity"]
st.dataframe(df[display_cols], use_container_width=True, hide_index=True)

st.subheader("Availability Trend")
fig = px.line(df, x="date", y="availability", color="api_name", markers=True,
              title="API Availability by Day")
st.plotly_chart(fig, use_container_width=True)

breaches = df[df["sla_breach"]].copy()
st.subheader("Business Incident Analysis")
if breaches.empty:
    st.success("No SLA breaches detected in the selected data.")
else:
    for _, row in breaches.iterrows():
        with st.expander(f'{row["severity"]} — {row["api_name"]} — {row["date"]}'):
            st.write(f'**Business process:** {row["business_process"]}')
            st.write(f'**Owner:** {row["owner_team"]}')
            st.write(f'**Availability:** {row["availability"]}% vs SLA {row["availability_sla"]}%')
            st.write(f'**Response time:** {row["response_time_ms"]} ms vs SLA {row["response_time_sla_ms"]} ms')
            st.write(f'**Error rate:** {row["error_rate_pct"]}% vs SLA {row["error_rate_sla_pct"]}%')

    if st.button("Generate AI Management Summary"):
        st.write(generate_ai_summary(breaches))

st.subheader("API Criticality Mapping")
st.dataframe(sla[["api_name","business_process","criticality","owner_team"]], use_container_width=True, hide_index=True)

st.download_button(
    "Download SLA Analysis CSV",
    df.to_csv(index=False).encode("utf-8"),
    "api_sla_analysis.csv",
    "text/csv"
)
