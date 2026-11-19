# 6. Evaluation framework

> **Status: rules results are measured on synthetic data. AI results do not exist.** No model was evaluated.

## Labels used in this project

| Label | Meaning |
|---|---|
| **Measured (synthetic)** | Calculated by running code on the synthetic dataset |
| **Scenario** | Calculated from assumptions; shows what would need to be true |
| **Expected benefit** | A reasoned expectation, not a number |
| **Pilot measure** | Defined here, to be measured in a real pilot |

## What was measured: the rules baseline

The rules were written against weeks 1–6 (development) and evaluated once on weeks 7–12 (held-out). Full output: [reports/rules-evaluation.md](../reports/rules-evaluation.md).

| Held-out measure (synthetic) | Value |
|---|---|
| Rules gave an answer | 84.6% |
| Correct when an answer was given | 90.1% |
| Silent misroutes, Policy A | 17 of 214 auto-routed (7.9%) |
| Silent misroutes, Policy B | 0 of 68 auto-routed |
| Sensitive requests sent to PROTECTED | 32 of 32 |
| Non-sensitive requests sent to PROTECTED | 5 |
| Missing-information check: recall / precision | 100% / 64.4% |

### How to read these figures

- **They are optimistic.** The same person wrote the generator and the rules.
- **Recall of 100% for missing information is partly circular:** the check looks for the formats the generator uses. The precision of 64% is the more informative figure: when fields are written informally, the check asks for information the requester already gave. A required field in the web form is a cheaper fix than AI.
- **The missing-information check is scored with the true category.** In real use it would run on the chosen category, so routing errors would add further mistakes.
- **Most Policy A misroutes come from messages that contain two requests** (12 of 17), which supports the "one request per submission" change.
- **Policy B's zero misroutes rest on an assumption.** The generator picks wrong web-form categories at random. Real requesters may pick the wrong category for the same misleading keywords that confuse the rules; their errors would then coincide, and Policy B would misroute more often. A pilot spot-check of the AUTO lane is still required.
- **Sensitive protection is 32 of 32 on synthetic data only, and partly circular:** the hint list was written with knowledge of the generator's vocabulary. Real messages will contain phrasing the list does not cover. The pilot must keep a human safety check.

## What was tested: the guardrails

`tests/test_ai_guardrails.py` runs 12 hand-written outputs through the guardrails, including broken JSON, unknown categories, extra keys, low confidence, sensitive suggestions and instruction-like text. All reach the expected lane. This shows the **controls behave as designed**; it says nothing about model quality.

## What a pilot must measure

| Pilot measure | Why it matters | Suggested adoption threshold |
|---|---|---|
| Coordinator acceptance rate of AI suggestions | Drives the time saving | Set before the pilot; the scenarios use 40–80% |
| Accepted-but-wrong rate | The real risk: a person confirms a wrong suggestion | Lower than the coordinators' own disagreement rate |
| Sensitive requests that reached the AI path | Must be zero | 0 |
| Time to first touch for safety requests | The main safety goal | No safety request waits more than 1 h in working hours |
| Information follow-ups per request | Tests the form change | Lower than baseline |
| Coordinator feedback | Usability | Qualitative |

## Pilot design

1. **Shadow mode (weeks 1–2):** AI suggestions are logged but not shown. Compare with coordinators' decisions.
2. **Assisted mode (weeks 3–6):** suggestions are shown in the REVIEW lane only. Coordinators confirm or correct.
3. **Decision:** adopt, adjust, or stop, using the thresholds above.
