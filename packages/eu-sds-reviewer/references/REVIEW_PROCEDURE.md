# Evidence-led review workflow and finding decision logic

## A. Scope first
Record: review ID; SDS filename and page count; source language; substance/mixture; product identifier; supplier; date/version on SDS; intended supply date (if different); reviewer date; target EU/EEA Member State(s) and country-specific source status; types of attachments; requested section scope; complete-file integrity; known regulatory sources.

If given only portions of an SDS, mark sections outside those portions **NOT_CHECKED**. If no known issue date, record the uncertainty and assess visible content under clearly identified hypothetical/default law only; **do not quietly presume present-day law controls historical obligations**.

## B. Two primary independent assessment tracks
1. **DOCUMENT_COMPLETENESS:** Are mandatory Part B headings and applicable fields present, in the correct subsections, with permitted and explained statuses? Legal question: did an applicable binding obligation require this content?
2. **TECHNICAL_PLAUSIBILITY:** Does the document make scientifically supportable, context-specific statements consistent with the verified classification, product data, intended uses, other sections, supplier records and exposure scenarios?

Additional distinct tracks:
3. **LEGAL_VERSION_AND_JURISDICTION:** current law, instrument/paragraph, effective dates/transitions, Member State language, national exposure limits, local restrictions.
4. **SUPPLY_AND_REVISION_PROCESS:** proof of issue and updates, delivery to recipients, obligations outside document text; NOT_CHECKED without records.
5. **INTERNAL_WORDING_CONTROL:** approved phrase version and template preference. Internal shortcomings are not legal conclusions without independent law.

No inferred substantive SDS correctness from the presence of all headings.

## C. Evaluate every candidate against six gates

**G1 — Observed evidence:** exact SDS page/subsection, a short quote or genuinely missing field from a **complete, readable** document. A bad quote or imagined absence fails the gate.

**G2 — Applicability:** substance or mixture, relevant composition/status, use/format, market/language, country, hazard/data condition and regulatory exception. Confirm applicability, don't assert universality.

**G3 — Time/version:** legal wording, material amendment and effective date, including placement-on-market transitions, appropriate to the issue/review purpose.

**G4 — Normative force:** provision from binding applicable law vs ECHA guidance vs REF-11 vs user preference. **Do not infer a mandatory duty from a nonbinding recommendation.**

**G5 — Contravention:** observable mismatch between binding duty and evidence. Distinguish a missing SDS field, missing support to assess truth, and an external process for which no audit record was provided.

**G6 — Alternative explanations:** exceptions, justified N/A, permitted ranges, approved alternative name, annexed ES, other section cross-reference, existing official statement, truncated document or unstated intended market.

### Single-class decision
- G1–G6 fully supported and G4 binding + actual contravention → **LEGAL_NONCOMPLIANCE**.
- A specific plausible legal requirement/failure exists, but required applicability, version, fact or contravention proof remains open → **POTENTIAL_NONCOMPLIANCE**; specify the missing decisive fact.
- Improvement warranted from guidance, readability, REF-11, template or internal control with no established unmet binding duty → **RECOMMENDATION**; source as nonbinding.
- Cannot make a supported observation or decide whether any breach is even plausible due to missing/out-of-scope evidence → **NOT_VERIFIED**; state the check needed.
- Where **no issue** is observed in an actually completed check, record **NO_ISSUE_IDENTIFIED_WITHIN_SCOPE** in the coverage ledger only, not a false 'finding' or global compliance assertion.

**Severity ≠ legal class.** Assign CRITICAL (direct serious safety/release impact), MAJOR (material compliance/information impact), MINOR (limited impact) or ENHANCEMENT (nonbinding improvement). A cosmetic statutory omission may be MINOR; an apparent but unproven serious danger can be POTENTIAL_NONCOMPLIANCE / CRITICAL.

