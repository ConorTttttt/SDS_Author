# REF-11 audit workflow, finding register and author-facing report format

This is the operational companion to `REF11_ENFORCEMENT_QA.md`. REF-11 is an enforcement case-study source, **not** a substitute for verified law; do not claim that the skill's checks replicate an official ECHA inspection.

## Procedure

**1. Intake and scope.** Gather document version, intended issue date, EU/EEA markets/languages, product identity, supplier, composition report, CLP classification/label, physical-property tests, current OELs, PPE exposure controls, relevant regulatory status, transport evidence, ES/CSR and any distribution history. Do not confuse document-only review with a supply-chain systems audit.

**2. Split the review into independent tracks:**

- `DOCUMENT_COMPLETENESS`: actual subsection, required field and status (present/absent/inapplicable/not verified).
- `TECHNICAL_PLAUSIBILITY`: supported claims, mutually incompatible statements, internal consistency, product/use-context consistency.
- `LEGAL_APPLICABILITY`: separate check against date-specific binding REACH/CLP/national law and applicable transitional measures; not established by REF-11 alone.
- `DOCUMENT_CONTROL_AND_SUPPLY`: version, changes, language, exposure scenarios, active provision and recipient notifications; mark `NOT_CHECKED` without records.
- `PHRASE_CONTROL`: exact approved phrase ID/version and eligibility. Factual data and official required statement text have a different source protocol.

**3. Run high-frequency section checks first:** 8, 3, 9, 1, 2. This priority comes from REF-11's findings, not a claim those sections are uniquely important. Then check the rest of the document and cross-section links.

**4. For each item R11-01 through R11-28** record: `applicability_reason`, `status`, `confidence`, `observed`, `evidence`, `source_type`, `legal_rule_verified?`, `impact`, `remedy`, and `review_owner`. `NOT_APPLICABLE` requires explanation and some factual or legal basis. `NO EVIDENCE` is never silently converted to compliant.

**5. Check cross-section tripwires:**

- `classification` ⇄ `component data` ⇄ `toxicology/ecology` ⇄ `label`; identify discrepancies without silently recalculating.
- `PPE/ventilation` ⇄ `uses` ⇄ `OEL / exposure` ⇄ `physical properties`; don't give unconditional PPE answers without operational context.
- `nanoform` ⇄ `composition / particle properties` ⇄ `relevant safety advice`; note 1.1-mixture clarification.
- `ED properties` ⇄ `2.3 / 3.2 / 11.2 / 12.6`, as applicable and date-scoped.
- `REACH authorisation` ⇄ `2.2 label elements / 15.1 decision conditions` ⇄ `identified use / ES / safe use`.
- `country-specific information` ⇄ `1.4 emergency / 8.1 OEL / 15.1 national regulations / language`.
- `9.x physical hazards` ⇄ `5 fire / 7 storage / 10 stability / 14 transport`, with independent transport classification.

**6. Render findings in two deliverables:** a **short priority register** with sources and a **remediation plan** linked to the underlying current legal clauses where verified. Distinguish confirmed failure, likely concern, unknown and N/A. Do not produce unsupported overall percentage compliance. Optionally report `coverage = items assessed / items applicable or pending`, but never a regulatory certification score.

**7. Release gate:** identify what competent-person review and additional evidence are needed. Gemini must not sign off, approve, publish, replace an upstream dossier or claim legal conformity.

## Finding record schema (example fields, no case is assumed true)

```yaml
finding_id: 'RF-001'
ref11_check_id: 'R11-13'
subsection: '8.2'
track: 'TECHNICAL_PLAUSIBILITY'
status: 'NEEDS_EVIDENCE'
priority: 'MAJOR'
statement_observed: '[quote source document text; do not invent]'
concern: 'Glove selection detail or suitability evidence not supplied'
product_evidence: '[source ID or UNSUPPLIED]'
regulatory_basis:
  type: 'REF11_QA_PROMPT | VERIFIED_LEGAL_TEXT | GUIDANCE | INTERNAL_CONTROL'
  reference: 'REF-11 p. 19 Table 4; check current Annex II'
  verified_as_of: null
impact: 'Can not substantiate that suggested PPE is adequate'
recommended_action: 'Obtain a qualified glove choice/compatibility source or documented reason for inapplicability'
owner: 'SDS competent person'
```

## Required short report layout

**Audit scope:** `product | SDS revision | date | market(s) | language(s) | source files | approved phrase-library version | legal snapshot or not verified`.

**Summary:** only issues supported by evidence; coverage vs `NOT_CHECKED`; `BLOCKER/MAJOR/MINOR/REVIEW` counts with explicit denominator.

**Priority register:** `ID | check | subsection | track | finding | actual evidence | severity | verified law? | recommended action`.

**All checks:** statuses for R11-01..R11-28 including actual applicability and lack-of-source flags.

**Phrase-control exceptions:** `phrase ID | exact quotation source | approval verified? | application verified? | unmet content`.

**Document release dependencies:** facts, regulatory source verification, translation, reviewer actions and supply controls. The user-facing SDS draft and the author-only audit report must remain clearly separated.
