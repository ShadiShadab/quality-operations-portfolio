# 5. AI solution design

> **Status: design only.** No AI model was called in this project. The controls are implemented and tested in code; the model behaviour is not.

## Where AI is used, and where it is not

| Lane | AI involvement |
|---|---|
| PROTECTED | None. Request text is not sent to an AI service. |
| AUTO | None. Rules and the web form agree. |
| REVIEW | AI may suggest category, priority, a one-sentence summary and missing fields. A coordinator confirms. |

## Components

| Component | File | Status |
|---|---|---|
| Rules: category, protected hints, instruction-like text, completeness | `src/triage_rules.py` | Implemented and tested on synthetic data |
| Prompt | `prompts/triage-prompt.md` | Draft, not run |
| Output schema | `prompts/output-schema.json` | Defined |
| Guardrails: validate output and decide the lane | `src/ai_guardrails.py` | Implemented and tested with hand-written outputs |
| Model call | — | Not implemented |

## Guardrails

The guardrails **fail closed**: anything unexpected sends the request to a person.

| Condition | Result |
|---|---|
| Request contains a protected hint | PROTECTED, whatever the AI says |
| AI suggests HR or safety | PROTECTED |
| No output (timeout, outage) | REVIEW |
| Output is not valid JSON, has unknown or extra keys, or values outside the schema | REVIEW |
| Confidence below 0.80 | REVIEW |
| Web-form category disagrees with the AI | REVIEW |
| Request contains instruction-like text | REVIEW |
| Valid, confident, no conflicts | SUGGEST: pre-filled for a coordinator to confirm |

The 0.80 threshold is a starting point. It must be set during the pilot from observed acceptance and error rates, not assumed.

## Data protection

- Only the subject and body are sent; names, contact details and team are removed.
- Protected requests never leave the organisation's own systems.
- The provider must be approved under the organisation's data-processing rules, with retention and training on inputs disabled where possible.
- Suggestions and coordinator decisions are logged for evaluation, without storing more personal data than the existing inbox already holds.

## What AI could add, and what it cannot

- **Could add:** handling indirect phrasing that the rules miss (rules coverage is 74% on indirect requests and 42% on "trap" requests in the held-out data), recognising informal field formats, and choosing the main request in a multi-request message.
- **Cannot replace:** the protected lane, the required-field form, or the coordinator's responsibility for routing.