## D. Evidence ledger
For each fact record:
- `evidence_id`; material/file; page/section; substance/mixture scope; exact value or short quote; date/version; source owner; units/conditions; confidence `VERIFIED / SUPPORTED / CONFLICTING / UNSUPPLIED / NOT_CHECKED`.
- Source conflicts must be shown rather than one chosen secretly. Clearly distinguish `not available`, `not determined`, `not applicable with basis`, tested-negative and `not hazardous`.
- Cite primary document pages, not only search snippets. An attached upstream SDS is supporting factual input, not proof of the reviewed mixture's classification or its exact regulatory validity.

## E. Document audit order
1. Completeness and version metadata: first page, 16 headings, Part B subsections, page numbers, language and non-blank fields.
2. Highest-risk substantive checks: **Sections 1, 2, 3, 8, 9**. Use relevant ingredient and national evidence.
3. Continue with Sections 4–7, 10–16 using `ANNEX_II_AUDIT_MATRIX.md`, without overlooking special/new CLP hazard classes.
4. Cross-section links:
   - 1 identity/use ↔ 2 label ↔ 3 ingredients ↔ 8 exposure ↔ 11/12 hazard.
   - 2 skin/eye risk ↔ 4 first aid ↔ 7 handling ↔ 8 PPE.
   - 5 fire ↔ 7 storage ↔ 9 flash/physical properties ↔ 10 reactions ↔ independent 14 transport assessment.
   - 6 release ↔ 12 ecology ↔ 13 disposal.
   - 2/3 hazard ↔ 15 legal status ↔ 16 H-text/method/version.
   - country language ↔ 1 emergency ↔ 8.1 OEL ↔ 15 national rules.
5. Identify duplicated/conflicting facts and specify what external validation decides the correct answer. Do not calculate new mixture classifications in conversation.

## F. Determining Section 3 omissions
- First establish whether 3.1 (substance) or 3.2 (mixture) applies.
- Under Annex II 3.2, **classified and nonclassified mixtures follow different tests**. Perform independent ingredient-disclosure analysis using the *actual current version* of Annex II §§3.2.1–3.2.4; assess the applicable lowest conditional comparator, specific limits, hazard status, national/Union OEL status, PBT/vPvB/endocrine and other triggers as defined. **Article 31(3) on-request SDS trigger is a separate duty**.
- Ingredient below a whole-mixture classification threshold may still require Section 3 listing. Conversely not every intentionally present chemical must necessarily be disclosed by the minimum rules.
- Require composition, ingredient identities/classes, concentrations/ranges, SCLs, M-factors, ATEs, relevant OELs and applicable status as appropriate. If missing, flag a potential legal gap or NOT_VERIFIED, **not a proven omission**.

## G. Reporting, triage, fix and retest
Use `references/REPORT_SCHEMA.md` and `templates/review_report.md`. Every issue must have:
1. stable ID, class, severity and track;
2. page/section and exact observation;
3. verified legal pinpoint **or identified nonbinding guidance/internal source**, not a blurred mixture;
4. applicability conditions and verification status;
5. effect on clarity or safety; concise, product-specific reason;
6. corrective action and whether it requires a field edit, product-data investigation, classification/transport re-evaluation, translation, version control or distribution action;
7. specific evidence and owner needed, acceptance test, and `OPEN` status.

**Remedy order:** (i) prevent unsafe erroneous advice; (ii) obtain verified source/data; (iii) determine legal requirement and content; (iv) implement correction; (v) compare 1–16 for new contradictions; (vi) competent-person release decision. A suggested phrase never proves a property.

## H. Reporting restrictions
Counts by class refer only to **identified findings**, not a percentage of compliance. Coverage counts refer to checks actually assessed; do not use missing evidence to inflate passes. Report `LEGAL_SOURCE_STATUS: VERIFIED_FOR_FINDINGS / PARTIAL / NOT_VERIFIED` and `DOCUMENT_SCOPE: FULL / PARTIAL / SELECTED_SECTIONS`.

Use language “no issues identified in the checks performed” rather than “SDS complies with EU law.” No automated certification or invented inspection powers. If exact governing law cannot be checked, do not hide this limitation.
