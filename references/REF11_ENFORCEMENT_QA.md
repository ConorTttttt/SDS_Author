# ECHA REF-11-derived inspection and plausibility control matrix

**Version:** 1.0, package v3.0. **Source:** ECHA Forum, *REF-11 project report on Safety Data Sheets (SDS)*, December 2024, document ECHA-24-R-13-EN (42 PDF pages; printed pages 5, 12–19, 26–30, 33–40). Original: `sources/ECHA_REF11_SDS_Enforcement_Report_Dec2024.pdf`.

## What this reference does and does not establish

REF-11 reports findings from a **2023 enforcement project** in 28 participating countries, reported in December 2024. It is a **descriptive enforcement report**, not legislation, not a binding interpretation for all cases, not a 2026 legal snapshot and not a statistically representative market survey. Inspectors' primary checks were of completeness; additional correctness/plausibility checks were not uniform in depth. Project results must never be represented as probability that an arbitrary user's SDS will fail.

- **2,528 SDS examined.** Overall reported non-compliance was about **35%** in the inspections; this cannot be generalised to the whole EU/EEA market (report pp. 2, 5, 20–21, 28).
- **513** of 1,883 SDS for which inspectors indicated quality observations were identified as incorrect or implausible. In the **513** cases, issues were associated with **Section 8: 249 (49%), Section 3: 240 (47%), Section 9: 182 (36%), Section 1: 157 (31%), Section 2: 122 (24%)**. Sections overlap: do not add percentages, and do not call these percentages the failure rates of all 2,528 SDS (report pp. 16–17, Table 3).
- Of eligible inspected SDSs, presence of **ATE** information was reported in **680/1,049 (65%)**, **SCL** in **839/1,029 (82%)**, and **M-factor** in **693/876 (79%)** (report pp. 12–13). These are empirical findings, not concentration thresholds.
- For 84 SDSs where nanoform information was checked, 56 were missing required information by the project checks; for 130 SDSs associated with ED properties, 68 had required information in all relevant subsections (report pp. 15–16). Interpretation of nanoforms evolved during the inspection; see the caveat below.

**Source classification:** Every check below is an internal *review question derived from* the report, marked `[REF-11 QA]`. When determining a legal defect, separately cite the exact current legal text and its applicability. The report alone is NOT sufficient to assert a statutory non-compliance.

## Standard inspection statuses

For **every** line below, determine: `PASS` (shown and substantiated), `FAIL_VERIFIED` (confirmed deviation from verified applicable legal/product evidence), `ISSUE_SUSPECTED` (plausibility concern or a possible mismatch), `NEEDS_EVIDENCE` (source/value or legal basis missing), `NOT_APPLICABLE` (justified), or `NOT_CHECKED` (not inspected). Never collapse the latter three into a pass or fail. Display **two tracks**: completeness and scientific/technical plausibility.

For `FAIL_VERIFIED`, include verified **applicable** law with article/subsection and document version; otherwise use `ISSUE_SUSPECTED` or `NEEDS_EVIDENCE`. The severity scale `BLOCKER / MAJOR / MINOR / REVIEW` is an **internal drafting triage**, *not an official REF-11 ranking*.

## Inspection matrix (ECHA REF-11 Table 4, printed pp. 18–20; Annex I questionnaire pp. 33–38)

