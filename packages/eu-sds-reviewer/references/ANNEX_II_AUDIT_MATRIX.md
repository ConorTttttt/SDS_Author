# Clause-grounded EU SDS audit matrix — conditional, not a universal fail checklist

**Use:** a prompt-based retrieval/checklist for a competent reviewer. It is **not** an exhaustive, verified extraction of all legal provisions. Before classing an observation as LEGAL_NONCOMPLIANCE, inspect the actual applicable REACH Annex II Part A/Part B paragraph plus CLP/national provisions, date, exceptions and product facts. The supplied REACH consolidation (22 June 2026) provides a versioned locator; current official law still controls.

Each item: `check ID | possible legal hook (verify actual wording) | evidence needed | possible corrective action`. Missing evidence normally starts as POTENTIAL_NONCOMPLIANCE or NOT_VERIFIED, not a breach.

## Horizontal gates — all SDSs within scope

| Check | Legal hook to verify | Test and remedy |
|---|---|---|
| H-01 Full 16 headings | REACH Article 31(6); Annex II Part B | Inspect complete pages for exact, appropriate section sequence/labels. Insert missing statutory headings and applicable content. |
| H-02 Subsection presentation | Annex II 0.4 and Part B | Required applicable content in correct subsection; no blank subsections. Populate accurately or explain evidence-based non-applicability/unavailability where permitted. |
| H-03 Author/date/version | Annex II 0.2.3, 0.2.5; Article 31(6)/(9) as applicable | Compilation/revision date, replaced version on first page, changes communicated in 16 or elsewhere; competent author is an external process check. Repair metadata from controlled records. |
| H-04 Page numbering | Annex II 0.3.2 | All SDS pages, including annexes, numbered and extent/continuation indicated. |
| H-05 Clear, accurate text | Annex II 0.2.4 | Detect contradictions or misleading blanket assurances, not editorial preferences alone. Replace only with justified product-specific information. |
| H-06 Market language | Article 31(5) + national rule | Compare actual text and official language requirement/exception for each destination. Verified lack of required language is a legal issue; document-only review may not establish destination. |
| H-07 Supply and updates | Article 31(8)–(9) | Assess only with supply ledger, event trigger, recipients and actual version delivery; never infer breach from SDS PDF alone. |
| H-08 ES/CSR link | Article 31(7); Annex II 0.1.2 and relevant §8/15 | Verify whether ES/CSR required, covered uses and attachments; do not require an ES unconditionally. |
| H-09 Different forms/nanoforms | Annex II 0.1.3 and applicable §§1/3/9 | Only for relevant different forms/nanoforms; ensure form-specific safety data attributable to the correct form. |

## Section 1 — Identification (1.1–1.4)
- **S1-01 / §1.1:** product identifier matching actual CLP label; registration details if required; clear IDs for forms; UFI **if shown in SDS** in §1.1, not universal UFI mandate. Evidence: actual label, registration record, applicable UFI condition. Fix: correct identifier/conditional registration/UFI location based on verified sources.
- **S1-02 / §1.2:** relevant identified uses, specific uses advised against where applicable and reasons. Evidence: product dossier/ES. Fix: align use statements.
- **S1-03 / §1.3:** responsible supplier full identification and actual contact information including competent SDS email. Evidence: organisation/contact records and country role. Fix verified details, not invented addresses.
- **S1-04 / §1.4:** accessible and appropriate emergency service contacts; hours/limitations where relevant; member-state advisory service condition. Evidence: verified country emergency information. Fix verified phone/hours/scope.

## Section 2 — Hazards (2.1–2.3)
- **S2-01 / §2.1:** accurate current CLP classification, clear 'not classified' where applicable and required hazard details. Evidence: validated classification & correct applicable CLP law, transitional status. Fix section from independent classification assessment, **not from model guess**.
- **S2-02 / §2.2:** actual legally required label elements, pictograms, signal word, H/EUH/P statements and relevant supplemental elements; compare actual approved label. Fix from verified label and applicable legal statement text. Do not flag a difference without proving its obligation.
- **S2-03 / §2.3:** other hazards and conditional PBT/vPvB, endocrine and additional concerns. Verify relevant status thresholds/current law; don't presume every product contains such substance. Fix documented status/explanation.

## Section 3 — Composition (3.1 substances; 3.2 mixtures)
- **S3-01 / §§3.1/3.2:** correct substance/mixture branch; identities, concentration or permitted ranges and relevant impurities/additives as applicable. Evidence: restricted composition dossier.
- **S3-02 / §§3.2.1–3.2.4:** individually verify mandatory ingredient disclosure. Classified vs nonclassified mixture thresholds **differ**; consider SCL, M-factor, ATE, OEL, health/environment classifications, PBT/vPvB/ED and lowest relevant clause-specific comparators. Do not apply one '1%' shortcut or infer absence from an incomplete ingredient list.
- **S3-03 / §§3.2.3–3.2.4:** listed component classification, H/EUH codes, identity/CAS/EC identifiers, registration numbers and available SCL/M/ATE/ED/nanoform particulars as required; verify conditional partial number masking and approved alternative-name allowance.
- **Correction:** create per-ingredient *legally justified* inclusion matrix; amend entries and §16 full statement text using validated data. Keep confidential ingredient input out of public review reports.

