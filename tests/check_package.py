#!/usr/bin/env python3
"""Static integrity check only: NOT a legal correctness or Gemini functional test."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
files = [
 'SKILL.md','README.md','CHANGELOG_V4.md','VALIDATION.md',
 'references/ANNEX_II_STRUCTURE_AND_GATES.md','references/ECHA_SECTION_PLAYBOOK.md',
 'references/PHRASE_NOTEBOOK_SPEC.md','references/PRODUCT_BRIEF.md',
 'references/REGULATORY_SOURCE_REGISTER.md','references/TEST_CASES.md',
 'references/REF11_ENFORCEMENT_QA.md','references/REF11_AUDIT_WORKFLOW.md',
 'references/REF11_TEST_CASES.md','references/REACH_ARTICLES_DECISION_ENGINE.md',
 'references/REACH_ANNEX_II_CLAUSE_PLAYBOOK.md','references/REACH_SECTION3_DISCLOSURE_ENGINE.md',
 'references/REACH_MULTI_PRODUCT_SDS_COVERAGE.md','references/REACH_REGULATORY_DECISIONS.md',
 'references/REACH_RULE_INDEX.jsonl','references/REACH_TEST_CASES.md',
 'sources/ECHA_Guidance_on_Compilation_of_SDS_v4_Dec2020.pdf',
 'sources/ECHA_REF11_SDS_Enforcement_Report_Dec2024.pdf',
 'sources/REACH_1907_2006_consolidated_EN_2026-06-22.pdf'
]
missing = [p for p in files if not (root/p).is_file()]
assert not missing, f'Missing: {missing}'
s = (root/'SKILL.md').read_text()
for text in ['version: 4.0.0','ARTICLE31_CHECK','SECTION3_REVIEW','MULTI_PRODUCT_COVERAGE','REACH_ARTICLES_DECISION_ENGINE.md','REACH_SECTION3_DISCLOSURE_ENGINE.md']:
 assert text in s, text
rules = [json.loads(line) for line in (root/'references/REACH_RULE_INDEX.jsonl').read_text().splitlines() if line.strip()]
assert len(rules) == 46, len(rules)
assert len({r['id'] for r in rules}) == len(rules)
for r in rules:
 assert r['source_file'] in files
 assert r['pdf_pages'] and all(isinstance(page,int) and 1 <= page <= 603 for page in r['pdf_pages'])
tests=(root/'references/REACH_TEST_CASES.md').read_text()
import re
ids=re.findall(r'^\| ([ASQG]\d{2}) \|', tests, flags=re.M)
assert len(ids)==48, (len(ids),ids)
assert len(set(ids))==len(ids)
print(f'PASS static only: {len(files)} expected content files, {len(rules)} legal index locators, {len(ids)} new scenarios; original 80 specs remain.')
