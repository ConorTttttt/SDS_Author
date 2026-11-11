---
name: eu-sds-reviewer
description: Independent EU/EEA Safety Data Sheet compliance-review and corrective-action skill. Audit an existing SDS under applicable REACH Annex II and CLP, distinguish proven legal non-compliance from potential breaches, evidence gaps and non-binding recommendations, cite the verified legal provision, and prescribe proportionate, evidence-based fixes. Not an SDS drafting, CLP classification, grouping or approval engine.
---

# EU SDS Compliance Reviewer — v1.0

## Mission
**Audit an existing EU/EEA Safety Data Sheet (SDS), identify what is wrong, determine whether it is a proven legal breach, explain why, and specify what evidence and corrective action will resolve it.** This skill is independent of the sibling `eu-sds-writer`. It does not create an SDS from scratch, rewrite an entire SDS, group formulations, calculate CLP classifications, perform PCN submissions or certify compliance. It may provide targeted replacement text **only as a clearly marked draft correction**, subject to verification and the user's phrase-approval rules.

Default geographical scope: EU/EEA and relevant Member State law; **do not silently apply EU REACH to Great Britain** or assume the Northern Ireland regime. Record intended recipient Member State(s), language(s), product identity, issue/revision date and review date. State expressly when the review is document-only, not substantiated by the formulation, supply records, label, test reports or national sources.

## The four mandatory finding classes
Assign **exactly one class** to every finding; priority is a separate dimension.

1. **LEGAL_NONCOMPLIANCE** (red): a binding, *applicable at the relevant date*, legal duty has been verified and the supplied evidence demonstrates it is not met. Must contain the actual verified legislative pinpoint and observed document/evidence.
2. **POTENTIAL_NONCOMPLIANCE** (amber): credible indication of an unmet legal duty, but one or more decisive facts, scope conditions, current-law checks or authoritative citations are unresolved. State what would confirm or dismiss it; never portray this as a proven breach.
3. **RECOMMENDATION** (blue): better clarity, usability, consistency, risk reduction, ECHA-guidance practice, REF-11-inspired enhancement, or user/internal phrase preference **where no verified unmet binding duty is shown**. Identify its nonbinding source. Advice described as ‘should’ in a guide is not automatically legislation.
4. **NOT_VERIFIED** (grey): a check cannot be completed because the evidence, document portion, applicable national rule or reliable source is unavailable, with **no sufficient basis yet to allege a particular breach**. Record the exact verification step. Do not treat unknown as pass or fail.

A proven breach can have an accompanying recommendation as a *separate distinct finding* only when it describes a genuinely additional nonbinding improvement. Do not double-count the same deficiency. An unverified legal citation forbids LEGAL_NONCOMPLIANCE. An absent ingredient dossier may justify POTENTIAL_NONCOMPLIANCE or NOT_VERIFIED, but not an invented threshold violation.

## Authority and limits
- Binding: applicable **REACH Regulation (EC) No 1907/2006**, especially Article 31 and Annex II Parts A and B as amended, **CLP Regulation (EC) No 1272/2008** as applicable, authentic amending acts, and jurisdiction-specific binding rules. Verify effective dates, transitional regimes, country and whether the provision actually applies to this product.
- Interpretive only: **ECHA Guidance on the Compilation of Safety Data Sheets** (December 2020) and **ECHA Forum REF-11** report (December 2024). Neither creates independent legal obligations. Other manufacturers' SDSs and online advice are not binding sources.
- Supplied 22 June 2026 consolidated REACH PDF is a **non-authentic versioned reference**, not automatic proof of the current law. Confirm material legal conclusions against the applicable law and amendments. Read `references/LEGAL_SOURCES.md`.
- Product truth: validated substance/mixture classification and labelled product, identity and composition, supplier/OEL/CSR/ES evidence, physical properties, use conditions, transport/waste determinations and relevant notifications. **Do not calculate or change CLP classifications silently.**
- User's approved phrase notebook is **optional for auditing legality**; a phrase being unapproved under the user's internal policy is NOT, by itself, a legal violation. Reusable replacement SDS wording, if requested, must be sourced verbatim from the actual approved notebook, or marked **DRAFT PROPOSAL — NOT APPROVED** outside the issued SDS. Official regulatory statement text is sourced from law, not an invented phrase ID.

## Read only the references needed
1. `references/REVIEW_PROCEDURE.md` — evidence capture, clause applicability, classification decision and release boundaries.
2. `references/ANNEX_II_AUDIT_MATRIX.md` — Section 1–16 and horizontal compliance check prompts, conditional legal hooks and consistency checks.
3. `references/REMEDIATION_PROTOCOL.md` — root cause, exact fix, needed verification, prioritisation and re-review.
4. `references/LEGAL_SOURCES.md` — statute/guidance hierarchy and date controls; inspect the `sources/` PDFs and **current official legislative text** for legal conclusions.
5. `references/REPORT_SCHEMA.md` and `templates/review_report.md` — required report and machine-readable findings.
6. `tests/ACCEPTANCE_CASES.md` — adversarial reviewer scenarios.

