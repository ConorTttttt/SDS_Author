# Legal sources, hierarchy, and applicability — EU SDS Reviewer

## 1. Binding and nonbinding sources are not interchangeable

| Tier | Source | Permitted conclusion |
|---|---|---|
| A — binding | Regulation (EC) 1907/2006 (REACH), in the applicable version, notably **Article 31** and **Annex II Parts A and B**; Commission Regulation (EU) 2020/878 (Annex II amendment); Regulation (EC) 1272/2008 (CLP) as amended; Member State binding requirements as relevant. | A definite legal breach **only if** applicable text, effective date, fact and unmet requirement are verified. |
| B — authentic amendment/version checks | Official Journal instruments and EU EUR-Lex legal history/consolidations, including effective/application/transitional clauses. | Establish version and temporal applicability; historical law may govern old supply. |
| C — product evidence | Identified SDS and label, verified composition/ingredient identities/statuses, classification report, testing, upstream SDS, national OEL/ES/CSR/waste/transport advice; source and date. | Substantiate what the product and supplier actually do and whether required content is missing or contradictory. |
| D — interpretive | ECHA Guidance on the Compilation of SDS (v4.0, December 2020). | Good-practice interpretation; must be connected to binding law for an allegation. |
| E — enforcement experience | ECHA Forum REF-11 SDS enforcement report (December 2024). | Identifies common failure patterns and inspection-priority topics, **not independent legal duties**. |
| F — internal controls | Approved phrase library, company template, style guide, peer reviewer preferences. | Internal/process recommendations unless binding law has separately been broken. |

## 2. Primary official legal entry points
- REACH: https://eur-lex.europa.eu/eli/reg/2006/1907
- REACH Annex II amendment 2020/878: https://eur-lex.europa.eu/eli/reg/2020/878/oj/eng
- CLP: https://eur-lex.europa.eu/eli/reg/2008/1272
- CLP new hazard classes: https://eur-lex.europa.eu/eli/reg_del/2023/707/oj/eng
- CLP revision 2024/2865: https://eur-lex.europa.eu/eli/reg/2024/2865
- Amended staged dates in Regulation (EU) 2025/2439: https://eur-lex.europa.eu/eli/reg/2025/2439/oj
- ECHA SDS guidance: https://echa.europa.eu/-/guidance-on-the-compilation-of-safety-data-sheets
- ECHA REF-11 report: https://echa.europa.eu/documents/10162/2304648/wg_ref11_project_report_en.pdf

**Always inspect actual relevant paragraphs** rather than citing only a regulation number or copying an unverified summary. Verify whether additional amendments, corrigenda or national measures apply as of the target date. Do not fabricate Official Journal passage text or legal pinpoints.

## 3. Bundled PDFs (for retrieval, not automatic currentness)
- `sources/REACH_1907_2006_consolidated_EN_2026-06-22.pdf`: 603-page **non-authentic consolidated** REACH snapshot, header `22.06.2026 — 069.001`. Article 31 around PDF pp.39–42; Annex II Part A around pp.117–150; Part B around pp.150–152. Confirm on the PDF itself before citing a page: PDF viewer pagination can vary.
- `sources/ECHA_Guidance_on_Compilation_of_SDS_v4_Dec2020.pdf`: nonbinding guidance; do not use superseded 2020 transition explanations as if they determine 2026 law.
- `sources/ECHA_REF11_SDS_Enforcement_Report_Dec2024.pdf`: nonbinding retrospective enforcement survey; its inspection sample was not representative of the entire EU market.

The skill authoring date is 11 November 2026. The supplied PDF does **not** independently establish that no law changed since 22 June 2026. If online legislation cannot be checked, keep legal-version confidence explicit and generally use POTENTIAL_NONCOMPLIANCE unless a reliable supplied authoritative current version and other required proof is available.

## 4. Binding Annex II hooks (confirm exact version before conclusions)
- Article 31(1)–(3): determine SDS supply triggers including request scenarios, **separate from** Section 3 ingredient disclosure. A duty to provide on request is not automatically proof that the document provided was deficient.
- Article 31(5): official language(s) of the Member State where placed on market, unless that Member State provides otherwise.
- Article 31(6): 16 main SDS headings.
- Article 31(7): exposure scenario annexing only where relevant obligations apply.
- Article 31(8): timing and manner of first SDS supply (requires transaction evidence).
- Article 31(9): update triggers and provision of updated SDS to previous 12-month recipients (requires revision/distribution evidence).
- Annex II Part A 0.2.3–0.2.5: competent author, clarity, first-page issue/revision/version information and communication of changes.
- Annex II 0.3.2, 0.4 and Part B: page-numbering/length or continuation, information under correct subsections, no blank subsections, specified structure.
- Annex II §§1–16: *conditional* requirements by substance/mixture, classification, use, form, recipient Member State and data availability.

## 5. CLP date/transition tripwires
- Delegated Regulation (EU) 2023/707 inserted endocrine-disrupting, PBT/vPvB, PMT/vPvM hazard classes with **different dates** for substances and mixtures and transitional periods depending on prior placement on the market. Do not call a pre-transition label deficient without checking date and inventory/market evidence.
- Regulation (EU) 2024/2865 was **amended by Regulation (EU) 2025/2439** to postpone application of selected labelling/packaging obligations to **1 January 2028**. This does not blanket-postpone every CLP or REACH SDS requirement. Verify the exact article being applied.
- A harmonised classification or new ATP may have its own application dates. Document the CLP version, ATP, national regime and classification evidence used.

## 6. Mandatory legal-source record per proven finding
Record: `instrument | article/annex/paragraph/table | official text checked (yes/no) | edition/amendment | effective/application date | transitional condition and result | Member State | product applicability trigger | observed contrary SDS evidence | citation or supplied PDF page`.

If a threshold/cutoff, chemical status, OEL, language exception, specific concentration limit, M-factor, ATE, transport restriction or national emergency rule cannot be established, **do not invent it or turn it into a definite breach**.

## 7. National and external-process boundary
Verify each target Member State's official language rules, OELs/notations, emergency contacts, specific chemical provisions and use-context controls from appropriate official national sources. Don't use an EU indicative limit as a confirmed national legally applicable limit without verifying transposition/context.

Supply/distribution timing, previous-recipient update, staff training and genuine author competence cannot normally be proven from the SDS PDF itself. Mark these `EXTERNAL_PROCESS_NOT_CHECKED` unless transactional/HR records are supplied; never infer violation from missing documentary proof inside the SDS.
