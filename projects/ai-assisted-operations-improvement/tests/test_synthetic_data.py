# SPDX-License-Identifier: AGPL-3.0-or-later
import csv
import hashlib
import re
from pathlib import Path

import generate_data

DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic"


def rows():
    with open(DATA / "requests.csv", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def test_generator_is_deterministic(tmp_path, monkeypatch):
    before = hashlib.sha256((DATA / "requests.csv").read_bytes()).hexdigest()
    monkeypatch.setattr(generate_data, "OUT", tmp_path)
    generate_data.main()
    assert hashlib.sha256((tmp_path / "requests.csv").read_bytes()).hexdigest() == before


def test_ids_unique_and_labels_valid():
    rs = rows()
    assert len({r["request_id"] for r in rs}) == len(rs) == generate_data.N_REQUESTS
    assert {r["true_category"] for r in rs} <= set(generate_data.CATEGORIES)


def test_sensitive_flag_matches_category():
    for r in rows():
        assert (r["sensitive"] == "1") == (r["true_category"] in generate_data.SENSITIVE)


def test_no_personal_data_patterns():
    text = (DATA / "requests.csv").read_text(encoding="utf-8")
    assert not re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", text), "email address found"
    assert not re.search(r"\+?\d[\d ]{8,}\d", text), "phone-like number found"