| ID | SDS item | What to check, grounded in REF-11 | Required evidence / important conditional logic | Related check |
|---|---|---|---|---|
| R11-01 | 1.1 | Product identifier matches supplied product and label. | Authorised product identity and current label; no guessing. | 2.1, 2.2 |
| R11-02 | 1.1 | If a UFI is **included in the SDS**, it is in subsection 1.1, not accidentally 2.2. Independently determine whether UFI must be on SDS or can be on label; **do not assume UFI is mandatory in every SDS**. | Packaging, uses, Annex VIII/CLP applicability, actual UFI source. | SDS 1.1 / CLP label / PCN |
| R11-03 | 1.2 | Identified uses actually reflect recipients; uses advised against and reasons considered where applicable. | Identified uses, use conditions and any CSR/exposure scenario. | 7, 8, ES |
| R11-04 | 1.3 | Full actual supplier details including address, phone, relevant SDS e-mail; a distributor supplying the SDS may have to identify itself. | Supplier chain + recipient country. | 1.4 |
| R11-05 | 1.4 | Emergency information telephone details correct and usable; official advisory-body details and limitations when applicable. | Target country-specific checked service, hours, restrictions. | local compliance |
| R11-06 | 2.1 | Complete whole-product classification; classification scientifically consistent with ingredient and test evidence. | Verified endpoint-level CLP classification, calculation/test rationale. | 3, 9, 11, 12 |
| R11-07 | 2.2 | Pictograms, H/EUH/P wording and signal word correct and match **actual label**; do not add every candidate P phrase. | Approved label & controlled official statement wording. | 2.1, label |
| R11-08 | 2.2 / 15.1 | Relevant **REACH authorisation number** reflected in 2.2 when required and matched to conditions/monitoring in 15.1. Do not place the number only in 15.1, and do not infer authorisation from an SVHC listing alone. | Applicable authorisation decision/use + official source. | 15.1, 7–8 |
| R11-09 | 3.1 / 3.2 | Use correct subsection (3.1 substance / 3.2 mixture); mandatory substances not omitted; avoid conflating Section 3 disclosure with contributors to whole-mixture classification. | Composition, relevant Annex II disclosure thresholds, exposure limits, PBT/ED, application dates. | 2.1, 8.1 |
| R11-10 | 3.1 / 3.2 | Each listed constituent has accurate identity and classification; ATE **with route**, SCL and M-factor provided **if applicable and available**. | Actual ingredient dataset + checked Annex VI/C&L/source; record `NOT_AVAILABLE` vs `NOT_APPLICABLE`. | 2, 11–12 |
| R11-11 | 6.1 | Personal precautions/PPE clearly distinguish non-emergency personnel from responders, where relevant. | Release conditions, worker roles, exposure pathways. | 8.2 |
| R11-12 | 8.1 | Occupational exposure limits accurate for **destination Member State**, with relevant notations, source and legal basis; do not use another country's OEL by default. | Current dated official OEL source, substance identity, limit type/units. | 3.2, 15 |
| R11-13 | 8.2 | PPE instructions specify suitable and sufficient protections with relevant details (e.g. glove **material, thickness, breakthrough time** when required/available, and actual relevant use conditions); do not invent product performance data. | SDS manufacturer/glove permeation data, task and exposure, applicable standards. | 6.1, 7, 11 |
| R11-14 | 8.2 | Respiratory protection type/use conditions explained when relevant; don't automatically say 'no respiratory protection needed' for volatile/mist-generating use. | Volatility, process, exposure monitoring/assessment, ventilation and respirator specifications. | 7, 9, 11 |
| R11-15 | 8.2 | Environmental exposure controls meaningful when applicable. | Environmental hazard, site/process controls and exposure scenario. | 6, 12, 13 |
| R11-16 | 9.1 | Every required physical/chemical parameter has value or appropriate no-data/non-applicability explanation; do **not** fill numeric parameters from the chemical family. | Physical measurements, method, conditions, mixture profile. | 2, 5, 7, 10, 14 |
| R11-17 | 9.1 | Particle characteristics given where relevant to solids/nanoforms, subject to actual applicability. | Form, registered nanoform status, available particle characteristics. | 3.1/3.2, 9 |
| R11-18 | 9.2 | Subsection present, relevant other physical hazards/safety properties included and consistent with composition; not a generic boilerplate 'N/A'. | Safety-relevant properties and relevant physical hazard assessment. | 2, 3, 10 |
| R11-19 | 10.2 / 10.4 | For desensitised explosives, check special stability/condition information when applicable. | Verified physical hazard classification and stability data. | 2, 5, 7, 9 |
| R11-20 | 11.1 | Toxicological evidence is represented adequately; no contradictions with classification or unsupported negative claims. | Supplier/mixture evidence and classification reasoning; distinguish no study from negative result. | 2, 3 |
| R11-21 | 14.2 / 14.7 | Transport names and bulk transport information addressed, with mode and applicability; don't infer UN numbers from CLP. | Verified ADR/IMDG/other transport assessment. | 2, 9 |
| R11-22 | 15.1 | Relevant national + EU legislation, restrictions, authorisation decisions and **conditions/monitoring** addressed as applicable. | Destination state, legal-source register, relevant decision. | 2.2, 7–8 |
| R11-23 | 16 | Abbreviations explained, revisions identified, and mixture classification method reported where required. | Revision control, endpoint-level classification dossier, section 2 text. | 2, 3 |
| R11-24 | 2.3, 3.2, 11.2, 12.6 | Endocrine properties checked and documented **across all relevant subsections** when applicable. | Ingredient ED evidence and applicable law/date. | ED cross-section package |
| R11-25 | 3.1/3.2, 9 (and 1.1 for substances as applicable) | Nanoform information linked across the applicable sections. **Do not apply Section 1.1 nanoform requirement automatically to a mixture**: REF-11 describes ECHA FAQ 2015 clarification during the project. | ECHA FAQ 2015 + current Annex II, product form. | nanoform cross-section package |
| R11-26 | Supply / version | SDS supplied actively as required; material updates tracked and communicated to applicable past recipients, not merely a website upload. | Article 31 basis, actual dispatch/revision data; a document cannot prove its own distribution history. | 1st page, 16 |
| R11-27 | Exposure scenario | Determine whether annexing or incorporating ES information is required and carried out appropriately; country language considered. | Registration/CSR/ES and upstream supplier info. | 1.2, 7, 8, annex |
| R11-28 | Language | SDS and attached ES comply with market's language regime; English draft ≠ automatically fit for every country. | Recipient Member State rules and actual languages. | all sections |

