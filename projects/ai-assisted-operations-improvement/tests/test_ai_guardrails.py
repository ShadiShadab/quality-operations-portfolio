# SPDX-License-Identifier: AGPL-3.0-or-later
import json
from pathlib import Path

import pytest

import ai_guardrails as ag

EXAMPLES = Path(__file__).resolve().parents[1] / "examples" / "illustrative_ai_outputs.jsonl"
CASES = [json.loads(line) for line in EXAMPLES.read_text(encoding="utf-8").splitlines() if line.strip()]


@pytest.mark.parametrize("case", CASES, ids=[c["case"] for c in CASES])
def test_illustrative_outputs_reach_the_expected_lane(case):
    assert ag.decide(case["request"], case["raw_output"])["lane"] == case["expected_lane"]


def test_examples_cover_every_lane():
    assert {c["expected_lane"] for c in CASES} == {"SUGGEST", "REVIEW", "PROTECTED"}


def test_nothing_is_auto_applied():
    # The pilot design never returns an AUTO lane from the AI path.
    lanes = {ag.decide(c["request"], c["raw_output"])["lane"] for c in CASES}
    assert "AUTO" not in lanes


def test_boolean_is_not_accepted_as_confidence():
    raw = json.dumps({"category": "FINANCE", "priority": "P3", "confidence": True,
                      "summary": "s", "missing_fields": [], "rationale": "r"})
    out, problems = ag.parse_and_validate(raw)
    assert out is None and any("confidence" in p for p in problems)
