# REACH Annex II clause-driven SDS authoring — operative legal source

Source: user PDF `sources/REACH_1907_2006_consolidated_EN_2026-06-22.pdf`, Annex II **Part A pp.117–150** and **Part B pp.150–152**. Snapshot dated 22 June 2026. Each source page below is the PDF page, not an ECHA guidance page. This playbook *supplements* `ECHA_SECTION_PLAYBOOK.md` but governs any disagreement on actual obligations, subject to newer/applicable law.

## Core legal clauses (before section drafting)

| Annex II clause | Requirement / operational implication | PDF |
|---|---|---|
| 0.1.1–0.1.3 | Use Annex II with Article 31; harmonise with registration/CSR/exposure scenarios when relevant; disclose/link nanoform information where applicable. | 117 |
| 0.2.1–0.2.2 | Supply safety information sufficient for workplace, environmental and employer risk assessment purposes, not merely CLP label repetition. | 117 |
| 0.2.3 | Competent person authors SDS and receives training/refresher training. An LLM is not the competent person. | 117 |
| 0.2.4 | Clear, concise, precise; do not use unqualified reassurance such as 'harmless', 'no health effects', etc., or statements inconsistent with classification. | 117 |
| 0.2.5 | Initial compilation date on first page; for revisions 'Revision: (date)' on first page + replaced version; explain changes in §16 unless elsewhere. | 117–118 |
| 0.3.1–0.3.2 | Length appropriate to hazards/information; number all pages and annexes and show extent/continuation. | 118 |
| 0.4 | Information in appropriate Part B subsections; **no blank subsections**. | 118 |
| 0.6 | Applicable units of measurement under Directive 80/181/EEC. | 118 |
| 0.7 | Consider special cases in CLP Annex I §1.3 despite labelling derogations. | 119 |

## Per-section authoring decisions and cross-links

### Section 1 (pp.119–120)
- **1.1** CLP product identifier matching label; registered-substance identifier and registration number where required; partial registration-number omission is conditional on obligations including providing/forwarding a full number within **7 days** upon enforcement request. Use conditional logic, never casually redact. **One SDS may cover >1 substance/mixture only if Annex II requirements are met for every one**. For different forms/nanoforms distinguish data by form. UFI, **when indicated in the SDS**, goes in §1.1; not a universal inference that every SDS must display UFI.
- **1.2** Relevant identified uses and where applicable uses advised against/reasons; consistent with CSR/ES as relevant.
- **1.3** Full supplier address, telephone, competent SDS contact email, applicable nominated responsible-person details.
- **1.4** Emergency information service(s), target-country official advisory number where applicable, and hours/limitations.

### Section 2 (pp.121–122)
- **2.1** Validated CLP classification; clearly state a non-classified mixture; match registration/notification classification where applicable; include full classification/H-text in §16 where abbreviated.
- **2.2** CLP label symbols, signal word, H/P statements and applicable supplemental label elements as legally relevant; cross-check actual label, avoid inserting other advice under label requirements as if mandatory label P statements.
- **2.3** Other hazards, including PBT/vPvB, specified endocrine status and other non-classifying hazards; for mixtures check qualifying substances at **>=0.1% w/w** as described by this clause. New CLP hazard classes may change mixture classification obligations on relevant dates; never replace the §2.3 status analysis with a classification-only check.

### Section 3 (pp.122–127)
- **3.1** Substance main constituent identity; relevant classified impurity/stabilising additive contributing to *substance* classification; available SCL/M-factors/ATEs; nanoform particle characteristics when appropriate.
- **3.2** Mixture ingredients reported under §3.2.1 if mixture classified and §3.2.2 if unclassified; supplier may voluntarily list additional ingredients. Concentration may be exact or a permitted range. **Where ranges are used and mixture-effect data are absent, hazard descriptions must reflect the highest concentration of each ingredient**. See dedicated `REACH_SECTION3_DISCLOSURE_ENGINE.md`.
- **3.2.3** Provide component CLP categories and H/EUH codes, full text in §16 if abbreviated, available SCL/M-factors/ATEs; for **non-classified** listed components, explain *why* they appear. For component nanoform, include appropriate particle characteristics dependent on registration/DU CSR status.
- **3.2.4** Names, identifiers and registration number where available; special conditional omission and 7-day forwarding obligations; verify any Article 24 CLP alternative-name permission before hiding identities.

### Sections 4–7 (pp.127–131)
- **4.1–4.3** Route-specific immediate first aid, delayed symptoms, immediate treatment needs and responder protection where appropriate; link §§2, 8, 11.
- **5.1–5.3** Suitable/unsuitable media, product/fire-decomposition hazards, firefighter protection; link §§9/10.
- **6.1–6.4** Differentiate non-emergency and emergency responders; containment, environmental protection, suitable cleanup and appropriate cross-references; link §§8/12/13.
- **7.1–7.3** Handling (including hygiene, emission control), storage/incompatible materials, end-use-specific recommendations; align identified uses and ES data, §§8/10.