### Important interpretive safeguards

1. **Authorisation number is a Section 2.2 check.** REF-11 executive summary (p.6) contains an inconsistent subsection reference; its detailed Table 4/questionnaire and discussion (pp. 18, 26–27, 34) refer to **2.2**, with the related authorisation conditions in **15.1**. Follow the **verified legal text** for a binding conclusion, and use this report only to motivate cross-section checking. Do not repeat the isolated p.6 subsection reference as law.
2. **Nanoform/mixture caveat:** REF-11 p.26 says interpretation changed in the inspection period after **ECHA FAQ ID 2015** clarified that **1.1 does not apply to mixtures** in that context. Verify the latest FAQ/legal text before asserting a deficiency; still inspect relevant **3 and 9** information. The report's aggregate results may be affected by that interpretive change.
3. **Endocrine classes changed after the inspection era:** Any note in the report saying ED is not part of CLP classification describes its **historical inspection context**, not a rule valid for every current product. The later CLP changes introduced by Regulation (EU) 2023/707 and their staggered application dates must be checked for the product. Never equate an ED assessment list entry, CLP hazard classification, REACH candidate-list status or biocidal/PPP ED criteria without establishing which rule applies.
4. **No invented thresholds:** The REF-11 dataset does not itself supply the current Section 3 threshold mapping or CLP decision algorithm. Use the applicable legislation, not a report's percentage or a generic 1% rule.
5. **Document issues vs supplier obligations:** Contents, legal delivery, language and revision communications are different audit tracks. You cannot assess a supplier's past delivery records merely from reading an SDS PDF.

## Consequences for phrase selection and drafting

For each selected approved phrase, record:

`phrase_id | section | content claim(s) covered | evidence_id(s) | REF-11 review IDs addressed | uncovered mandatory data elements | cross-section dependency | result`.

A phrase can be **verbatim and APPROVED** but **insufficient** to meet an Annex II content obligation. Example: a general 'use suitable gloves' stock phrase may be approved for 8.2 but not by itself substantiate material/thickness/breakthrough requirements when those details are applicable. Keep the phrase, identify its coverage gap, and obtain factual values or more suitable approved wording. No new words may be invented solely to pass a check.

Distinguish: `wording_approved` ≠ `product_suitability_verified` ≠ `mandatory_content_complete` ≠ `regulatory_released`.

## Severity and answer policy

- `BLOCKER`: verified or strongly indicated material health/environmental control contradiction, absent indispensable input for a high-risk claim, or known invalid use of approved phrases. Explain whether this is an internal hold or verified legal non-compliance.
- `MAJOR`: possible required SDS content omitted, wrong country OEL, incomplete ingredient/ATE/SCL/M-factor reporting, incomplete PPE protection detail, unverified hazard/transport claim, or mismatch between critical sections.
- `MINOR`: readability, explanatory, traceability or formatting issue not established to affect mandatory or safety-critical information.
- `REVIEW`: unclear evidence/applicability, unverified law or unresolved scientific interpretation. Do not pretend uncertainty is a legal breach.

**Priority is a human-review triage recommendation, not a statutory grading.** A phrase-drafting session should still run the relevant REF-11 checks, but only for affected sections; a full SDS audit should run all 28 questions and mark unavailable sources or skipped checks explicitly.
