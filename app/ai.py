import os
from dotenv import load_dotenv

load_dotenv()

def generate_ai_summary(breach_rows, model=None):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "AI analysis is not configured. Rule-based SLA analysis is available. Add OPENAI_API_KEY to generate narrative insights."

    from openai import OpenAI
    client = OpenAI(api_key=api_key)
    model = model or os.getenv("OPENAI_MODEL", "gpt-5.6-mini")

    records = breach_rows.to_dict(orient="records")
    prompt = f"""Act as a business analyst reviewing API SLA breaches.
Use only the supplied data. Do not claim a root cause unless the data proves it.
Produce:
1. Executive summary
2. Key observations
3. Potential business impact
4. Recommended investigation areas
5. Stakeholder follow-up questions

Data:
{records}
"""
    response = client.responses.create(model=model, input=prompt)
    return response.output_text
