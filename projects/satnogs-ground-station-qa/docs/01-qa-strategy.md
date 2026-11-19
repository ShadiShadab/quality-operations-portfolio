# 01 — QA strategy

## Goal

Produce **reliable evidence** about whether a real ground station completes the full observation chain, and how it behaves when parts of that chain fail. The focus is the station-side software (SatNOGS Client, flowgraphs, SDR integration) and its interaction with the SatNOGS Network and DB.

## Scope

| In scope | Out of scope |
|---|---|
| Network UI and API behaviour a station owner depends on: authentication, station management, scheduling, permissions, observation records | Load or performance testing of shared public services |
| Client job retrieval, SDR initialisation, flowgraph execution, artifact generation and upload | RF hardware design and antenna performance |
| Failure handling: network loss, client restart, SDR contention, flowgraph failure, invalid configuration | Decoder correctness for specific satellites |
| Regression of client and flowgraph upgrades | Changing upstream code |

## Test levels

1. **Area-based functional tests.** 16 areas that mirror the system components ([03](03-risk-based-execution.md)).
2. **End-to-end tests.** Scenarios that cross every component boundary: a clean pass, a network interruption during capture, and an SDR failure followed by recovery ([05](05-end-to-end-test-design.md)).
3. **Release regression.** A short critical-path suite run against a baseline captured *before* each update ([06](06-release-regression-method.md)).

## Principles

- **Representative, not exhaustive.** The aim is risk reduction, not a high test count.
- **Execution order follows impact on the station.** Read-only checks first, passive live passes second, disruptive tests last and only after explicit sign-off.
- **The production client is never edited by hand.** Destructive configuration tests run in a disposable container.
- **Every status carries an evidence class** ([04](04-evidence-standard.md)). "Not recorded" is never treated as a pass.
- **Environment problems are not product findings.** A lost uplink or a local permission error makes a result `BLOCKED`, not `FAIL`.
- **Overlapping scenarios keep separate statuses.** One test is never used to silently close another.

## Definition of done for a scenario

A scenario is done when it has:

1. a status from the shared vocabulary;
2. an evidence class;
3. the location of the raw evidence; and
4. if it did not pass, a written observation with its risk and a recommendation.

## What "done" does not mean

A completed plan means the planned scenarios were executed and recorded. It does **not** mean the system is defect-free, that a release is certified, or that untested paths behave correctly.
