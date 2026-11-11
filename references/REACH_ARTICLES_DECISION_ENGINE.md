# Binding REACH obligations relevant to EU SDS authoring — versioned decision engine

**Source:** User-supplied `sources/REACH_1907_2006_consolidated_EN_2026-06-22.pdf`, consolidated text marked `02006R1907 — EN — 22.06.2026 — 069.001`. **Snapshot, not a live database and not the authentic Official Journal text** (see PDF p.1 disclaimer). Article references below were checked against this PDF on 2026-11-11. Its printed/PDF page numbers are identical. Final issuance requires applying legislation effective for the relevant date and country.

## A. Regulatory applicability BEFORE drafting

1. Establish product identity, whether **substance** or **mixture**, whether `Article 2` places it outside relevant Title IV obligations, supplier/recipient roles, whether it is supplied and to whom, target EU Member States, intended uses and issue/placement dates. A REACH registration exemption does **not** by itself mean an SDS exemption. Article 2 is nuanced; do not generalise across exemptions. `REACH Articles 2–3`, PDF pp.7–14.
2. Apply **Article 31(1)** for an SDS provided to a recipient: classified hazardous substance/mixture under CLP **or** substance meeting PBT/vPvB criteria **or** substance on the Article 59(1) list for other reasons. Do not incorrectly apply the substance-only PBT/Candidate List clauses directly to every non-classified mixture; Article 31(3) separately addresses mixtures on request. `Art.31(1)(a)-(c)`, pp.39–40.
3. For a **non-classified mixture**, separately assess **Article 31(3): SDS on recipient request** where it contains (a) a substance posing human/environmental hazards at >=1% w/w non-gas / >=0.2% v/v gas; (b) specified sensitiser/CMR/lactation/PBT/vPvB/Candidate List statuses at >=0.1% w/w non-gas; or (c) a substance for which there is a Union workplace exposure limit. Do not apply the 1% threshold to (c). This Article 31(3) test is **not interchangeable with Section 3.2 ingredient disclosure**. `Art.31(3)(a)-(c)`, p.40.
4. For hazardous substances/mixtures offered/sold to general public with adequate safety information, consider the **Article 31(4)** exception and the downstream-user/distributor request carve-out. Never assume all consumer supplies require the same automatic SDS delivery. `Art.31(4)`, p.40.
5. If **SDS is not required**, check **Article 32** obligations to communicate registration information if available, relevant authorisation/restrictions, and available risk-management information; do **not** automatically draft a purported mandatory SDS. `Art.32`, pp.42–43.

## B. Supply and document-control obligations

| Rule | Operative question | Actual REACH basis | Result if lacking |
|---|---|---|---|
| ART31-05 | Is SDS in official language(s) of target Member State unless that State provides otherwise? | Art.31(5), p.40 | Local language review blocker; English-only drafts are not automatically sufficient. |
| ART31-06 | Are 16 main headings present and SDS dated? | Art.31(6), p.41; Annex II Part B pp.150–152 | Draft/content blocker. |
| ART31-07 | Are relevant exposure scenarios attached/integrated as legally required for this role and use? | Art.31(7), pp.41–42; Annex II 0.1.2 p.117 | Evidence/attachment blocker. Check exceptions/role. |
| ART31-08 | Has an SDS been supplied free of charge on paper/electronically no later than first supply? | Art.31(8), p.41 | Supply-process item, not proven by a PDF alone. |
| ART31-09 | Was SDS updated without delay for new hazards/RMMs, authorisation grant/refusal, restriction; and reissued to recipients of preceding 12 months? | Art.31(9), pp.41–42 | Revision and distribution workflow, not just date stamping. |
| ART31-02 | If required CSA/CSR exists, is SDS consistent with it? | Art.31(2), pp.40–41 | Cross-reference blocker if mismatch. |
| ART34 | Is new hazard/RMM challenge communicated up the supply chain? | Art.34, p.43 | Process flag when triggered; do not falsely assert communication occurred. |
| ART36 | Are duty-supporting records retained for >=10 years after last manufacture/import/supply/use? | Art.36, p.44 | Record-control / retention action. |

## C. Authorisation / restrictions check for Section 15

- **Authorisation:** Identify relevant Article 59 Candidate List status, Annex XIV listing under Title VII, use-specific authorisation, decision number, conditions, monitoring and exemptions only from validated, current records. Annex XIV listing **does not automatically mean every use of every mixture is forbidden**. Check Articles 56–58, 60–66 as applicable. `Art.56`, pp.56–58; Annex II §15.1, PDF p.149.
- **Restrictions:** Check current restrictions for relevant substances, uses, concentrations and user categories under **Title VIII, particularly Article 67 and Annex XVII**; actual entry conditions and exemptions may be decisive. An Annex XVII listing alone does not establish product-level breach. `Art.67`, PDF p.68; Annex II §15.1 p.149.
- **Authorisation-related SDS content:** Applicable decision/number and relevant downstream-user conditions may affect §§2.2 and 15.1. Use the **text of Annex II** plus applicable CLP labelling and decision; the ECHA REF-11 report alone is not the legal basis. `Annex II §15.1`, p.149.
- **Assessment of substance status** must be separately recorded for each constituent, with concentration, use, jurisdiction, decision/entry and verification date. `NOT_CHECKED` means unknown, not compliant.

## D. Mandatory authoring output for this decision tree

```text
PRODUCT_SCOPE: substance | mixture | exempt-scope-review
JURISDICTION: EU Member State(s), with language per market
REFERENCE_DATE: YYYY-MM-DD  (law applicability, first supply and issue dates distinguished)
ART31_1: TRIGGERED | NOT_TRIGGERED | INSUFFICIENT_INFORMATION
ART31_3_ON_REQUEST: TRIGGERED | NOT_TRIGGERED | INSUFFICIENT_INFORMATION | NOT_RELEVANT
ART31_4_PUBLIC_EXCEPTION: APPLIES | DOES_NOT_APPLY | INSUFFICIENT_INFORMATION
ART32_INFORMATION: REQUIRED | NOT_REQUIRED | INSUFFICIENT_INFORMATION
EXPOSURE_SCENARIOS: REQUIRED | NOT_REQUIRED | INSUFFICIENT_INFORMATION
SDS_DELIVERY: REQUIRED | ON_REQUEST | NOT_REQUIRED_UNDER_31 | REVIEW_NEEDED
REACH_AUTHORIZATION: VERIFIED_APPLICABLE | VERIFIED_NOT_APPLICABLE | PENDING
REACH_RESTRICTIONS: VERIFIED_APPLICABLE | VERIFIED_NOT_APPLICABLE | PENDING
EVIDENCE: data source + date + pinpoint to statute or register for each result
```

Where the applicable rule depends on CLP classification, OEL, status in a dynamic list or market date, do **not** treat the supplied REACH PDF as evidence of the underlying current product fact. For the latter, ask for upstream SDS, product regulatory dataset, list extract, national OEL or validated classification. A `NOT_TRIGGERED` result is not a blanket statement that no other law applies.
