# 7. Risk register

> **Status: proposed.** Risks of the future-state design.

| # | Risk | Likelihood | Impact | Control | Owner |
|---|---|---|---|---|---|
| R1 | A safety request is not recognised and waits in a normal queue | Medium | High | Protected-hint list; safety option at the top of the form; daily human check of the REVIEW lane; pilot measure on safety first-touch time | Safety focal point |
| R2 | Personal or HR information is sent to an external AI service | Low | High | Protected lane before any AI call; data minimisation; approved provider only | Data-protection lead |
| R3 | Silent misroute in the AUTO lane | Medium (Policy A), low (Policy B) | Medium | Policy B; weekly spot-check sample; handler "not mine" button that returns to REVIEW | Coordinator lead |
| R4 | Coordinators accept AI suggestions without reading them (automation bias) | Medium | Medium | Measure accepted-but-wrong rate; occasional blind checks; suggestions show the rationale | Coordinator lead |
| R5 | Instruction-like text in a request changes AI behaviour | Low | Medium | Request text treated as data; pattern check sends to REVIEW; output schema allows no actions | Technical owner |
| R6 | AI service unavailable | Medium | Low | Fail closed to REVIEW; the process works without AI | Technical owner |
| R7 | Rules or hint lists drift as language changes | Medium | Medium | Monthly review of abstentions and corrections | Coordinator lead |
| R8 | The form adds friction and people return to email | Medium | Medium | Short form; email still accepted and triaged; feedback in pilot | Office manager |
| R9 | Benefits are claimed before they are measured | Medium | Medium | Only pilot measures are reported as results; scenarios stay labelled | Project sponsor |
