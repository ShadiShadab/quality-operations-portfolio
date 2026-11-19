# 05 — End-to-end test design

Each scenario crosses every boundary in the chain:
Station → Schedule → Network API → Client → SDR → Flowgraph → Artifacts → Upload → Network record → Review.

## Scenarios

| Test | Question it answers | Pass criteria (summary) |
|---|---|---|
| E2E-01 Clean observation | Does a normal scheduled observation complete the whole chain? | Job retrieved on time; SDR opened; flowgraph ran for the whole pass; artifacts created, uploaded and visible on the Network; record reviewable |
| E2E-02 Network interruption during capture | If the Network becomes unreachable mid-pass, is the capture kept and delivered once the Network returns? | Capture continues while the Network is unreachable; upload succeeds after recovery; no artifact lost |
| E2E-03 SDR unavailable, then recovery | If the radio is busy at pass start, does the station fail safely and recover on the next pass without intervention? | Failure is contained to the affected pass; the next pass completes normally with no manual action |

## Execution status

All three scenarios were **executed** on my station in October 2026 and each met its stated pass criteria. Each run also recorded limitations:

- **E2E-01:** no signal was demodulated during the pass, so the decoding path remains unproven on a real signal. A pass of the chain is not proof that decoding works.
- **All scenarios:** any observation that was not resolved with the maintainers is kept in the private record and is **not** reported here, as a defect or otherwise.

## Design choices

### E2E-02 — network interruption

| Choice | Reason |
|---|---|
| Silently drop outbound HTTPS traffic from the client container to the Network, rather than rejecting it | A dropped connection hangs until it times out, which is how real outages usually behave; a fast rejection is the less realistic case |
| Apply the block only after capture start has been confirmed | Proves that capture continues while the Network is unreachable, rather than testing a different failure (no job at all) |
| Hold the block well past pass end, covering several upload attempts | Tests retry behaviour, not just a single attempt |
| Copy the local artifacts before removing the block | Local files may be deleted after a successful upload, so the reference copy must be taken first |
| Check the Network side from a separate machine | The block affects the station's path; the station's own view is not a reliable witness |
| Revert with the identical rule specification, then verify connectivity | A fault injection is not finished until the system is proven to be back in its normal state |

**Generic lesson:** verify a fault injection by its *observable signature* (for example, consistent timeout durations), not by the error text an application prints. Error messages often describe a different failure from the one injected.

### E2E-03 — SDR unavailable

| Choice | Reason |
|---|---|
| Hold the radio with a streaming process to `/dev/null` before the pass | A self-test utility was unreliable on this tuner type; a streaming reader holds the device consistently |
| Release the device early, well before the recovery pass | The failure occurs at start; holding longer adds nothing and risks the next pass |
| Stop the holding process by exact name | Avoids terminating the shell that runs the test |
| Leave the recovery pass completely untouched | The question is whether the station recovers *on its own* |

## Preconditions shared by all E2E tests

- Connectivity probe running and healthy for the whole window, otherwise the result is `BLOCKED`
- Lead time of at least 15 minutes before the pass
- No other observation within the configuration buffer
- Logs saved before and after; evidence files hashed and listed in the run log
- Explicit sign-off for E2E-02 and E2E-03 (Phase 3 disruptive tests)
