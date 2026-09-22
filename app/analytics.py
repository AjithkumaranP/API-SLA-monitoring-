import pandas as pd

def analyze_performance(perf: pd.DataFrame, sla: pd.DataFrame) -> pd.DataFrame:
    merged = perf.merge(sla, on="api_name", how="left")
    merged["availability_breach"] = merged["availability"] < merged["availability_sla"]
    merged["response_breach"] = merged["response_time_ms"] > merged["response_time_sla_ms"]
    merged["error_breach"] = merged["error_rate_pct"] > merged["error_rate_sla_pct"]
    merged["sla_breach"] = merged[["availability_breach","response_breach","error_breach"]].any(axis=1)
    merged["breach_count"] = merged[["availability_breach","response_breach","error_breach"]].sum(axis=1)

    def severity(row):
        if not row["sla_breach"]:
            return "Within SLA"
        if row["criticality"] == "Critical" and row["breach_count"] >= 2:
            return "Critical"
        if row["criticality"] in ("Critical", "High"):
            return "High"
        return "Medium"

    merged["severity"] = merged.apply(severity, axis=1)
    return merged

def kpis(df: pd.DataFrame) -> dict:
    return {
        "APIs Monitored": int(df["api_name"].nunique()),
        "SLA Breaches": int(df["sla_breach"].sum()),
        "Critical Breaches": int((df["severity"] == "Critical").sum()),
        "SLA Compliance": round((~df["sla_breach"]).mean() * 100, 2),
    }
