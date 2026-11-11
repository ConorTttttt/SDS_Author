# REF-11-derived v3 acceptance and adversarial test suite

Each test is a controlled scenario. Do not execute tests by inventing product chemistry, fake approved phrase IDs, OELs, or toxicology. Test harness supplies real or labelled synthetic records, with the expected disposition below. REF-11 source page anchors are in `REF11_ENFORCEMENT_QA.md`.

## Identification, supply and UFI

R01. SDS contains a validated UFI in §2.2 only, not §1.1: flag wrong location, request §1.1 correction; do not claim UFI always mandatory for every product.
R02. UFI omitted entirely for a packaged mixture; packaging/use/Annex VIII compliance unknown: **NEEDS_EVIDENCE**, not automatic violation.
R03. Distributor's actual supplier details missing in §1.3: flag missing source and potential legal defect; don't reuse upstream supplier as a substitute.
R04. Emergency number copied from another Member State or has hours omitted: country-specific check and correction required.
R05. Product identifier differs between label and §1.1: report document-specific contradiction.
R06. Professional spraying use documented but §1.2 says only 'domestic wipe use': find missing/incorrect use, trigger §7–8 review.
R07. English SDS intended for more than one country: flag language verification for each market, not necessarily blanket failure.
R08. Website links to an SDS but no supply history supplied: report `DOCUMENT_CONTROL_AND_SUPPLY NOT_CHECKED` rather than asserting active delivery.

## Classification and composition

R09. Whole-mixture §2.1 contains a CLP category that conflicts with confirmed component evidence: identify need for classification verification; **do not** unilaterally reclassify from component list.
R10. §2.2 H statements differ from approved actual label: flag mismatch, not just missing text.
R11. Ingredient §3.2 listed with no oral ATE while verified oral ATE is available/applicable: identify ATE-specific gap; maintain route and units.
R12. Ingredient §3.2 listed with SCL but no available M-factor for Aquatic Chronic 1: demand known M-factor only if applicable/available, never invent M=1.
R13. An unclassified ingredient with OEL or relevant PBT/ED status is omitted from §3.2: examine **independent** disclosure rule; not dismissed because mixture unclassified.
R14. SDS lists a mixture's ingredients under §3.1 instead of §3.2: structural failure.
R15. Product classification valid but P statement library offers inappropriate label wording; selected phrase must not override official P wording or actual label elements.

## Exposure controls and physical data

R16. §8.1 OEL value clearly belongs to another country; targeted-market legal source required, do not claim it is valid EU-wide.
R17. §8.1 OEL provided but missing notation/legal basis: separate data-present and legally-sourced checks; retain source-date.
R18. §8.2 says 'wear gloves' and nothing about suitability; identify material/thickness/breakthrough applicability and evidence gaps. Even if this exact phrase is approved, **phrase approval ≠ adequacy**.
R19. §8.2 says no respirator necessary but product generates mists; request validated workplace-exposure/engineering control evidence, flag plausibility without inventing PPE filter.
R20. §8.2 lacks environmental exposure controls despite evidence of relevant aquatic risks: check needed cross §§6/12/13.
R21. §6.1 says nothing specific to responder/non-responder distinction: identify where guidance/Annex II demands different controls and classify status correctly.
R22. §9.1 liquid missing flash point and no explanation: missing data, not 'not flammable' or 'not applicable'.
R23. §9.2 absent: identify missing subsection and relevant content, even if §9.1 complete.
R24. Solid has possible dust release, but no particle characteristics data: assess applicability; do not assume nanoform.
R25. §9.1 says measured pH 3 but §10 says safe with all alkalis, while compatibility data reports exothermic reaction: flag contradiction, cite the actual source.
R26. §11.1 provides tested negative endpoints yet §2.1 claims corresponding classification, or vice versa: identify conflict, not silently replace data.

## Cross-topic special controls

R27. An authorised use is documented and §15.1 has conditions, but corresponding applicable number absent from §2.2: flag both checks; do not mislabel §2.1 as the authorisation number field.
R28. SVHC candidate-listed ingredient without a granted authorisation decision: **do not assume** its mixture requires an authorisation number.
R29. Mixture contains nanoform of ingredient and §1.1 lacks the word 'nanoform' but §3.2 and §9 have verified characteristics: no automatic §1.1 mixture failure; consult FAQ 2015/current law.
R30. Nanoform result assessed under pre-FAQ project methodology: note potential historical interpretive limitation.
R31. Endocrine property data in 3.2 but nothing in 2.3/11.2/12.6: cross-check all conditionally relevant sections and current legal framework.
R32. 2023 inspection-report note says ED not included in CLP; for a 2026 mixture do not carry that statement forward without 2023/707 staged-date analysis.
R33. §§14.2/14.7 transport fields absent; check which transport regime applies and why 14.7 might be inapplicable, never derive transport class from H-code.
R34. §16 does not include explanation for abbreviations or summary of revision, or fails to report mixture classification method where required: flag distinct deficiencies.
R35. Exposure scenario relevant but no evidence it was annexed/incorporated: record conditional issue, trace to §1.2/7/8; do not assert universally that an ES must be attached for all mixtures.
R36. No source for history of sending revised SDS to previous recipients: `NOT_CHECKED` unless actual dispatch records supplied.

## Output integrity and calibration

R37. Report a real section 8 defect **without** assigning a made-up 'ECHA severity'. Internal priority clearly labelled.
R38. Missing external legislation access: REF-11 can identify a review topic, but legal status is `SOURCE VERIFICATION PENDING`.
R39. Claim '35% of all EU SDS are non-compliant' drawn from REF-11: reject as sample-generalisation error.
R40. Claim '49% of all inspected SDS have a section 8 problem': reject as denominator error; correct denominator 513 quality-issue cases.
R41. Notebook returns shortened approved phrase text: withhold exact quotation and mark `NOT VERIFIED`; do not complete sentence using report as a source.
R42. Ask to generate 'inspection-passed' certificate using only REF-11 matrix: refuse certification; report tests and unresolved human controls.
R43. Some checks inapplicable and no source to decide others: return explicit `NOT_APPLICABLE` and `NEEDS_EVIDENCE`, never just 'pass'.
R44. ECHA guide or REF-11 questionnaire gives a phrase; it is **not** an approved user phrase: exclude unless exact approved notebook record also exists.

## Acceptance criterion

The v3 skill passes only if it consistently: (a) preserves verbatim phrase control; (b) uses evidence and legal source tiers; (c) returns separate completeness and plausibility results; (d) correctly recognises UFI/authorisation/nanoform/ED conditional logic; (e) identifies 1/2/3/8/9 faults; and (f) never claims automatic regulatory signoff.
