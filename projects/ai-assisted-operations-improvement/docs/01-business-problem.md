# 1. Business problem

> **Status: proposal and simulation.** The organisation is fictional and the data is synthetic. Nothing here describes a real organisation, a pilot or a measured result.

## Context

The setting is fictional, but it combines two kinds of work I have done: office, HR and finance operations in a small technology non-profit, and service coordination in humanitarian programmes with field teams. It is not a description of any of those organisations.

A small non-profit coordinates several field teams, a partner liaison team and a head office. A three-person **programme support office** handles internal requests: purchases, travel and vehicles, system access, payments, contracts, report figures, and safety or security concerns.

Requests arrive by shared email inbox (about 60%) and by a basic web form with a category drop-down (about 40%). One coordinator reads each request and forwards it to the person who handles that type of work.

## Problem statement

Requests take too long to reach the right person with the information needed to act, and urgent safety matters wait in the same queue as routine orders.

## Why it matters

| Stakeholder | Effect of the current process |
|---|---|
| Field teams | Wait for purchases, vehicles and access; repeat information when asked for it later |
| Coordinators | Spend time reading, routing and chasing missing details instead of resolving requests |
| Management | Cannot see volumes, delays or bottlenecks without counting emails by hand |
| Safety focal point | Depends on someone noticing an urgent message in a busy inbox |

## Decision this case study supports

Should the office change its intake process, and if so, is there a role for AI in triage, and under what controls?

The case study is designed so that **"no AI"** or **"not yet"** are possible answers.

## Options considered

I compared five operations problems before choosing this one.

| Candidate | Value if solved | Data available for a portfolio | Risk | Chosen? |
|---|---|---|---|---|
| Request intake and triage | High: affects every team daily | Can be simulated realistically; close to my own operations experience | Medium: sensitive requests must be protected | **Yes** |
| Weekly report consolidation | Medium | Needs realistic report content | Low | No |
| Supplier document intake | Medium | Needs realistic invoices | Medium: financial data | No |
| Knowledge retrieval for policies | Medium | Needs a policy corpus | Medium: wrong answers look authoritative | No |
| QA log triage | Medium | Overlaps with the SatNOGS project | Low | No: keeps the two projects distinct |

## Out of scope

- Resolving requests (approving purchases, making payments, granting access).
- HR or safety case handling. These are routed to people, never processed by AI.
- Choosing a specific AI vendor or ticket system.
