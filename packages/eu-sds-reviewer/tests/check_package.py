#!/usr/bin/env python3
"""Static structural checks for the standalone EU SDS reviewer skill (not legal validation)."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md", "README.md", "GEM_INSTRUCTIONS.md",
    "references/LEGAL_SOURCES.md", "references/REVIEW_PROCEDURE.md",
    "references/ANNEX_II_AUDIT_MATRIX.md", "references/REMEDIATION_PROTOCOL.md",
    "references/REPORT_SCHEMA.md", "templates/review_report.md",
    "templates/finding_record.schema.json", "tests/ACCEPTANCE_CASES.md",
    "sources/REACH_1907_2006_consolidated_EN_2026-06-22.pdf",
    "sources/ECHA_Guidance_on_Compilation_of_SDS_v4_Dec2020.pdf",
    "sources/ECHA_REF11_SDS_Enforcement_Report_Dec2024.pdf",
]
missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
assert not missing, f"Missing required package files: {missing}"
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
assert skill.startswith("---\nname: eu-sds-reviewer\n"), "Invalid skill frontmatter"
assert "independent" in skill.lower()
classes = ("LEGAL_NONCOMPLIANCE", "POTENTIAL_NONCOMPLIANCE", "RECOMMENDATION", "NOT_VERIFIED")
for content_path in ("SKILL.md", "references/REVIEW_PROCEDURE.md", "references/REPORT_SCHEMA.md"):
    content = (ROOT / content_path).read_text(encoding="utf-8")
    for required_class in classes:
        assert required_class in content, f"{content_path}: absent {required_class}"
schema = json.loads((ROOT / "templates/finding_record.schema.json").read_text(encoding="utf-8"))
assert set(schema["properties"]["finding_class"]["enum"]) == set(classes)
assert {"finding_class", "legal_basis", "fix_action", "closure_test"}.issubset(schema["required"])
test_spec = (ROOT / "tests/ACCEPTANCE_CASES.md").read_text(encoding="utf-8")
assert sum(1 for line in test_spec.splitlines() if line.startswith("| T")) >= 20
for path in REQUIRED:
    if path.endswith(".pdf"):
        with (ROOT / path).open("rb") as f:
            assert f.read(5) == b"%PDF-", f"Bad PDF header: {path}"
print("PASS: reviewer package structural/schema invariants. No legal or Gemini validation performed.")
