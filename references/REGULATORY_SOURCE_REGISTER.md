# Regulatory source register and date/version protocol

## Source status (prepared 2026-11-11)

| Source | Status | Application |
|---|---|---|
| REACH Regulation (EC) 1907/2006, Art. 31, 35, 36 and Annex II (Part A, Part B) | **Binding EU law, use current applicable consolidated text** | SDS trigger, content, format, supply, competent author, updates, retention. |
| Commission Regulation (EU) 2020/878, replacement of REACH Annex II | **Amending legal text** | Baseline format reflected in ECHA v4 guidance; its format transition concluded 31 Dec 2022. |
| CLP Regulation (EC) 1272/2008 (applicable consolidated text including Annexes I, II, IV, VI, VIII) | **Binding EU law, use current applicable version** | Classification, label elements, H/EUH/P language, mixture ingredients, UFI and relevant PCN information. |
| Commission Delegated Regulation (EU) 2023/707 | **Binding CLP amendment with staged application** | New endocrine disruption, PBT/vPvB, PMT/vPvM hazard classes; requires product-type/market-placement timing review. |
| Regulation (EU) 2024/2865 as subsequently amended | **Binding CLP amendment with staggered dates** | Product-specific CLP changes; check exact parts applying on the SDS date. |
| ECHA Guidance on the compilation of SDS, version 4.0 (Dec 2020; attached) | **Non-binding interpretation / compilation guidance; historical version** | Section-level explanations, examples, competency, cross-section review, evidence gathering, ES integration. |
| ECHA Guidance on the Application of the CLP Criteria | **Non-binding interpretation** | Classification methodology, not a substitute for legal CLP text and validated calculations. |
| ECHA Guidance on Labelling and Packaging under CLP; Guidance on Annex VIII | **Non-binding interpretation** | P-statement decisions, labelling, UFI/PCN caveats. |
| Target Member State OELs, emergency number rules, waste, workplace and other relevant law | **Country-specific** | Must be selected based on market; cannot simply copy from another country's SDS. |
| Dangerous-goods regulations (ADR, RID, ADN, IMDG, ICAO-TI/IATA DGR as applicable) | **Separate transport rules** | Source for Section 14; not inferred solely from CLP classification. |

## Primary URLs for human/legal verification
- ECHA guidance: https://echa.europa.eu/-/guidance-on-the-compilation-of-safety-data-sheets
- REACH (consolidated EU publication): https://eur-lex.europa.eu/eli/reg/2006/1907
- REACH 2020/878 amendment: https://eur-lex.europa.eu/eli/reg/2020/878/oj/eng
- CLP (consolidated): https://eur-lex.europa.eu/eli/reg/2008/1272
- CLP 2023/707: https://eur-lex.europa.eu/eli/reg_del/2023/707/oj/eng
- CLP 2024/2865 (check **consolidated**, not solely original publication): https://eur-lex.europa.eu/eli/reg/2024/2865

## Date-sensitive example — do not turn into a hard-coded universal rule
- 2023/707 generally applies to **newly placed-on-market substances** from 1 May 2025 and **newly placed-on-market mixtures** from 1 May 2026, with specified transitional treatment for products placed on the market before those dates (1 November 2026 and 1 May 2028 respectively). The author must verify relevant hazard-class provisions and product facts. In particular, as of 11 November 2026, the first of those transitional endpoints has passed.
- The 2024/2865 CLP revision has later amended application dates, including staged dates in 2026, 2027 and 2028 in its consolidated version. **Never blindly use the original regulation's unamended transitional schedule.**
- The ECHA guidance's 2020 statement that the 2020/878 format could be delayed until 31 December 2022 is **historical**. Do not offer 2015/830 as a valid current format for newly supplied SDSs.

