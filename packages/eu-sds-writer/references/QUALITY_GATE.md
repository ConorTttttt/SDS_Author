# EU SDS writer — completeness and technical plausibility review

Derived from the supplied v4 REACH clause playbook, ECHA SDS compilation guidance and REF-11 inspection failure modes. **Two independent verdicts** must be reported for a full draft/review:
- `CONTENT_COMPLETENESS: PASS / GAPS / NOT_CHECKED` (all applicable Annex II first-level subsections, evidence-based information and formatting).
- `TECHNICAL_PLAUSIBILITY: PASS / ISSUES / NEEDS_EVIDENCE / NOT_CHECKED` (claims supported, safe use realistic, cross-section agreement).
A third field `LEGAL_SOURCE_CHECK: VERIFIED_FOR_SCOPE / PENDING` and `PHRASE_APPROVAL: VERIFIED / GAPS` prevent false signoff. The skill must not equate a complete-looking document with a safe or compliant one.

## Hard section gates
**1** Product identifier vs label; supplier name/address/phone/email; real emergency number with scope/hours; language/country/date/version and any UFI applicable to this SDS. No assumption every SDS requires UFI.

**2** Validated mixture/substance CLP classification, real label elements including applicable EUH/P statements, contextual other hazards (ED/PBT/vPvB where applicable); compare to 11/12.

**3** Appropriate 3.1 or 3.2; per-ingredient separate disclosure test; concentration/range, identities, available ATE/SCL/M-factors/status and rationale for relevant nonclassified components. Compare 2/8/11/12.

**4** Exposure-route-specific first aid, delayed effects, required medical treatment; no chemically unsafe generic advice or contradictory instructions.

**5** Suitable **and unsuitable** extinguishing media, combustion hazards and firefighter protection. Verify against 7/9/10.

**6** Non-emergency vs emergency precautions, environmental protection, technically valid containment/cleanup and references to 8/13; no default neutralisation without evidence.

**7** Use-specific handling, temperature/ignition/dust/vapour and segregation/storage compatibility, specific end uses aligned to 1.2/8 and real ESs.

**8** Correct **target-country** occupational and biological limits (units/notations/fractions, source date); appropriate ventilation/environmental control; PPE specified by evidence (hand protection material/thickness/permeation time, eye and respiratory characteristics as relevant) rather than generic claims.

**9** Every applicable 9.1 property evaluated, including state, colour, odour, melt/freeze, boil/range, flammability, explosion limits, flash, autoignition, decomposition, pH, kinematic viscosity, solubility, log Kow, vapour pressure, density/relative density, relative vapour density and particle characteristics. Add relevant 9.2 hazard/safety characteristics. `NOT AVAILABLE` ≠ `NOT APPLICABLE` ≠ `NEGATIVE TEST`; reasons and methods/temperature/units where appropriate.

**10** Each reactivity/stability/reaction/condition/incompatibility/decomposition claim substantiated; do not infer 'stable' merely from no incident report.

**11** Toxicological routes and hazard endpoints, acute/delayed effects, ingredient versus mixture data, 11.2 endocrine/other hazards where applicable; align with 2/3/4/8.

**12** Toxicity, persistence, bioaccumulation, mobility, PBT/vPvB, endocrine properties, other effects; distinguish lacking data from tested low concern; align 2/6/13/14.

**13** Treatment/disposal advice for product and packaging, correct jurisdiction/waste context. No invented waste code.

**14** Verified transport mode(s) ADR/RID/ADN/IMDG/air as applicable; 14.1–14.7 statements supported by independent transport data. No inference from CLP alone.

**15** Product/use-specific applicable regulations, restrictions/authorisations and CSA status with sourced details. Never cite a provision just because a chemical family could be affected.

**16** Abbreviations, exact H/EUH full texts when abbreviated elsewhere, data sources, mixture classification method(s) **as provided by a validated assessment**, change indication and training notes where appropriate.

## Cross-section contradictions (mandatory)
- Section 2 hazard and label ⇄ 3 constituent disclosure ⇄ 11/12 toxicological/ecological statements.
- 2 skin/eye/aspiration risk ⇄ 4 first aid ⇄ 7 handling ⇄ 8 PPE.
- 5 fire/combustion ⇄ 7 storage/ignition precautions ⇄ 9 flash/flammability ⇄ 10 reactivity ⇄ independently supported 14.
- 6 environmental controls ⇄ 12 hazards ⇄ 13 waste treatment.
- 1.2 identified use ⇄ 7.3 instructions ⇄ 8 protection / upstream exposure scenario.
- 1/2/3/8/15/16 product identifier, national context, OEL, legal and revision evidence.

For each observed issue record `subsection | quoted observation | issue | completeness vs plausibility | source/evidence | legal citation verification | severity | specific fix`. When only a draft document is visible, use `NEEDS_EVIDENCE` rather than alleging a verified infringement. REF-11 findings are prioritisation evidence only.
