# Test Scenarios

| ID | Scenario | Expected Result |
|---|---|---|
| TC-001 | Availability below SLA | Availability breach |
| TC-002 | Response time above SLA | Response breach |
| TC-003 | Error rate above SLA | Error breach |
| TC-004 | No breach | Within SLA |
| TC-005 | Critical API with 2+ breaches | Critical severity |
| TC-006 | High API with breach | High severity |
| TC-007 | AI unavailable | Rule-based analysis still works |
| TC-008 | Missing API mapping | Missing mapping is visible |
