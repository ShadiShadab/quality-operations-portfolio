# SPDX-License-Identifier: AGPL-3.0-or-later
"""Validation and routing controls for AI-suggested triage.

No AI model is called anywhere in this repository. This module defines what
an AI suggestion must look like and what happens to it, so that the controls
can be tested *before* any model is connected. The tests use hand-written,
illustrative outputs (examples/illustrative_ai_outputs.jsonl), not model
outputs.

Design rule: fail closed. Anything malformed, uncertain, sensitive or
suspicious goes to a person.
"""
from __future__ import annotations

import json

from triage_rules import CATEGORIES, SENSITIVE, REQUIRED_FIELDS, injection_suspected, protected_hint

CONFIDENCE_THRESHOLD = 0.80
MAX_SUMMARY_CHARS = 300
PRIORITIES = {"P1", "P2", "P3"}
KNOWN_FIELDS = {f for fs in REQUIRED_FIELDS.values() for f in fs}
REQUIRED_KEYS = {"category", "priority", "confidence", "summary", "missing_fields", "rationale"}


def parse_and_validate(raw: str) -> tuple[dict | None, list[str]]:
    """Return (output, problems). output is None if it cannot be used at all."""
    try:
        out = json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return None, ["not valid JSON"]
    if not isinstance(out, dict):
        return None, ["not a JSON object"]
    problems = []
    missing = REQUIRED_KEYS - out.keys()
    if missing:
        problems.append("missing keys: " + ", ".join(sorted(missing)))
    extra = out.keys() - REQUIRED_KEYS
    if extra:
        problems.append("unexpected keys: " + ", ".join(sorted(extra)))
    if out.get("category") not in CATEGORIES:
        problems.append("unknown category")
    if out.get("priority") not in PRIORITIES:
        problems.append("unknown priority")
    conf = out.get("confidence")
    if not isinstance(conf, (int, float)) or isinstance(conf, bool) or not 0 <= conf <= 1:
        problems.append("confidence must be a number between 0 and 1")
    if not isinstance(out.get("summary"), str) or len(out.get("summary", "")) > MAX_SUMMARY_CHARS:
        problems.append("summary missing or too long")
    mf = out.get("missing_fields")
    if not isinstance(mf, list) or any(f not in KNOWN_FIELDS for f in mf):
        problems.append("missing_fields must list known field names")
    return (None if problems else out), problems


def decide(req: dict, raw_ai_output: str | None) -> dict:
    """Combine request-level controls with an AI suggestion.

    Returns {"lane": PROTECTED | REVIEW | SUGGEST, "reasons": [...], "suggestion": {...} | None}.
    SUGGEST means the suggestion is pre-filled for a coordinator to confirm with
    one action. In the proposed pilot nothing is applied without confirmation.
    """
    reasons = []
    if protected_hint(req) or (req.get("form_category") or "") in SENSITIVE:
        return {"lane": "PROTECTED", "reasons": ["request-level protected hint"], "suggestion": None}
    if raw_ai_output is None:
        return {"lane": "REVIEW", "reasons": ["no AI output"], "suggestion": None}
    out, problems = parse_and_validate(raw_ai_output)
    if out is None:
        return {"lane": "REVIEW", "reasons": ["invalid AI output: " + "; ".join(problems)], "suggestion": None}
    if out["category"] in SENSITIVE:
        return {"lane": "PROTECTED", "reasons": ["AI suggests a sensitive category"], "suggestion": out}
    if injection_suspected(req):
        reasons.append("instruction-like text in request")
    if out["confidence"] < CONFIDENCE_THRESHOLD:
        reasons.append(f"confidence {out['confidence']:.2f} below {CONFIDENCE_THRESHOLD:.2f}")
    form = req.get("form_category") or ""
    if form and form != out["category"]:
        reasons.append(f"form says {form}, AI says {out['category']}")
    if reasons:
        return {"lane": "REVIEW", "reasons": reasons, "suggestion": out}
    return {"lane": "SUGGEST", "reasons": ["all checks passed"], "suggestion": out}
