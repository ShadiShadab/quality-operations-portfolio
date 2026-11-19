# 9. Business recommendation

> **Status: recommendation based on a simulation.** Figures are synthetic or scenario-based and must be replaced with real measurements before any decision.

## Recommendation

1. **Do the process work first (phases 0–2).** Required-field intake, one request per submission, a protected lane and Policy B rules address the main delays and the safety risk without AI.
2. **Run a time-boxed AI pilot only for the REVIEW lane**, starting in shadow mode, with adoption decided by measured acceptance and error rates.
3. **Do not allow AI to route, approve or handle HR and safety requests.**

## Why

| Finding | Type |
|---|---|
| Handler work is 67% of simulated elapsed time and is outside the scope of this redesign; waiting for first touch (17%) and for missing information (12%) are the largest parts the redesign can influence | Simulated baseline |
| Rules decide alone (Policy A): 17 silent misroutes in 214 auto-routed held-out requests | Measured (synthetic) |
| Rules plus form agreement (Policy B): no silent misroutes in 68 auto-routed requests | Measured (synthetic) |
| Policy B reduces triage minutes by about 19% compared with manual triage | Scenario |
| Adding AI suggestions to REVIEW could raise the reduction to 36–52%, if 40–80% of suggestions are accepted | Scenario, depends on unmeasured acceptance |
| Total coordinator triage and follow-up effort is about 4.3 h per week | Simulated baseline |

The last row is important. In the scenarios, AI suggestions save about 35–70 coordinator minutes per week beyond Policy B (40–80% acceptance, 311 held-out requests over 6 weeks). This is a scenario estimate on synthetic data, not a measured saving. The stronger arguments for change are the safety lane, shorter waits before first touch and fewer follow-ups, none of which needs AI. End-to-end resolution time will improve only modestly, because most of it is the handlers' own work. AI is worth piloting only if those hours matter to the team, or if request volume grows.

## Decision requested

Approve phases 0–2. Decide on phases 3–5 after the real baseline is known.

## What would change this recommendation

- A real baseline showing much higher volume or triage effort would strengthen the case for AI.
- Low agreement between coordinators on categories would mean neither rules nor AI can be accurate, and the category list should be simplified first.
- If the organisation cannot approve an AI provider for this data, phases 3–5 should not proceed.