## Section 4 — First-aid (4.1–4.3)
- **S4-01:** exposure-route guidance, first aider protection where relevant; delayed symptoms and need for medical intervention. Verify consistency with §§2, 8 and 11. Correct unsafe contradictions with qualified technical evidence, not boilerplate.

## Section 5 — Fire-fighting (5.1–5.3)
- **S5-01:** appropriate and inappropriate media, special fire hazards, responder PPE and measures. Compare §9 flash/flammability and §10 hazardous decomposition. Verify applicability to physical form/use. Fix with confirmed firefighting advice.

## Section 6 — Accidental release (6.1–6.4)
- **S6-01:** separate emergency vs non-emergency personnel, environmental precautions, valid containment and cleaning, appropriate links to §§8/13. Avoid speculative neutralisation/disposal advice. Correct with product/use-specific spill response evidence.

## Section 7 — Handling/storage (7.1–7.3)
- **S7-01:** actual use-related handling and hygiene, compatibility and safe storage conditions; specific end-use recommendations where applicable. Verify consistency with §§1.2, 8, 9, 10 and ES. Fix vague instructions only when required information is demonstrably missing.

## Section 8 — Exposure controls/PPE (8.1–8.2)
- **S8-01 / §8.1:** applicable **national** OELs and biological values with relevant fractions, units, notations, monitoring and where relevant DNEL/PNEC; assess country and ingredient applicability. Missing an applicable national value could be legal failure once verified; generic EU values alone may not suffice.
- **S8-02 / §8.2:** engineering/environmental controls and context-appropriate personal protection; suitable glove material/thickness/breakthrough-time details where relevant, eye/face protection, respiratory filters/type and protective clothing. Annexed ES may supply some §8.2 information. **A generic glove phrase isn't automatically a proven breach**: evaluate actual use, exposure route, available evidence and exact legal clause. Fix with documented PPE specification from qualified evidence.

## Section 9 — Physical/chemical properties (9.1–9.2)
- **S9-01 / §9.1:** inspect each listed physical/chemical property and whether the product/form can have that property; check units, measurement method, temperature, relevant data source and justified unavailable/N/A statements. **Do not demand a fabricated numeric test result**, or mislabel unavailable data as inapplicable or ‘no risk’.
- **S9-02 / §9.2:** where relevant provide other physical hazards and safety characteristics, particularly where triggered by classified hazard class. Compare §§2/5/7/10/14. Correct data status, units and contradictory product facts with verified tests.

## Section 10 — Stability/reactivity (10.1–10.6)
- **S10-01:** evidence-backed reactivity, chemical stability, hazardous reactions, conditions to avoid, incompatible materials, hazardous decomposition; test consistency with Sections 5, 7, 9 and 14. No blanket 'stable' from absent data.

## Section 11 — Toxicological information (11.1–11.2)
- **S11-01:** route- and endpoint-specific toxicology information and classification-aligned health hazards, where relevant data and limitations are clear; conditional endocrine/other health hazard information. Separate mixture data from ingredient data. Fix contradictions with validated hazard dossier.

## Section 12 — Ecological information (12.1–12.7)
- **S12-01:** aquatic/other ecotoxicity, persistence, bioaccumulation, mobility, PBT/vPvB, environmental endocrine effects, other adverse effects; conditional status and evidence quality. No invented negative ecological conclusions. Compare §2/3/6/13.

## Section 13 — Disposal (13.1)
- **S13-01:** appropriate waste treatment advice for product and packaging, potentially prohibited methods, disposal constraints under relevant waste context. Verify region/use and actual waste code assignment if present. Fix with verified disposal specialist input, not generic unverified code.

## Section 14 — Transport (14.1–14.7)
- **S14-01:** confirmed modal classification and UN/ID number, proper shipping name, class, packing group, environmental hazards, user precautions and maritime transport in bulk according to IMO instruments as applicable. A CLP hazardous mixture can still be non-DG and vice versa. Do not infer a UN number or absence of DG status without competent transport assessment.

## Section 15 — Regulatory information (15.1–15.2)
- **S15-01:** correct relevant EU/national product regulations, REACH restriction/authorisation and affected uses/conditions if applicable; chemical safety assessment status. Verify actual ingredient/status, threshold, use and date; avoid generic lists as proof of applicability.

## Section 16 — Other information
- **S16-01:** needed abbreviations, methods of mixture classification provided by validated calculation, full legal hazard statement text where abbreviated, source/training info as applicable, revisions/changes where relevant. Compare §§2/3 and first-page revision metadata. Correct omissions using verified approved sources.

## Report discipline
- For every **legal** outcome, show **instrument + precise paragraph + application test + page/section + actual contrary evidence**.
- For ECHA/REF-11-derived improvements without an independent binding breach, tag **RECOMMENDATION**.
- If composition or country is not supplied, do not falsely 'pass' ingredient/OEL/label checks; classify specific plausible issues appropriately and list unknown checks.
- Prioritise harms but preserve **legal classification independent of severity**.
