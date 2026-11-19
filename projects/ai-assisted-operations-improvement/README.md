# AI-assisted operations improvement: request intake and triage

> **Proposal and simulation.** The organisation is fictional, the data is synthetic, and no AI model was called. Rules results are measured on synthetic data; AI benefits are scenarios that a pilot would have to confirm. This is an independent project. It has not been piloted or deployed in a real organisation. The code and documentation were developed with AI assistance under my direction (see [Provenance](../../README.md#provenance)).

A case study in redesigning an operations process before deciding whether AI belongs in it. A small programme support office receives internal requests by email and web form. Requests wait, get routed to the wrong person, arrive without the details needed to act, and urgent safety matters sit in the same queue as stationery orders.

## Why this problem

I chose a problem type I know from practice. As Office & Operations Manager with HR operations responsibilities at Libre Space Foundation (January 2024 – January 2026), I coordinated facilities, finance, HR and logistics requests, including invoices, payroll processes, vendors, onboarding and confidential HR matters. In humanitarian roles with the Hellenic Red Cross, IOM and One Happy Family, I worked in high-volume reception, case-handling and referral settings where urgent and sensitive cases had to be recognised quickly.

That experience shaped the design choices here: a protected lane for personal and safety matters, required fields so that people are not asked twice, and suspicion of any automation that routes sensitive requests without a person seeing them.

**The organisation, process, data and figures are invented.** They do not describe Libre Space Foundation or any other organisation I have worked with, and no employer data was used.

## Main conclusion

The changes that remove the safety risk and shorten the largest avoidable waits **need no AI**: a required-field form, one request per submission, a protected lane for safety and personal matters, and rules that route only when the web form agrees. AI is proposed only for unclear requests, as a suggestion a coordinator confirms, in a time-boxed pilot with defined stop criteria.

## Contents

| Step | Document |
|---|---|
| 1. Business problem | [docs/01-business-problem.md](docs/01-business-problem.md) |
| 2. Current state | [docs/02-current-state.md](docs/02-current-state.md) |
| 3. Baseline and data | [docs/03-baseline-and-data.md](docs/03-baseline-and-data.md) |
| 4. Future state | [docs/04-future-state.md](docs/04-future-state.md) |
| 5. AI solution design | [docs/05-ai-solution-design.md](docs/05-ai-solution-design.md) |
| 6. Evaluation framework | [docs/06-evaluation-framework.md](docs/06-evaluation-framework.md) |
| 7. Risk register | [docs/07-risk-register.md](docs/07-risk-register.md) |
| 8. Implementation roadmap | [docs/08-implementation-roadmap.md](docs/08-implementation-roadmap.md) |
| 9. Business recommendation | [docs/09-business-recommendation.md](docs/09-business-recommendation.md) |

Generated reports: [baseline](reports/baseline-report.md), [rules evaluation](reports/rules-evaluation.md), [effort scenarios](reports/effort-scenarios.md).

## What is real and what is not

| Item | Status |
|---|---|
| Organisation, requests, timings | Synthetic |
| Rules and guardrail code | Implemented, tested |
| Rules accuracy | Measured on synthetic held-out data; optimistic because one author wrote data and rules |
| Prompt | Draft, never run |
| AI accuracy and time savings | Not measured; scenarios only |
| Example AI outputs | Hand-written to test the guardrails, not model output |

## Run it

Python 3.10 or later, standard library only. Tests need `pytest`.

```bash
cd projects/ai-assisted-operations-improvement
python src/generate_data.py   # regenerate the synthetic data (deterministic)
python src/evaluate.py        # regenerate the three reports
python -m pytest -q tests
```

## Skills shown

Process analysis and mapping, baseline and metric design, evaluation design with a held-out split, risk-based control design, writing a business recommendation that includes "not yet" as an option, and small, tested Python.
