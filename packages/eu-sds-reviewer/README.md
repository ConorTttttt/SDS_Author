# EU SDS Compliance Reviewer — standalone Gemini skill (v1.0)

A **separate skill** in the SDS_Author repository. It reviews *existing* EU/EEA Safety Data Sheets for legal non-compliance, potential non-compliance, evidence gaps and nonbinding recommendations, then provides targeted, verifiable corrections.

## What it does
- Reviews REACH Annex II Part B Sections 1–16 and relevant Article 31/CLP/country-specific obligations, including conditional requirements.
- Reports **LEGAL_NONCOMPLIANCE / POTENTIAL_NONCOMPLIANCE / RECOMMENDATION / NOT_VERIFIED** separately; severity and completeness are independent.
- Names the precise applicable legal clause for proven breaches, shows the actual observed SDS evidence and offers a practical fix.
- Keeps document-content observations distinct from unverified product facts and external supply/revision process obligations.
- Checks consequences of changed law and transitional rules; does not declare every historical SDS noncompliant by applying future rules.
- Includes a review report template, machine-readable finding schema, source PDFs and adversarial acceptance tests.

## Does not do
No fresh SDS authoring, grouping, classification calculation, UFI/PCN submission, transport determination, false compliance certification or invented replacement safety data. These tasks require separate validated inputs. Finding an unapproved internal phrase is an **internal-control recommendation**, unless the underlying content also violates verified law.

## Gemini deployment
1. Package **this directory only** as its own skill, with `SKILL.md` at the package root. Include all `references/`, `templates/`, `tests/` and `sources/`, preserving paths.
2. Activate the reviewer separately from the sibling `eu-sds-writer`; invoke it on an **existing** SDS PDF/text.
3. Supply country, language, target issue/review date, product identifier, revision and—where available—validated classification, formulation/status dossier, label, supplier SDSs, measured properties, OEL records, ES/CSR, national requirements, transport determinations and supply records. It can still perform a narrower **document-only review** if these are absent.
4. Require a current-law check from authoritative legislation before counting an issue as LEGAL_NONCOMPLIANCE. Source PDFs are versioned reference snapshots and ECHA material is nonbinding.
5. Review every output with a competent SDS professional. Uploading these files does not certify complete Gemini retrieval or legal validity.

## Prompts
**Full review:** “FULL_REVIEW my attached SDS for sale in [EU Member State], version [X], issue date [date]. Cite verified provisions for every proven legal breach, separately list potential breaches and recommendations, and tell me specifically how to fix each problem.”

**Section-only:** “TARGETED_REVIEW Sections 3 and 8 using this validated composition and OEL dossier. Treat missing ingredient details as a confirmed breach only after proving the applicable threshold and clause.”

**Fix and verify:** “FIX_PLAN finding IDs R-001–R-006; then RE_REVIEW my corrected document and say which have actually closed, citing new evidence.”

## Reference directory
- `references/LEGAL_SOURCES.md`: sources, authority, date applicability.
- `references/REVIEW_PROCEDURE.md`: evidence and class decision gates.
- `references/ANNEX_II_AUDIT_MATRIX.md`: structured checks for all 16 sections.
- `references/REMEDIATION_PROTOCOL.md`: actionable corrections and verification.
- `references/REPORT_SCHEMA.md`: report fields and examples.
- `templates/review_report.md`: human-readable output.
- `templates/finding_record.schema.json`: structured output validation contract.
- `tests/ACCEPTANCE_CASES.md`: sample adversarial audit cases.
- `sources/`: shared-content copies of the repository's dated REACH/ECHA/REF-11 PDFs. They are reference sources, not approval datasets.

**Regulatory currency:** assembled 11 November 2026; no assertion that an included consolidation remains current after its stated date. Product, Member-State, legal-version and transitional checks remain case-specific.
