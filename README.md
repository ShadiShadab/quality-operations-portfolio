# Shadi Shadabshoar — Quality, Operations and Product Portfolio

I work where operations, quality and technology meet. I analyse how a process or system really behaves, decide what evidence is good enough, identify the risks, and turn the findings into practical recommendations.

My experience includes software QA for SatNOGS ground-station software at Libre Space Foundation (January–October 2026), office, HR and finance operations at the same organisation (January 2024 – January 2026), service coordination in humanitarian programmes, operations project coordination, and sales team leadership. I hold a BSc in Electronic and ICT Engineering and an MSc in International Business & Management, and completed the MIT Emerging Talent programme in Computer & Data Science.

This repository contains two case studies. They are written to show **how I reason and decide**, with the evidence for each claim and its limits stated next to it.

## Projects

| Project | What it shows | Evidence level |
|---|---|---|
| [SatNOGS ground station: risk-based end-to-end QA](projects/satnogs-ground-station-qa/) | QA strategy for a distributed open-source system: risk-ordered execution, evidence standards, end-to-end and recovery test design, release regression, a staged automation roadmap | Testing executed on my own station in 2026; methodology published, raw evidence and unresolved observations withheld |
| [AI-assisted operations improvement: request intake and triage](projects/ai-assisted-operations-improvement/) | Operations redesign with a business case: process mapping, baseline design, a rules baseline evaluated on held-out data, AI controls that fail closed, risk register, pilot plan and a recommendation | Proposal and simulation on synthetic data; no AI model was called |

## Roles this portfolio supports

- **Business, technical or product operations:** process analysis, baselines and KPI definitions, phased roadmaps with exit criteria, risk ownership.
- **Technical project or programme coordination:** scoping, sequencing work by risk, gates and sign-offs, communicating status and limits.
- **QA lead and quality operations:** test strategy, risk-based prioritisation, evidence and reporting standards, regression method.
- **Product management,** where the role values problem framing, option comparison and stating what would change a recommendation.

QA is the technical foundation of this portfolio, not its only focus.

## How to read the claims

Each document labels its content. The labels mean:

| Label | Meaning |
|---|---|
| Executed | I carried out the test or activity; the record is mine |
| Measured (synthetic) | Produced by running code on synthetic data in this repository |
| Designed / Proposed | A plan or design that has not been carried out |
| Scenario | Calculated from stated assumptions; not a result |
| Observation | Something seen once and not confirmed; not presented as a defect |

Neither project certifies software, proves system reliability, or reports measured AI performance.

## Run the tests

Python 3.10 or later. The code uses only the standard library; the tests need `pytest`.

```bash
python -m pip install pytest
python -m pytest -q projects/ai-assisted-operations-improvement/tests
```

The same commands run in GitHub Actions on every push, which also checks that the operations reports regenerate exactly from the committed data.

## Provenance

- **SatNOGS case study.** The testing was carried out by me, on a station I own, as part of my QA role at Libre Space Foundation. The method comes from a Master QA Plan I developed during that work: I set its overall risk-based structure, including the 16 test areas and the regression approach, from my testing knowledge, work, observations and decisions. The plan was informed by the existing SatNOGS/LSF project context and formal test cases, and AI assisted with drafting, structuring, consolidation and refinement. This edition is a generalised write-up, not the plan itself. It is not Libre Space Foundation documentation, and Libre Space Foundation has not reviewed, approved or endorsed this repository. SatNOGS is a [Libre Space Foundation](https://libre.space/) project.
- **Operations case study.** I chose the problem from my operations and humanitarian experience and set the design decisions and limits. The fictional organisation, synthetic data generator, rules, guardrail code, tests and reports were generated with AI assistance under my direction. No AI model is called by the code, and no AI triage was run or measured.
- **What was tested.** The code is covered by unit tests that run in GitHub Actions on every push. The rules were evaluated on synthetic data only. The AI tool did not carry out any of the SatNOGS testing described here.
- **Responsibility.** I am responsible for the content of this edition.

## Licence

| Content | Licence | File |
|---|---|---|
| Documentation, templates, prompts, synthetic data and reports | Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) | [LICENSE-DOCS](LICENSE-DOCS) |
| Code in `src/` and `tests/` | GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later) | [LICENSE-CODE](LICENSE-CODE) |

These match the licences used across the [SatNOGS project](https://libre.space/projects/satnogs/) for documentation and network software. SatNOGS names and links are used for identification only.

## Contact

[LinkedIn](https://www.linkedin.com/in/shadi-shadabshoar/) · [GitHub](https://github.com/ShadiShadab)
