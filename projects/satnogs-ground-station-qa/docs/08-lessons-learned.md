# 08 — Lessons learned

These lessons are written as general testing practice. Where a lesson came from an observation that was not resolved with the maintainers, the original issue is deliberately not described.

## Planning

- **Order tests by blast radius, not by area number.** Read-only checks first, passive live passes next, disruptive tests last and only with sign-off.
- **Budget the scarcest resource explicitly.** Here it was real satellite passes. Counting them up front protected the most expensive tests.
- **Write gates as numbers.** "Leave enough time" leads to rushed fault injection; "at least 15 minutes" does not.

## Evidence

- **"It passed" needs a reason.** Every status carries an evidence class; derived claims are labelled.
- **Absence of a record is not a pass.** `NOT RECORDED` is reported on its own line.
- **Environment failures are not product failures.** A validity gate (the connectivity probe) stops an unreliable uplink from being reported as a software defect.
- **Contradictions are results.** When two tests disagree, keep both with their evidence instead of choosing the comfortable answer.

## Diagnosis

- **Most risk sits in recovery, not the happy path.** Design as much effort into restarts, contention and network loss as into the clean pass.
- **Check the user-visible outcome, not only the logs.** A system that is quiet on success can also be quiet on failure; confirm delivery from the receiving side.
- **Error text can describe the wrong failure.** Confirm an injected fault by its observable signature (timing, state) rather than by the message printed.
- **A test that crosses many components needs an attribution step.** For each failure, record which boundary it was observed at before guessing at a cause.

## Reporting

- **Separate observation, candidate and confirmed defect.** Only maintainers confirm defects; a tester's job is to make the evidence strong enough for that decision.
- **Keep private evidence complete and public excerpts minimal.** Publishing is a separate, reviewed step.

## Automation

- **Manual first, then automate what was proven.** The regression procedure was run by hand before deciding what to script, which kept automation focused on judging evidence rather than replacing human gates.
