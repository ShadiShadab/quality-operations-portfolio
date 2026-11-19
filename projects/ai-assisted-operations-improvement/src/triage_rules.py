# SPDX-License-Identifier: AGPL-3.0-or-later
"""Rules baseline for request triage and completeness checks.

This is the *conventional automation* part of the proposed workflow. It is
deterministic, explainable and cheap, and it is written first so that any
AI component has to beat a transparent baseline.

The keyword lists were written by reading the development split (weeks 1-6)
only. They are deliberately simple: the point is to see where simple rules
are good enough and where they are not.
"""
from __future__ import annotations

import re

CATEGORIES = [
    "PROCUREMENT", "TRAVEL_LOGISTICS", "IT_ACCESS", "FINANCE",
    "HR_CONTRACTS", "REPORTING_DATA", "SAFETY_SECURITY",
]
SENSITIVE = {"HR_CONTRACTS", "SAFETY_SECURITY"}

KEYWORDS = {
    "PROCUREMENT": ["purchase", "procurement", "order", "buy", "supplies", "run out"],
    "TRAVEL_LOGISTICS": ["travel", "vehicle", "trip", "accommodation", "driver", "book a"],
    "IT_ACCESS": ["log in", "login", "password", "access", "account", "permission denied"],
    "FINANCE": ["reimburse", "invoice", "payment", "paid", "receipt", "per diem"],
    "HR_CONTRACTS": ["contract", "leave", "payslip", "hr"],
    "REPORTING_DATA": ["report", "figures", "data", "spreadsheet", "how many"],
    "SAFETY_SECURITY": ["security", "incident", "safety", "urgent"],
}

# Words that should send a request to the protected (human-only) lane even if
# the category rules disagree. A false alarm costs a few minutes; a missed
# safety or personal matter costs much more.
PROTECTED_HINTS = [
    "incident", "security", "safety", "unsafe", "hurt", "injured", "threat",
    "blocked by", "stopped and searched", "crowd",
    "contract", "payslip", "personal matter", "confidential", "harass",
]

INJECTION_PATTERNS = [
    r"ignore (all |your )?(previous|prior) instructions",
    r"^\s*system\s*:", r"\bsystem\s*:", r"you are now",
]

SITES = ["northern site", "regional office", "coastal site", "capital"]
SYSTEMS = ["shared drive", "finance system", "email group", "survey platform", "case database"]
ITEMS = ["toner", "lantern", "projector", "stationery", "water filter", "router"]
REPORTS = ["monthly activity report", "donor quarterly report", "attendance summary", "distribution tracker"]
_MONTH = r"(January|February|March|April|May|June|July|August|September|October|November|December)"

REQUIRED_FIELDS = {
    "PROCUREMENT": ["item", "budget_code"],
    "TRAVEL_LOGISTICS": ["destination", "dates"],
    "IT_ACCESS": ["system"],
    "FINANCE": ["amount"],
    "HR_CONTRACTS": [],
    "REPORTING_DATA": ["report", "deadline"],
    "SAFETY_SECURITY": ["location"],
}


def _text(req: dict) -> str:
    return f"{req.get('subject', '')} {req.get('body', '')}".lower()


def _word_hit(text: str, kw: str) -> bool:
    return re.search(r"\b" + re.escape(kw), text) is not None


def classify(req: dict) -> tuple[str | None, str]:
    """Return (category or None, reason). None means the rules abstain."""
    text = _text(req)
    scores = {c: sum(_word_hit(text, k) for k in kws) for c, kws in KEYWORDS.items()}
    best = max(scores.values())
    if best == 0:
        return None, "no rule matched"
    top = [c for c, s in scores.items() if s == best]
    if len(top) > 1:
        return None, "rules conflict: " + ", ".join(sorted(top))
    return top[0], f"keyword score {best}"


def protected_hint(req: dict) -> bool:
    text = _text(req)
    return any(h in text for h in PROTECTED_HINTS)


def injection_suspected(req: dict) -> bool:
    text = _text(req)
    return any(re.search(p, text, flags=re.I | re.M) for p in INJECTION_PATTERNS)


def present_fields(req: dict) -> set[str]:
    text = _text(req)
    found = set()
    if any(i in text for i in ITEMS):
        found.add("item")
    if re.search(r"\bbc-\d{4}\b", text):
        found.add("budget_code")
    if any(s in text for s in SITES):
        found.update({"destination", "location"})
    if re.search(rf"from \d{{1,2}} {_MONTH} to \d{{1,2}} {_MONTH}", text, flags=re.I):
        found.add("dates")
    if any(s in text for s in SYSTEMS):
        found.add("system")
    if re.search(r"\beur \d+", text):
        found.add("amount")
    if any(r in text for r in REPORTS):
        found.add("report")
    if re.search(rf"\bby \d{{1,2}} {_MONTH}", text, flags=re.I):
        found.add("deadline")
    return found


def missing_fields(req: dict, category: str) -> list[str]:
    """Required fields for `category` that cannot be found in the request."""
    have = present_fields(req)
    return [f for f in REQUIRED_FIELDS.get(category, []) if f not in have]


def route(req: dict) -> dict:
    """Rules-only routing decision for the proposed future-state workflow.

    Lanes:
      PROTECTED - human-only queue (safety, HR, personal matters)
      AUTO      - routed to a queue without a person reading it first
      REVIEW    - a coordinator decides (in the AI-assisted design, this is
                  where an AI suggestion would be shown)
    """
    category, reason = classify(req)
    form = req.get("form_category") or ""
    if protected_hint(req) or category in SENSITIVE or form in SENSITIVE:
        return {"lane": "PROTECTED", "category": category, "reason": "protected hint or sensitive category"}
    if injection_suspected(req):
        return {"lane": "REVIEW", "category": category, "reason": "instruction-like text in request"}
    if category is None:
        return {"lane": "REVIEW", "category": None, "reason": reason}
    if form and form != category:
        return {"lane": "REVIEW", "category": category, "reason": f"form says {form}, rules say {category}"}
    return {"lane": "AUTO", "category": category, "reason": reason}
