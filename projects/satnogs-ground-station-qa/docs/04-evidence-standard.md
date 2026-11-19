# 04 — Evidence standard

No result is stronger than the evidence behind it.

## Evidence classes

| Tag | Meaning |
|---|---|
| RAW | Raw terminal or API output is preserved |
| UI | Browser-only check, supported by screenshots |
| REPORTED | Operator or summary statement; raw output not preserved |
| DERIVED | A conclusion drawn from other evidence; always labelled, never presented as measured |
| PROPOSED | A step that was suggested but never executed |
| EXTERNAL | Official documentation or upstream tracker, with the date it was read |

## Status vocabulary

| Status | Use it when |
|---|---|
| `PASS` | Every stated criterion was met and evidenced |
| `FAIL` | A criterion was not met in a valid test window |
| `BLOCKED` | The test could not run validly (environment, access, missing resource) |
| `PARTIAL` | Some criteria evidenced, others not |
| `INCONCLUSIVE` | Evidence exists but does not support either conclusion |
| `COVERAGE GAP` | A part of the scenario that the procedure did not exercise |
| `NOT EXECUTED` | Planned, not run |
| `NOT RECORDED` | No outcome exists in the record. **Never** counted as a pass |

A simple Passed/Failed/Blocked lifecycle is common in test-management tools. The extra values exist because real execution produces them, and collapsing them into pass/fail hides information that a decision-maker needs.

## Observation versus defect

| Term | Meaning in this project |
|---|---|
| Observation | Behaviour recorded with evidence that may or may not be a defect |
| Candidate defect | An observation the tester believes is wrong, not yet reviewed by maintainers |
| Confirmed defect | Accepted by the maintainers in the project's issue tracker |

Only confirmed defects should be described publicly as bugs. This portfolio publishes none of the observations from the original work.

## Recording rules

1. Preserve raw output; a summary is not evidence.
2. Record the HTTP status code of every API call.
3. Use UTC timestamps in a single format.
4. Hash evidence files when they are saved and list them in a run log.
5. Substitute every placeholder before running a command. An unsubstituted placeholder produces misleading errors.
6. Save logs before every update and at every milestone; container logs do not survive a re-creation.
7. Do not truncate log lines while diagnosing; truncation can hide the real error.
8. Treat configuration backups as secrets: restrict permissions, delete them once a revert is verified, and never share them.
9. A result whose window contains a connectivity-probe failure is `BLOCKED`, never `FAIL`.
10. Never invent a pass/fail threshold. If none is specified, report the raw value against named reference points.

## Private evidence versus public excerpts

Preserving evidence and publishing it are separate steps. Raw evidence is kept complete in a private record. Anything shared publicly is a reviewed excerpt with credentials, locations, host details and personal information removed or replaced with synthetic values.

See [templates/run-log.md](../templates/run-log.md) and [templates/defect-report.md](../templates/defect-report.md).
