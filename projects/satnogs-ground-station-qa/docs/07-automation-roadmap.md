# 07 — Automation roadmap

**Status: proposed, not built.** Everything on this page is a plan.

The principle: anything that reads and judges evidence can be scripted. What stays manual is what needs a real satellite pass, a human decision or an interactive login.

## What can and cannot be automated

| Step | Automatable? | Proposed approach |
|---|---|---|
| Pre/post version snapshot and comparison | Yes, first candidate | One script that records versions and hashes, then compares them |
| Log save, configuration backup and hash comparison | Yes | Same script; configuration content never printed |
| Connectivity probe and validity check | Yes | Probe loop plus a validity check for a given time window |
| Per-observation verification (regression items 4–9) | Yes; highest value | A verifier that checks API fields, artifact sizes, timing, log window and probe validity, and prints a PASS / FAIL / BLOCKED table |
| Verify after every observation | Yes | Triggered by the end-of-pass log line |
| Release detection | Partly | Watch published image tags or announcements |
| Scheduling | Probably | Network API with a dedicated user token, once the API documentation confirms it is supported |
| Browser checks (sign-in, vetting) | Possible but brittle | Browser automation with a dedicated test account and secrets from a store |
| The update itself and the final verdict | **No** | Human gate |

A related, separately published tool, [satnogs-observation-verifier](https://github.com/ShadiShadab/satnogs-observation-verifier), explores the per-observation verification step against public data.

## Staged plan

| Stage | Deliverable | Status |
|---|---|---|
| 1 | Snapshot script and per-observation verifier | Proposed. The verifier prototype linked above is a separate project, not part of this roadmap |
| 2 | Verify after each pass; report generated from structured results | Proposed |
| 3 | Manually triggered job that runs stage 1–2 on the station and stores the report | Proposed |
| 4 | Browser automation for sign-in and scheduling | Proposed |

## Design rules

1. Baseline values live in one data file, so thresholds are data, not code.
2. The validity rule is built in: a probe failure in the window gives `BLOCKED`, never `FAIL`.
3. Evidence files are hashed automatically; secrets never reach a log or report.
4. Human gates before the update and before the final verdict.
5. The output is the same 11-item table, so runs are directly comparable.
