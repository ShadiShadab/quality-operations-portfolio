# 02 — System under test

## Components and interfaces

| # | Component | Interface | Typical symptom the operator sees when it fails |
|---|---|---|---|
| 1 | Station host, SDR, antenna | USB, container runtime | Station appears offline; SDR not found or busy |
| 2 | Scheduling | Network UI and REST API | Observation rejected; unexpected pass window |
| 3 | Network API | Jobs, observations and stations endpoints | Client cannot fetch jobs; unclear status codes |
| 4 | SatNOGS Client | Container with an internal scheduler | Job not started |
| 5 | SDR initialisation | SoapySDR / RTL-SDR driver | Device busy or not opened |
| 6 | Flowgraph | gr-satnogs scripts launched per mode | Capture ends early or produces nothing |
| 7 | Artifacts | Audio, waterfall, demodulated data | Missing or truncated files |
| 8 | Upload | Client → Network | Retries; incomplete records |
| 9 | Network record | Observation page and API fields | Record incomplete or status not updated |
| 10 | Review | Vetting in the UI | Outcome hard to interpret |
| — | SatNOGS DB | Satellites, transmitters, orbital data | Stale or inconsistent reference data |

The point of the table is attribution: the same operator symptom ("no data") can originate in at least six different components, so every test records *which boundary* it exercises.

## Representative station profile

The method was applied on a single, typical volunteer station. Exact identifiers and configuration are not needed to understand the method and are omitted.

| Item | Representative value |
|---|---|
| Host | Small arm64 single-board computer |
| Deployment | The standard SatNOGS setup tooling (Ansible-based), running the client in Docker Compose with a read-only root filesystem |
| Client and flowgraphs | SatNOGS Client 2.1.x; satnogs-flowgraphs 2.6 → 2.7 during the regression |
| SDR | RTL-SDR-class USB receiver |
| Antenna | Simple VHF/UHF antenna with a fixed minimum horizon |
| Uplink | Consumer-grade connection that is not always on |

## Environment characteristics that shaped the tests

- **Intermittent uplink.** A lightweight DNS/HTTP connectivity probe ran alongside the tests. Any result whose time window contains probe failures is `BLOCKED`, not `FAIL`.
- **Success is quiet.** At its default log level the client logs little on a successful job retrieval or upload, so delivery is proven from the Network side (API fields, artifact availability), not from the absence of errors.
- **Limited tools inside the container.** Diagnostic commands had to be chosen from what the image provides, which shaped how evidence was collected.
- **Public pages can lag.** Some Network page fields update only after the next observation, so versions are verified directly on the host.

## Public references

- [SatNOGS documentation](https://docs.satnogs.org/)
- [SatNOGS wiki](https://wiki.satnogs.org/)
- [SatNOGS projects on GitLab](https://gitlab.com/librespacefoundation/satnogs)
