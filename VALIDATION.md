# Validation protocol for v4 (not regulatory signoff)

## Static package validation

Check `SKILL.md` root, all markdown modules, three PDFs, JSONL validity and file references. See `tests/check_package.py`. This is a **file-level** test, not proof that Gemini understands or obeys legal rules.

## Functional regulatory evaluations (not yet run)

Use `references/REACH_TEST_CASES.md` (48), `references/REF11_TEST_CASES.md` (44), and `references/TEST_CASES.md` (36). Run each in Gemini with the actual approved phrase library and supporting product evidence; record prompts, source version, expected vs observed decisions, source citations, false positives/negatives, phrase ID accuracy and reviewer adjudication. Do not count a prompt as passed if the correct decision is based on a fabricated phrase or incorrect legal citation.

## Suggested acceptance gates before production use

- 100% of any **selected** stock phrase IDs must resolve to exactly approved wording and applicability conditions in the connected notebook.
- No numerical property, OEL, SCL/ATE/M-factor, authorization status, CLP classification or transport number may be fabricated.
- Every Section 3 test must record separate **classification contribution** and **disclosure requirement**.
- Every trigger or nonconformity claim must show **pinpoint applicable legal text** and corresponding product evidence; missing law versions marked unverified.
- A multi-product SDS candidate is acceptable only with complete, attributable product-by-subsection coverage and explicit competent author approval.

These are design acceptance criteria, not assertions that the skill already meets them.
