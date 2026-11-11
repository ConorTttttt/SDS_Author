# EU SDS Authoring Skill for Gemini — v4.0 (Full REACH / clause-grounded)

## Purpose
A **drafting and decision-support skill**, not a certified regulatory engine. It combines:
1. **Actual REACH legal text** supplied as a 603-page consolidated snapshot marked 22 June 2026 (Articles 31–36 and Annex II Parts A/B).
2. ECHA *Guidance on the Compilation of Safety Data Sheets* v4.0 (December 2020) for interpretive authoring workflows.
3. ECHA Forum **REF-11** SDS enforcement report (December 2024) for quality failure modes.
4. **Your own separately attached, pre-approved SDS phrase notebook** for reusable wording, never fabricated by the skill.

It aims to recommend suitable approved phrases, compile working SDS sections, audit existing SDSs and help determine whether multiple products may share one SDS. All release decisions require an adequately trained competent person. No actual product, phrase, CLP current data or country-specific OEL is prevalidated by this package.

## What changed since v3

- Added full user-supplied **REACH Regulation consolidated snapshot** (date/version explicitly tagged; *not* an authentic Official Journal edition or claim of currentness after the snapshot).
- Added **Article 31 / Article 32 decision routing**: hazardous/SVHC/PBT triggers, conditional SDS-on-request thresholds, public supply exception, language, delivery, update, exposure scenarios and Article 32 information.
- Added direct **Annex II clause-level authoring**, with PDF page references from Parts A and B. Preserved v3 ECHA guidance and REF-11, but put binding legal clauses ahead of those nonbinding documents for obligations.
- Added **classified vs unclassified Section 3** ingredient-reporting engine with §3.2.1 eight-way lowest-comparator logic, independent Union OEL and 0.1% status clauses; §3.2.2 six special branches; Section 3 fields, controlled ranges and interpretation of withheld identity.
- Added **multi-product SDS coverage** based on Annex II §1.1: each individual product must be fully addressed; common classification does not suffice. This can support a later Google Sheets/App Script grouping system.
- Added **46 machine-readable legal rule locators**, not an executable compliance engine, and **48 additional adversarial test specifications**. Existing 36 + 44 = 80 test specifications are preserved, making **128** in total. These have **not** been executed in Gemini on your actual phrase bank.

## ZIP structure

```text
SKILL.md
README.md
references/
  ANNEX_II_STRUCTURE_AND_GATES.md
  ECHA_SECTION_PLAYBOOK.md
  PHRASE_NOTEBOOK_SPEC.md
  PRODUCT_BRIEF.md
  REGULATORY_SOURCE_REGISTER.md
  TEST_CASES.md
  REF11_ENFORCEMENT_QA.md
  REF11_AUDIT_WORKFLOW.md
  REF11_TEST_CASES.md
  REACH_ARTICLES_DECISION_ENGINE.md
  REACH_ANNEX_II_CLAUSE_PLAYBOOK.md
  REACH_SECTION3_DISCLOSURE_ENGINE.md
  REACH_MULTI_PRODUCT_SDS_COVERAGE.md
  REACH_REGULATORY_DECISIONS.md
  REACH_RULE_INDEX.jsonl
  REACH_TEST_CASES.md
sources/
  ECHA_Guidance_on_Compilation_of_SDS_v4_Dec2020.pdf
  ECHA_REF11_SDS_Enforcement_Report_Dec2024.pdf
  REACH_1907_2006_consolidated_EN_2026-06-22.pdf
```

## Attach to Gemini

1. Upload v4 as a replacement for v3 in the available Gemini Skill interface, keeping the `SKILL.md` root and references intact.
2. Attach your separately controlled **approved phrase notebook**; do not use the source PDFs as approved phrase datasets.
3. Confirm that Gemini can read **exact phrase IDs and wording** and retrieve a requested REACH subsection/page from the attached PDF. Large PDFs and notebook retrieval are not guaranteed exhaustive. The compact markdown decision files are the primary retrieval aids; verify exact clauses in the PDF before using them for a legal conclusion.
4. Provide real composition, dated ingredient classifications, validated mixture CLP classification, physical properties, uses, Member State, supplier contacts and any relevant upstream exposure/OEL data.
5. Start with `ARTICLE31_CHECK` and `SECTION3_REVIEW` on one product; then try `RECOMMEND`, `DRAFT`, `AUDIT`, `REF11_PRECHECK`, or `MULTI_PRODUCT_COVERAGE`.

## Recommended first test prompt — classification vs disclosure

> ARTICLE31_CHECK and SECTION3_REVIEW this nonclassified EU mixture: [ingredient composition and statuses]. Use the included REACH consolidated 22 June 2026 snapshot as legal source, cite Article 31(3) and Annex II §3.2.2 as **separate tests**, determine each ingredient's disclosure status separately from its CLP mixture-classification contribution, and identify every missing CLP/SCL/OEL/status input. Do not guess thresholds or approved phrases.

## Recommended second test prompt — phrase adequacy

> RECOMMEND Sections 7 and 8 approved phrases from my attached [notebook/version] for [product/use/country]. Provide exact text and real approved phrase IDs. For each, map applicable Annex II §7/8 requirements to product-specific evidence and explain which additional fields are needed. Flag an approved glove phrase as incomplete if it lacks verified material, thickness or breakthrough-time detail where appropriate. Use Annex II p.131–133 and ECHA REF-11 as separate legal and inspection sources.

## Recommended third test prompt — grouping

> MULTI_PRODUCT_COVERAGE: compare these four formulation variants for a possible shared EU SDS. Apply Annex II §1.1 (p.119), then test each variant against Sections 1–16, particularly component disclosure, PPE, pH/flash point, transport and countries. Return a product-by-subsection coverage matrix, issues that a common SDS would need to differentiate, recommended candidate grouping(s), and unresolved legal/data gaps. Identical CLP classification alone is not sufficient.

## Safety and accuracy limitations

- Consolidated REACH text is provided for **reference**; authentic Official Journal law and applicable subsequent amendments must be checked where a legal determination is necessary. Reference snapshot is **22 June 2026**; a 2026 issue date does not alone prove the text stayed unchanged afterward.
- REACH Annex II is **not** the current full CLP Annex I classification engine, CLP Annex IV official P-text database, CLP Annex VIII UFI/PCN rules, or national OEL database. Date-specific checks and validated facts are still needed.
- SDS supply/revision duties (e.g. issuing free of charge by first supply; providing updates to prior 12-month recipients) concern **external processes** and cannot be certified by inspection of a document alone.
- The skill does not manufacture hazardous chemical data, regulatory statuses, approved phrase IDs or unverified exact legal citations.
- The machine-readable index records verified page locators and explanatory summaries, **not a proved exhaustive legal rule extraction or automated legal compliance calculator**.

## Testing status

The package can be statically validated for file integrity, expected references and JSONL format. Regulatory outputs and exact approved phrase retrieval have **not** been evaluated in a connected Gemini runtime and must be assessed by a competent SDS author.
