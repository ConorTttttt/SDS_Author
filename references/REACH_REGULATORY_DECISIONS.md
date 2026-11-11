# Clause-first decisions, evidence provenance and outputs

The purpose of this module is to prevent an LLM from producing plausible but legally under-specified SDS content. Apply in every authoring mode and retain reasoning **outside the printable SDS**.

## Rule evaluation pipeline

`REGULATORY_SCOPE → EVIDENCE_INVENTORY → CLAUSE_APPLICABILITY → REQUIRED_CONTENT → FACT_VERIFICATION → APPROVED_PHRASE_RETRIEVAL → COMPLETENESS_CHECK → CROSS_SECTION_VALIDATION → HUMAN_REVIEW`

**Do not invert the pipeline** by choosing an attractive stock phrase and retrofitting reasons to it. Read `REACH_ARTICLES_DECISION_ENGINE.md`, `REACH_ANNEX_II_CLAUSE_PLAYBOOK.md`, and `REACH_SECTION3_DISCLOSURE_ENGINE.md` when relevant.

## Evidence hierarchy

1. Applicable **binding** REACH/CLP/national law, verified for actual issue/market/transition date, controls legal rules. The supplied PDF is the **22 June 2026 snapshot**, not proof there have been no subsequent changes; check OJ/ELI when necessary for issue.
2. Validated product-specific **factual evidence** controls physical/chemical/health/safe-use truth. A supplier SDS may be an input, but does not alone prove the formulated mixture has identical properties or classification.
3. ECHA **guidance** explains interpretive approaches (non-binding). ECHA **REF-11** identifies common audit defects (non-binding, retrospective).
4. Only the user's designated **approved phrase notebook** controls selection of discretionary reusable wording; not a regulator, not a factual source. The user controls phrase approvals.

## Classification of regulatory conclusions

- `LEGAL_REQUIREMENT_VERIFIED`: exact valid law and clause plus applicability evidence.
- `LEGAL_REQUIREMENT_CONDITIONAL`: law established but material fact/date/status unknown.
- `GUIDANCE_RECOMMENDATION`: interpretive recommended approach, not legislated independently.
- `REF11_ENFORCEMENT_FLAG`: evidence of a defect pattern, requires legal/factual confirmation.
- `INTERNAL_AUTHORING_CONVENTION`: style/workflow, not law.
- `NOT_APPLICABLE_WITH_EVIDENCE`: substantiated specific exclusion; never universal based on absence of data.
- `LEGAL_SOURCE_VERSION_UNVERIFIED`: new law, national rule, CLP rule or OJ authenticity not checked.

## Authoring decision record per subsection and requirement

```yaml
regulatory_snapshot:
  file: REACH_1907_2006_consolidated_EN_2026-06-22.pdf
  labelled_consolidation: '22 June 2026 / 069.001'
  checked_at: YYYY-MM-DD
  legal_authenticity_checked: false
product:
  name: '[actual]'
  formula_revision: '[actual]'
  substance_or_mixture: '[actual]'
  first_placed_on_market: '[actual/unknown]'
  sds_revision: '[actual/unknown]'
  eu_member_state: '[actual]'
requirement:
  ref: 'REACH Annex II §8.2.2.2(b)(i)'
  pdf_page: 132
  condition: 'glove protection needed for specific use/exposure'
  applicability: 'APPLIES | DOES_NOT_APPLY | REQUIRES_EVIDENCE'
  evidence: ['product SDS / documented glove compatibility / exposure estimate']
  missing_evidence: ['breakthrough time not validated']
  required_content: ['material', 'thickness', 'breakthrough']
phrase:
  notebook: '[actual controlled notebook]'
  approved_id: '[actual retrieved ID or absent]'
  approval_version: '[actual]'
  exact_text_verified: false
  sufficient_to_meet_requirement: false
result:
  status: 'READY_FOR_REVIEW | EVIDENCE_GAP | PHRASE_GAP | SOURCE_GAP | CONTRADICTION'
  printed_sds_text: '[only supported values/actual approved wording]'
  author_only_explanation: '[why, law, source, exclusions, counterevidence]'
```

## Release gates

- **Block any 'publication-ready' or 'compliant' claims** if required product classification, key Sections 1/2/3/8/9 evidence, relevant legal sources, exact approved text, target language, exposure scenarios or competent-person signoff are missing.
- For an exploratory `RECOMMEND` response it is acceptable to identify plausible candidates marked `CONDITIONAL` but **not to label them approved/selected when not fully retrievable**.
- A clause can be satisfied by a verified numerical field rather than a stock sentence; no requirement for an approved phrase for every data point.
- `REGULATORY_REQUIREMENT_NOT_MET`, `LEGAL_RISK_UNCONFIRMED`, `EXTRA_SAFETY_INFORMATION_SUGGESTED`, and `PHRASE_GAP` must be kept distinct.
- Never print placeholder or reviewer flags in a final SDS delivered for issue.

## Mode-specific outputs

**RECOMMEND:** subsection/requirement → exact clause/page → condition → available evidence → retrieved candidate phrase ID+exact text → suitability, exclusions and data gaps → alternatives rejected. Separate compulsory legal content not contained by the approved phrases.

**DRAFT:** 16-section working SDS with required Part B subsections, plus author-only clause map/phrase IDs/unresolved blockers. No false certification.

**AUDIT / REF11_PRECHECK:** primary finding rows use `ID | legal clause | law snapshot / p | actual document evidence | completeness status | plausibility status | verification status | proposed correction | urgency`.

**ARTICLE31_CHECK:** output Article 31(1)/(3)/(4), Article 32 and supply/ES statuses from `REACH_ARTICLES_DECISION_ENGINE.md` before attempting drafting.

**SECTION3_REVIEW:** per ingredient `contribution-to-classification` and `requirement-to-disclose` as separate conclusions, showing each threshold and legal source used.

**MULTI_PRODUCT_COVERAGE:** product × Annex II-subsection coverage matrix and gaps. Not a 'same formulation' chemical equivalence assumption.
