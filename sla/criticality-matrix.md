# API Criticality Matrix

| Criticality | Meaning |
|---|---|
| Critical | Failure can interrupt a core business transaction |
| High | Failure materially affects a customer/business workflow |
| Medium | Failure affects a supporting workflow |

Sample mapping:
- Payment API → Payment Processing → Critical
- Policy API → Policy Issuance → Critical
- Customer API → Customer Registration → High
- Notification API → Customer Communication → Medium
