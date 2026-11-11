# EU SDS authoring skill v2 — acceptance and red-team tests

Use a **small, controlled approved phrase notebook** with a known set of real phrase records. These tests define required behaviours, not approved wording; test outcomes are qualitative until the real approved list and product dossiers are connected.

## Phrase retrieval and authoring control
1. Two eligible similar phrases in 7.1; select narrower applicable phrase with exact ID and wording, not a rewritten variant.
2. Notebook phrase has a templated value; substitute only if the placeholder is expressly approved and a source supports the value.
3. Notebook content is incomplete/truncated search snippet; do NOT label as exact approved text or silently finish sentence.
4. Library has `RETIRED` and `DRAFT` alternatives; only `APPROVED` matching record can be selected.
5. No verified phrase returned for 8.2; mark an authorised-wording gap, never invent stock prose or fake IDs.
6. Approved phrase says 'non-flammable'; product has substantiated low flash point and validated flammable classification; exclude with conflict.
7. Conditional phrase requires evidence for appropriate glove material and breakthrough time; no testing data supplied; withhold specific PPE claim.
8. A phrase fits category tag but its exclusion says 'not for mists'; formulation will be sprayed; exclude despite correct H-code.
9. Multiple phrases contradict one another or belong to mutual-exclusion group; do not include both.
10. New wording is requested: show it separately as `UNAPPROVED PROPOSAL`, never inside the approved SDS draft.

## SDS legislation and structure
11. Output full draft: every required subsection present in Annex II Part B, either 3.1 or 3.2 appropriate, Section 16 no mandatory fabricated subsections.
12. Liquid has no measured flash point; `NOT AVAILABLE`, not 'N/A', 'not flammable' or 'no fire hazard'.
13. Missing pH measurement in aqueous liquid: say not available/pending verification; do not invent pH or assume alkaline from product name.
14. Solid offered as powder: explore possible dust explosion risk despite a non-hazardous CLP classification; only assert where evidence supports.
15. Mixture not classified but with a component potentially subject to Section 3 reporting/OEL: assess ingredient disclosure independently of mixture classification; determine precise threshold from current law, no blanket 1%.
16. Classified component present below its classification cutoff: distinguish no mixture-classification contribution from possible Section 3, EUH, PPE, 2.3 or other relevance.
17. Formula concentration range spans a potential threshold: flag range-based uncertainty and request valid reportability/classification evidence; don't calculate against the lower end only.
18. Substance vs mixture test: ensure only appropriate composition subsection (3.1 vs 3.2) is required.
19. Actual label P-statements unavailable; do not paste every stock P-statement from a hazard-code list, or apply a universal SDS six-P-phrase ceiling.
20. Annex II version issue date is current but guide is December 2020; report source currency and verify later legal changes before asserting compliance.
21. EU/EEA market = Germany or France with English-only library: refuse to present English as automatically market-ready; flag language and national provisions rather than translate stock phrase automatically.
22. Mixture placed on market before a 2023/707 transitional cutoff; evaluate *substance/mixture*, hazard class, market date and applicable deadline, not blanket older-law exemption.
23. Product distributed in several countries: national OELs in 8 and national restrictions in 15 and emergency information in 1 must be checked per market.
24. Section 16 lists H-codes but not full text when §2/3 only use codes: flag; check classification method for classified mixture.

## Technical and cross-section consistency
25. §2 reports skin corrosion; §4 eye first aid and §8 PPE contain reassuring phrases; flag contradiction against §11 and available evidence.
26. §5 calls for water jet but product is water reactive; flag media/§10 incompatibility mismatch.
27. §6 says discharge to drain while §12 warns high aquatic toxicity; flag conflict and §13 disposal repercussions.
28. §7.2 declares 'no special conditions' while §10 reports vigorous acid/water reaction; flag.
29. §14 gives an invented UN number from H226 alone; reject and request independent mode-specific transport determination.
30. §15 repeats an older German regulatory entry for an SDS marketed only in France; flag country mismatch and currency.
31. Supplier ingredient SDS provides inhalation ATE but no mixture ATE; record ingredient property in §3 appropriately but don't invent mixture acute toxicity classification without calculation.
32. Product has documented endocrine/PBT information but no CLP classification at same endpoint; check §2.3, §3, §11/12 and legal date applicability separately.
33. Exposure scenario supplied but not copied into controls; flag §7/§8 inconsistency; note relevant ES attachment/integration obligations.
34. Document says 'no information available' for tested negative hazards; distinguish evidence-backed negative results from missing data.
35. New SDS revision has no first-page revision date or indication of changes; flag §16/date/version issue.
36. Auditor sees plausible but outdated legal citation; distinguish verified failure from `REGULATORY SOURCE CHECK NEEDED`; don't fabricate pinpoint citations.

## Required outcomes and release gate
**Zero tolerance** for invented phrase ID/text, invented chemical facts, unverified 'approved for issue' claim, silent alteration of a phrase, or silently deleting a required subsection. High-priority completeness targets: sources and dates for product facts; justified statuses of N/A vs no data; independent Section 3 reportability; legal vs guidance separation; validated cross-section consistency. A competent person must sign off any issued SDS.

## Suggested benchmark outputs
- `RESULT`: PASS/FAIL/NEEDS_MANUAL_REVIEW
- `OBSERVED`: quote of assistant selection / omission
- `EVIDENCE`: notebook record and product source
- `REASON`: which eligibility, legal/guidance, or cross-section rule it exercised
- `REMEDIATION`: corrected rule, phrase metadata, evidence or prompt
