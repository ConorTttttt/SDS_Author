# EU SDS Reviewer acceptance and adversarial tests (specification, not executed Gemini results)

Each test should feed a minimal SDS excerpt or complete test SDS as specified, the relevant product/legal evidence, and ask for FULL_REVIEW/TARGETED_REVIEW/FIX_PLAN/RE_REVIEW. The output must preserve four classes, separate severity, cite binding law for proven breaches, suggest evidence-based corrections and record unknown scope. **A test's expected result is conditional on its supplied legal/source assumptions.**

| ID | Scenario / supplied evidence | Expected classification and rationale | Key negative assertion |
|---|---|---|---|
| T01 | Complete 8-page REACH SDS with no page numbers on pages 2–8; applicable Annex II 0.3.2 verified. | LEGAL_NONCOMPLIANCE, direct page-format requirement; add numbering/continuation. | Not RECOMMENDATION just because 'formatting'. |
| T02 | First page of a **revised** complete SDS has no date or predecessor version; currently applicable Annex II 0.2.5 checked. | LEGAL_NONCOMPLIANCE; corrected controlled revision metadata and change history. | Don't invent revision date. |
| T03 | Only Sections 1–4 uploaded; no Section 14 shown. | NOT_VERIFIED/out of checked scope for §14; cannot allege missing §14. | No false confirmed missing heading. |
| T04 | Product mixture SDS has no UFI in Section 1; no information whether UFI is stated in the SDS or other applicable obligation. | NOT_VERIFIED or specific POTENTIAL only with evidence of requirement. | Never blanket “UFI absent => illegal SDS”. |
| T05 | Section 8 generic glove advice, but exposure type and product data unavailable. | POTENTIAL_NONCOMPLIANCE if specific legal applicability plausible; ask for exposure, glove/permeation data. | No confirmed breach or invented breakthrough time. |
| T06 | Comprehensive Section 8 glove advice and relevant ES annex supplied, but a reviewer prefers longer prose. | RECOMMENDATION only if clarity improved; avoid duplicate legally mandatory data demands. | No breach from stylistic preference. |
| T07 | Approved company phrase bank rejects otherwise correct SDS wording, no relevant binding requirement unmet. | RECOMMENDATION/internal control. | Internal wording policy is not EU law. |
| T08 | ECHA REF-11 lists a typical Section 9 issue; supplied Section 9 has justified N/A for a property with actual physical-state evidence. | No finding for that property; optionally separate guidance advice if justified. | REF-11 finding frequency is not law. |
| T09 | Nonclassified mixture with an ingredient at a concentration that *may* trigger §3.2.2; actual ingredient classification/OEL unknown. | POTENTIAL_NONCOMPLIANCE or NOT_VERIFIED; collect ingredient-specific statuses and evaluate correct branch. | No universal 1% ingredient shortcut. |
| T10 | Classified mixture Section 3: complete validated ingredient matrix shows a compulsory-listed ingredient omitted; applicable §3.2.1 and threshold verified. | LEGAL_NONCOMPLIANCE; supply precise comparator and add legally required component detail. | No false claim omission is due solely to mixture hazard contribution. |
| T11 | Section 8 lists no OEL but supplied country has a binding applicable OEL verified for a component. | LEGAL_NONCOMPLIANCE if actual omission, Member State provision and Annex II §8.1 application proved; give reference and correct entry. | Not claim same rule across all Member States. |
| T12 | Section 8 lists an EU indicative OEL; target Member State not stated. | NOT_VERIFIED/POTENTIAL according to evidence; determine national rule. | Do not convert EU number to national legal value. |
| T13 | SDS classification is said to be obsolete due solely to a future CLP application date; market-placement transition applies. | NOT_VERIFIED until date, CLP version and market facts established, possibly no finding. | No premature non-compliance finding. |
| T14 | 2024/2865 provision changed by 2025/2439; reviewer tries original postponed date. | Reject original date; verify the exact affected article, application now due and instrument. | Don't claim entire CLP postponed. |
| T15 | EU SDS in German supplied to target market GB only. | Scope clarification: not automatically EU REACH breach; GB regime out of scope. | Do not treat GB as EU Member State. |
| T16 | Same mixture shows “nonflammable” in §9 and verified measured low flash point plus independently classified fire hazard in §2. | TECHNICAL_PLAUSIBILITY issue; potentially LEGAL_NONCOMPLIANCE once exact applicable duty/proof established; fix with validated report, check §§2/5/7/9/10/14. | Don't choose a flash point or UN number arbitrarily. |
| T17 | Section 14 states non-dangerous for transport, but no transport assessment or product configuration data given. | NOT_VERIFIED or POTENTIAL if positive conflicting evidence; request independent multimodal determination. | No auto DG status from CLP. |
| T18 | A full SDS with all 16 headings; no composition, CLP or measured property evidence. | Structure may be checked, technical truth remains NOT_VERIFIED; no global 'compliant' or score. | Presence of headings does not prove accuracy. |
| T19 | Manufacturer supplied revision history but not customer distribution log. | Internal revision text can be checked; Article 31(9) notification remains NOT_VERIFIED. | No inferred late delivery from PDF. |
| T20 | First full review correctly marks missing §4.3 as LEGAL_NONCOMPLIANCE; re-review inserts scientifically unsupported first-aid claim. | Remains UNRESOLVED/PARTIALLY_RESOLVED pending evidence; report regression risk. | Added text does not automatically resolve. |
| T21 | Two independent deficiencies: verified missing §14 heading and nonbinding recommendation to simplify §7 wording. | Two findings, legal and recommendation, different causes, independent priorities. | No double-counting one issue. |
| T22 | Severe potential error in PPE but legal exception unresolved; trivial verified page-format defect. | PPE POTENTIAL_NONCOMPLIANCE/CRITICAL; formatting LEGAL_NONCOMPLIANCE/MINOR. | Priority != legal proof. |
| T23 | SDS officially must be in a Member State language; authenticated actual market language and national exception rule checked, SDS only in incompatible language. | LEGAL_NONCOMPLIANCE with Article 31(5)/country exceptions documented; fix translated technically verified SDS. | Do not demand translation just because recipient country guessed. |
| T24 | Some hazard data absent, but 'not available' accompanied by a documented allowed explanation. | Conditional analysis of exact field; only legal breach if actual applicable duty unmet. | Don't require manufactured measurements. |
| T25 | Full SDS applies to relevant nanoforms; form-specific data not clearly identified; verified REACH Annex II 0.1.3 applicability. | Possible LEGAL_NONCOMPLIANCE when exact requirement and document failure proved, else POTENTIAL. | No nanoform assumptions for every mixture. |
| T26 | SDS supplier has no verified label, no official CLP version, and notebook only. | NOT_VERIFIED classification/label, request validated evidence and exact current H/EUH/P. | Approved phrase bank is not official law or classifier. |

## Hard pass criteria for a generated review
- Every issue has exactly **one** of four classes and a separate priority.
- Each LEGAL_NONCOMPLIANCE cites an **actually examined** binding provision and demonstrates scope, date, applicable conditions, document evidence, and unmet obligation. No generic “REACH says so.”
- Every recommendation cites nonbinding guidance or internal rationale, without masquerading as law.
- Every NOT_VERIFIED/POTENTIAL finding specifies decisive evidence or law required to settle it.
- There are independent content, plausibility and temporal/country checks, and unreviewed sections remain NOT_CHECKED.
- Each finding has concrete corrective action, owner, acceptance test and cross-section regression review.
- Revised text is not called approved; no fabricated classifications, ingredient limits, OEL, UFI, UN number, measured value or phrase ID.
- Report says NOT CERTIFIED.

## Execution status
**Test specifications only.** The repository contains no proof these scenarios have been executed in Gemini with real source retrieval or real company SDSs. Validation of legal/chemical accuracy and coverage remains required by a competent reviewer.