### Section 8 (pp.131–133)
- **8.1.1** Provide **national** OEL/biological limit values currently applicable in the target Member State, their legal basis and relevant notations; do not pass an EU-level limit directly off as the national legal limit without confirming transposition. **8.1.2** Relevant monitoring procedures, **8.1.3** limits for contaminants formed during use, **8.1.4** relevant DNEL/PNEC where CSA/CSR required or data available, **8.1.5** control-banding constraints where used.
- **8.2** Exposure controls unless an attached ES contains the relevant information; include engineering measures matched to §1.2 uses, details of protective equipment, and environmental controls. Glove **material and thickness** and typical/minimum **breakthrough times** must be considered; respiratory protection specifies suitable type and filters/cartridge/mask if relevant; eye/face and protective clothing must be use- and exposure-specific. Do **not** invent vendor-specific glove validation, breakthrough or legal OELs. A short approved phrase can still fail §8.2 information completeness.

### Section 9 (pp.133–140)
- **9.1** Do not equate 'no classification' with 'not applicable'. Record each relevant property separately: physical state, colour, odour, melting/freezing, boiling, flammability, LEL/UEL, flash point, autoignition, decomposition, pH, kinematic viscosity, solubility, log Kow, vapour pressure, density, relative vapour density, particle characteristics. See pp.134–137 for exact scope and exceptions. Required missing/N/A properties need explicit status and reasons where possible. Property method/temperature/units, substance vs mixture, and physical state can determine applicability. The colour may be **'various' for mixture variants** under p.134 if appropriate; do not generalise this exception to all differing properties.
- **9.2** Other physical-hazard/safety characteristics relevant to safe use; separate screening from §9.1 (pp.137–140).

### Sections 10–12 (pp.140–147)
- **10.1–10.6** Reactivity, stability, hazardous reaction potential, conditions to avoid, incompatible substances, decomposition products. For mixture without measured data, substance data may be relevant but identify what applies to which substance; §10.1.2 p.141.
- **11.1** Information for each relevant CLP human-health hazard class/differentiation, whether classified or not, with data-based reasoning and route-specific effects. Do not claim 'not toxic' merely because mixture does not meet classification. **11.2** Other hazards, especially endocrine health effects where relevant. See pp.141–144.
- **12.1–12.7** Ecotoxicity, persistence/degradation, bioaccumulation, soil mobility, PBT/vPvB results, endocrine environment effects, other effects. Where data are ingredient-level rather than mixture-level, identify that. See pp.144–147.

### Sections 13–16 (pp.146–152)
- **13.1** Relevant waste management including product and packaging, treatment methods, sewer disposal warning and country context; waste codes require independent evidence.
- **14.1–14.7** UN/ID, shipping name, class, group, environment, precautions, *maritime bulk* conditional details. CLP hazard alone does not establish ADR/IMDG classification. Validate the actual transport regime. See pp.147–149.
- **15.1** Applicable Union/national provisions, REACH Title VII authorisation and Title VIII restriction status with specific affected uses/conditions, including relevant authorisation decision conditions/monitoring for downstream users; **15.2** whether supplier carried out a CSA. See pp.149–150.
- **16** Revision changes; acronym key, information sources, **mixture classification method(s) under CLP Article 9**, full H/P text not already written out; worker training advice where appropriate. See p.150.

## Mandatory phrase-selection bridge (LEGAL FACT → APPROVED PHRASE)

For each proposed sentence or structured value:
1. Find **applicable legal clause**, identify condition (`mandatory`, `mandatory_if`, `permitted`, `recommended_by_guidance`, `not_applicable`) and source PDF page.
2. Identify the **fact/evidence** that makes the clause applicable and any data still needed.
3. Retrieve **actual verified approved phrase** from linked notebook, with exact ID, version, jurisdiction, use, safety scope and text. A clause's factual requirement **does not authorise inventing stock wording**.
4. Evaluate content adequacy: does that phrase actually contain the required detail? Return `PHRASE_MATCHED_BUT_INCOMPLETE` if not.
5. For legally required identity, data, official statements and quantitative fields, use verified values and exact official wording as applicable (not discretionary prose).
6. Output a clean *working* SDS and a separate author-only legal/evidence/phrase audit trail; block issue if critical legal, product or phrase facts are unresolved.

## Explicit conflict resolution

- Binding REACH Annex II text outranks ECHA 2020 guidance and the REF-11 2024 report on legal duties. Newer applicable law outranks a 2026 snapshot.
- ECHA guidance is used for interpretation when consistent; REF-11 for inspection-priority patterns, *not* legal triggers.
- Phrase bank is only an approved **writing vocabulary**; it cannot relax disclosure thresholds, remove legal fields, or overrule tested product facts.
- If a phrase is unsuitable, do not force it. Put an approved-phrase gap or an evidence gap in the author-only issue register.
