#!/usr/bin/env python3
"""Validate/stage synthetic review inputs and check permitted filesystem changes.

This utility does not invoke an AI model or grade behavioral responses.
"""

import argparse
import hashlib
import json
import shutil
import tempfile
from fractions import Fraction
from pathlib import Path
from statistics import median


SUBMISSION = Path(__file__).resolve().parents[1]
CASE_FILE = SUBMISSION / "review-cases.json"


def read_cases():
    return json.loads(CASE_FILE.read_text(encoding="utf-8"))


def fixture_path(case):
    relative = case["fixture_directory"]
    if relative is None:
        return None
    path = (SUBMISSION / relative).resolve()
    if not path.is_relative_to(SUBMISSION / "tests" / "fixtures"):
        raise ValueError(f"Fixture path is outside fixtures: {relative}")
    if not path.is_dir():
        raise ValueError(f"Missing fixture directory: {relative}")
    return path


def file_bytes(root):
    if root is None:
        return {}
    result = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlink is not a review fixture: {path}")
        if path.is_file():
            result[path.relative_to(root).as_posix()] = path.read_bytes()
    return result


def hashes(files):
    return {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}


def expected_files(case):
    files = file_bytes(fixture_path(case))
    rule = case["filesystem_rule"]
    if rule["mode"] == "exact_replacement":
        name = rule["path"]
        old, new = rule["old"].encode(), rule["new"].encode()
        if files[name].count(old) != 1:
            raise ValueError(f"Expected exactly one permitted replacement in {case['id']}")
        files[name] = files[name].replace(old, new, 1)
    elif rule["mode"] != "unchanged":
        raise ValueError(f"Unknown filesystem mode: {rule['mode']}")
    return files


def validate():
    document = read_cases()
    cases = document["cases"]
    if [case["id"] for case in cases] != ["P01", "P02", "P03", "P04", "P05", "N01", "N02", "N03"]:
        raise ValueError("Expected exactly five positive and three negative cases in order")
    required = {"id", "kind", "title", "fixture_directory", "expected_skills",
                "execution_status", "prompt", "expected_result_shape",
                "required_rubric", "filesystem_rule"}
    rubric_ids = set()
    for case in cases:
        if required - case.keys():
            raise ValueError(f"Missing fields in {case['id']}: {required - case.keys()}")
        expected_kind = "positive" if case["id"].startswith("P") else "negative"
        if case["kind"] != expected_kind or case["execution_status"] != "not_run":
            raise ValueError(f"Unexpected kind or claimed execution in {case['id']}")
        if not case["prompt"].strip() or not case["required_rubric"] or not case["expected_result_shape"]:
            raise ValueError(f"Incomplete case: {case['id']}")
        for item in case["required_rubric"]:
            if item["id"] in rubric_ids or not item["check"].strip():
                raise ValueError(f"Invalid rubric item: {item['id']}")
            rubric_ids.add(item["id"])
        expected_files(case)

    # Independently check the published arithmetic oracle using exact rationals.
    record = json.loads((SUBMISSION / "tests/fixtures/p04/observations.json").read_text())
    rows = record["runs"]
    rates = [Fraction(row["completed_operations"], row["elapsed_seconds"]) for row in rows]
    payloads = [Fraction(row["p0_sent_bytes"] + row["p1_sent_bytes"], row["completed_operations"]) for row in rows]
    pooled = Fraction(sum(row["completed_operations"] for row in rows), sum(row["elapsed_seconds"] for row in rows))
    if (rates, sum(rates) / 3, median(rates), pooled, payloads, sum(payloads) / 3) != (
        [1000, 500, 250], Fraction(1750, 3), 500, Fraction(3000, 7), [30, 36, 42], 36
    ):
        raise ValueError("P04 expected arithmetic no longer matches fixture")
    synthetic = json.loads((SUBMISSION / "tests/fixtures/p05/observation.json").read_text())
    if Fraction(synthetic["completed_operations"]) / Fraction(synthetic["elapsed_seconds"]) != 50000:
        raise ValueError("P05 expected arithmetic no longer matches fixture")

    # Finite consistency check of the toy counterexample; the rubric contains the
    # symbolic all-n argument and is not replaced by this bounded check.
    for n in (1, 2, 3):
        for key in range(1 << n):
            for challenge_bit in (0, 1):
                c1, c2 = key, key ^ challenge_bit
                guess = int((c1 ^ c2) != 0)
                if guess != challenge_bit:
                    raise ValueError("P01 finite counterexample check failed")
    return cases


def select(cases, case_id):
    for case in cases:
        if case["id"] == case_id:
            return case
    raise ValueError(f"Unknown case: {case_id}")


def prepare(case):
    root = Path(tempfile.mkdtemp(prefix=f"crypto-plugin-review-{case['id']}-"))
    workspace = root / "workspace"
    workspace.mkdir()
    source = fixture_path(case)
    if source is not None:
        shutil.copytree(source, workspace, dirs_exist_ok=True)
    snapshot = root / "initial-state.json"
    record = {
        "case_id": case["id"],
        "workspace": str(workspace),
        "case_file_sha256": hashlib.sha256(CASE_FILE.read_bytes()).hexdigest(),
        "initial_sha256": hashes(file_bytes(workspace)),
        "allowed_final_sha256": hashes(expected_files(case)),
    }
    snapshot.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"case_id": case["id"], "workspace": str(workspace),
                      "snapshot": str(snapshot), "prompt": case["prompt"],
                      "behavioral_execution": "NOT RUN"}, indent=2))


def check(case, workspace, snapshot):
    record = json.loads(snapshot.read_text(encoding="utf-8"))
    if record["case_id"] != case["id"] or Path(record["workspace"]).resolve() != workspace.resolve():
        raise ValueError("Snapshot does not belong to this case/workspace")
    if record["case_file_sha256"] != hashlib.sha256(CASE_FILE.read_bytes()).hexdigest():
        raise ValueError("Case definitions changed since preparation; stage a fresh case")
    if not workspace.is_dir():
        raise ValueError("Workspace is missing")
    observed = hashes(file_bytes(workspace))
    expected = record["allowed_final_sha256"]
    added = sorted(observed.keys() - expected.keys())
    removed = sorted(expected.keys() - observed.keys())
    changed = sorted(name for name in observed.keys() & expected.keys() if observed[name] != expected[name])
    passed = not (added or removed or changed)
    print(json.dumps({"case_id": case["id"], "filesystem_check": "PASS" if passed else "FAIL",
                      "added": added, "removed": removed, "unexpected_content": changed,
                      "behavioral_grade": "NOT ASSESSED: review response and tool trace manually"}, indent=2))
    return 0 if passed else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    sub.add_parser("validate")
    stage = sub.add_parser("prepare")
    stage.add_argument("case_id")
    compare = sub.add_parser("check")
    compare.add_argument("case_id")
    compare.add_argument("workspace", type=Path)
    compare.add_argument("snapshot", type=Path)
    args = parser.parse_args()
    cases = validate()
    if args.action == "validate":
        print("PASS: 5 positive + 3 negative case definitions, fixture paths, and arithmetic oracles")
        print("Behavioral test execution: NOT RUN; this is review-material validation only")
        return 0
    case = select(cases, args.case_id)
    if args.action == "prepare":
        prepare(case)
        return 0
    return check(case, args.workspace, args.snapshot)


if __name__ == "__main__":
    raise SystemExit(main())
