# Illustrative AI outputs

`illustrative_ai_outputs.jsonl` contains **hand-written** examples of what an AI triage step might return, including deliberately broken and risky outputs. They were written to test the controls in `src/ai_guardrails.py`.

They were **not produced by any AI model**, and they say nothing about how well a model would perform. Each line contains:

| Field | Meaning |
|---|---|
| `case` | What the example tests |
| `request` | A short synthetic request |
| `raw_output` | The text an AI step might return (`null` = no output, for example a timeout) |
| `expected_lane` | Where the controls must send it: `SUGGEST`, `REVIEW` or `PROTECTED` |