## How to use this register
1. Record `intended_issue_date`, `placement_on_market_date`, `country`, `substance_or_mixture`, `intended_uses`, relevant `regulatory_snapshot_ID` and `checked_on`.
2. Check primary legal text, including consolidated amendments and effective/application/transitional dates for each requirement. Do not substitute a web search snippet for text if a legal determination matters.
3. Use a pin cite `REACH Annex II Part A §X` or `CLP Annex I §Y` **only if the referenced clause was actually verified**. Source citation to ECHA's commentary instead must be written `ECHA guidance, §3.N, p.N (guidance)`.
4. If a text cannot be checked, output `REGULATORY BASIS NEEDS VERIFICATION` and classify the consequence (blocking a release vs acceptable for exploratory phrase recommendations).
5. Always distinguish a component's status under a given regime from a declared whole-mixture classification; do not invent status from a CAS name.

This file is a navigation/procedure document, **not** a living legal database and not a regulatory determination for any named product.

## REF-11 report — distinct source tier

| Source | Tier | Permitted use |
|---|---|---|
| ECHA Forum **REF-11 project report on SDS**, December 2024, ECHA-24-R-13-EN; in `sources/ECHA_REF11_SDS_Enforcement_Report_Dec2024.pdf` | **Enforcement findings / inspector questionnaire, non-binding and retrospective** | Prioritise likely quality gaps, design a two-track completeness/plausibility audit, identify cross-section dependencies and test scenarios. **Never cite it as the legal basis for a duty**; verify the applicable binding text independently. |
| ECHA **FAQ ID 2015** on nanoform in mixtures, cited at REF-11 p.26 | **Interpretive clarification to check** | Report states Section 1.1 nanoform requirement does **not** apply to mixtures in that context. Verify current FAQ/current law before final determination; §§3 and 9 may still apply. |

**Historical-data caution:** Report was published December 2024 for 2023 inspections; descriptions of ED properties as not yet CLP classes must not override later CLP 2023/707 changes and implementation dates. Report p.6 contains an inconsistent reference to the authorisation number in §2.1, while the detailed results, discussion and inspection questionnaire (pp.18, 26–27, 34) check **§2.2**. Use verified applicable Annex II/REACH/CLP for binding conclusions; don't blindly import the isolated mismatch.

**Methodological caution:** Report 35% non-compliance refers to inspected cases, **not** a representative market estimate; Table 3's 49%/47% etc are percentages of the **513 quality-issue cases**, **not** all 2,528 inspected SDS. Distinguish availability of ATE/SCL/M-factor data from actual completeness and always use condition `if applicable/available`.

**Source URL for optional verification:** https://echa.europa.eu/documents/10162/2304648/wg_ref11_project_report_en.pdf

## V4 supplied full REACH consolidated snapshot (read first for REACH duties)

- **File:** `sources/REACH_1907_2006_consolidated_EN_2026-06-22.pdf` (603 pages; title-line `02006R1907 — EN — 22.06.2026 — 069.001`). Supplied by user. **Consolidated text not legal-authentic** (PDF p.1); authentic acts are published in the Official Journal and on EUR-Lex.
- **Pinpoint navigation:** Article 31 pp.39–42; Article 32 pp.42–43; Article 34 p.43; Article 36 p.44; Article 56 pp.56–58; Article 67 p.68; Annex II preamble/format pp.117–119; Part A §§1–3 pp.119–127; §8 pp.131–133; §9 pp.133–140; §15 pp.149–150; §16 p.150; Part B pp.150–152.
- **V4 derivative files:** `REACH_ARTICLES_DECISION_ENGINE.md`, `REACH_ANNEX_II_CLAUSE_PLAYBOOK.md`, `REACH_SECTION3_DISCLOSURE_ENGINE.md`, `REACH_MULTI_PRODUCT_SDS_COVERAGE.md`, `REACH_REGULATORY_DECISIONS.md`, `REACH_RULE_INDEX.jsonl`, `REACH_TEST_CASES.md`. They are practical reading aids, **not replacements for legal clauses**.
- **Novel risk:** REACH Annex II is necessary for SDS compilation, but also verify **contemporary CLP** classification/label/Annex VIII requirements, applicable national law and dated lists/authorisation decisions. Full REACH document alone does not establish those up-to-date facts.
- **Product grouping:** §1.1 p.119 expressly allows a single SDS for more than one substance or mixture subject to *full coverage of every one*. Not a numerical concentration or hazard-class shortcut.
