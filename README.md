# AI-Powered API SLA Monitoring & Business Incident Assistant

A Business Analyst portfolio project that automates API SLA monitoring, breach identification, business-impact mapping and stakeholder reporting.

## Business Problem
Business teams depend on APIs for critical journeys such as payments, customer onboarding and policy processing. Manually reviewing API performance makes it difficult to identify SLA breaches, understand business impact and prepare consistent incident reports.

## Solution
The application compares API performance data against defined SLAs, identifies breaches, maps them to business processes, classifies severity and uses an LLM to generate business-friendly incident summaries and management insights.

## Key capabilities
- Upload API performance CSV data
- Configure SLA thresholds
- Detect availability, response-time and error-rate breaches
- Map APIs to business processes and criticality
- Generate AI-assisted incident summaries
- Generate management-level SLA observations
- Track breach frequency and trends
- Export a business report

## BA deliverables
See `business-analysis/` for the BRD, requirements, As-Is/To-Be process, user stories, acceptance criteria, business rules, SLA matrix, escalation matrix and traceability.

## Run locally
1. Python 3.10+
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env`
4. Add an OpenAI API key if AI analysis is required.
5. Run: `streamlit run app/main.py`

The application works without an API key for rule-based SLA analysis; AI narrative generation is optional.

## Important
Sample metrics are synthetic portfolio data and must not be represented as production/company results.