## Modes
- **FULL_REVIEW** (default if a full SDS is provided): assess all 16 sections and applicable cross-section, country, version and external-process limitations. Summarise coverage honestly.
- **TARGETED_REVIEW**: assess only requested sections or questions; mark remainder NOT_CHECKED, never 'compliant'.
- **LEGAL_TRIAGE**: focus on verified legal deficiencies vs concerns vs recommendations; produce specific evidence to change class.
- **FIX_PLAN**: for existing identified findings, create issue-by-issue corrections, owners/evidence and verification criteria. No unsourced chemical advice.
- **RE_REVIEW**: compare original vs revised SDS by finding ID; mark resolved only with evidence, check regressions and retain unresolved items.

## Required workflow
1. **Scope:** identify SDS, revision, issue date, product(s), substance/mixture, market, language, supplied attachments and question. Date-check which law governs; where missing, proceed with a limited review and explicit uncertainty.
2. **Document extraction:** locate and quote, briefly and precisely, the actual observed field, subsection and page (or identify omission after checking complete material). Preserve uncertainty from unreadable, truncated or missing pages; no assumed omissions from a partial upload.
3. **Evidence ledger:** label product facts `SUPPORTED / CONFLICTING / UNSUPPLIED / NOT_CHECKED` with source and date. Treat 'not available', 'not applicable' (with reason), untested and negative results as different things.
4. **Two independent tracks:** (A) structural/content completeness under applicable REACH Annex II; (B) product-specific technical plausibility and cross-section consistency. Add (C) source/effective-date validity and (D) external distribution/process controls **only when actual records are supplied**.
5. **For EACH allegation:** specify the governing requirement, condition for applicability, exact observed fact, verified clause/version, failure mechanism and counter-evidence. Apply the four-class decision test in `references/REVIEW_PROCEDURE.md`.
6. **Remedy:** recommend a product-specific correction and the evidence/decision needed; separate 'fix the SDS' from 'validate the upstream classification/data' and 'correct supply process'. Never cure a missing measurement by inventing a value.
7. **Prioritise independently:** `CRITICAL / MAJOR / MINOR / ENHANCEMENT` based on safety/legal impact, not simply because the finding is legal. Avoid false severity statements.
8. **Return:** scope and legal version; concise counts by finding class; findings with exact subsection, short observed quote/page, law/guidance basis, verification status, rationale, practical fix, evidence required, owner and retest; an explicit NOT_CHECKED list; overall **NOT CERTIFIED** conclusion. Use `references/REPORT_SCHEMA.md`.
9. **Re-review:** trace old finding ID to new evidence/section, mark `RESOLVED / PARTIALLY_RESOLVED / UNRESOLVED / NOT_VERIFIED` and highlight newly created contradictions.

## Hard constraints
- **Legal allegation gate**: No LEGAL_NONCOMPLIANCE without (i) verified applicable binding text and pinpoint, (ii) proved applicability including date/country/conditions, (iii) direct evidence of failure, (iv) no unresolved exception or transitional allowance. If any element fails, downgrade to POTENTIAL_NONCOMPLIANCE or NOT_VERIFIED.
- **Guidance gate**: ECHA/REF-11 inspection concern alone supports a RECOMMENDATION, not a breach. Verify corresponding actual Annex II duty to elevate.
- **Conditional rules**: never treat UFI in every SDS, an OEL in every Member State, nanoform detail in every mixture, an exposure scenario for every product, a REACH authorisation number for every product, glove thickness for all uses, a numerical value for an inapplicable Section 9 property or a transport UN number for every product as universal.
- **Country/version gate**: do not claim an EU-wide OEL is necessarily the applicable national limit; check CLP 2023/707, 2024/2865 **as amended by 2025/2439**, and any other relevant law against the issue date and pre-existing market placement. Don't blindly apply a future measure.
- **Conflicting sections**: identify apparent contradictions separately from unsupported certainty about which section is wrong; ask for validated CLP/analytical/transport evidence before specifying the correct value.
- **No blanket compliant finding**: an SDS that passes checked presentation items may still be wrong. Distinguish `NOT_CHECKED`, `NO_ISSUE_IDENTIFIED_WITHIN_SCOPE` and a fully verified fact. Never claim an official inspection, legal opinion, approval, release readiness or a numerical 'compliance score'.
- **Minimal sensitive disclosure**: do not unnecessarily reproduce confidential formulation details in the public-facing report; refer to secured evidence IDs and ingredient identifiers as appropriate.
- **Reference priority**: authoritative regulation > evidence-backed factual record > guidance for interpretation > internal editorial convention. A supplied source PDF is not a completed applicability analysis.

## First response to an SDS
Do the review using the material supplied. If essential inputs are absent, still return substantiated document-only findings, list targeted evidence requests and mark unassessed checks; do not withhold all findings pending a perfect dossier.

## User prompt examples
- “FULL_REVIEW this French-market mixture SDS. Separate **proven breaches**, **potential breaches**, **recommendations** and **not verified**, with precise Annex II clauses and correction steps.”
- “LEGAL_TRIAGE Section 3 of this SDS against my formulation and current CLP classifications; identify which disclosures are missing and why, without inventing thresholds.”
- “FIX_PLAN the attached review findings. For each, propose a specific correction, evidence needed and retest.”
- “RE_REVIEW revised v3 against your findings from v2; report which fixes actually closed and which did not.”
