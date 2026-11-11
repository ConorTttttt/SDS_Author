# ECHA Section-by-section authoring playbook (v4.0, December 2020)

This is an **authoring decision aid**, summarising the uploaded ECHA *Guidance on the compilation of safety data sheets*, pages cited below (printed PDF page numbers). It is **not** a replacement for REACH Annex II as applicable on the issue date and not a source of user-approved phrases. The ECHA document reproduces explanatory examples and 2020-era legal passages, which **must not be assumed current by default**. For each section: decide what information is needed, collect product-specific evidence, then search only the user's approved-phrase notebook for permitted wording.

## Global design principles — ECHA pp. 13–32
- **Competence and accountability (pp. 13–15, 29):** supplier retains responsibility; a competent person prepares and reviews, even when using software or an outside service. Phrase catalogues can aid clarity but do not automatically ensure accuracy.
- **Structure and completeness (pp. 16–17):** use REACH Annex II Part B's prescribed 16 section names and subsection numbers. All applicable subsections contain information, a reasoned non-applicability statement or explained unavailability; only subsection 3.1 or 3.2 may be omitted as appropriate to substance/mixture. A 16-heading-only template is insufficient.
- **Source and scope of SDS obligations (pp. 8–9, 22–26):** check Article 31(1), 31(3), 31(4), exceptions, and other applicable circumstances. “Mixture not classified” does NOT equal “SDS never needed.” Evaluate target recipients and relevant Member State language (pp. 21–22).
- **Revision and supply (pp. 17–21):** verify triggers under Article 31(9), revision date and affected customers; manage changes in Section 16, date and superseded versions; note obligations to proactively supply rather than merely host.
- **Exposure scenarios (pp. 26–29 and Appendix 1 pp. 121–127):** obtain information from upstream scenarios and CSR; account for conditions when attaching ESs versus integrating safe-use information; do not quietly discard ES-driven controls.
- **Iterative preparation and checking (pp. 19–20):** ECHA Figure 1 links identity → components → hazard-property evidence → transport/regulation → exposure/handling → emergency measures → disposal → changes → final Section 2. Treat as a useful workflow, not a mandated output order.

## Section 1 — Identification (ECHA pp. 33–40; REACH Annex II Part A §1)
**1.1 Product identifier:** match label and applicable REACH registration identifiers; consider UFI where required/appropriate under CLP Annex VIII; nanoform identification if relevant. Do not assume every mixture needs a UFI or that UFI always belongs on the SDS; conditions depend on packaging and market context.
**1.2 Relevant identified uses and uses advised against:** state recipient-relevant uses concisely and reasons for advised-against uses where applicable; align with CSR/ES. Don't hallucinate forbidden uses.
**1.3 Supplier:** full supplier name/address/telephone and SDS-competent-person email; responsible person details if applicable. A distributor providing a supplier SDS still has supplier-contact duties.
**1.4 Emergency telephone:** accurate service and correct limitations (hours, language, medical-only line, timezone), matched to country. Do not invent a national poison-centre contact.
**Approved phrases needed:** identified uses, use restrictions, contact-service limitations if present in notebook; identifiers and verified contact details are factual fields.
**Checks:** SDS version/date; label identity; UFI/PCN status; Member State/language; supplier address; emergency service legitimacy and hours.

## Section 2 — Hazards identification (ECHA pp. 41–46; Annex II §2)
**2.1 Classification:** exact validated product CLP classification or explicit non-classified determination; source/date and calculation methodology traceable, full text in §16 where abbreviations used. Review key adverse effects against §§9–12.
**2.2 Label elements:** actual applicable CLP label content — pictograms, signal word, hazard and supplemental hazard statements, selected precautionary statements and any applicable extra elements; ensure matches the verified label. Do NOT mechanically paste all possible P-statements from H-code mappings. ECHA pp. 43–45 discuss selected label P-statements and explain why the usual six-statement **label** limit is not a universal limit on SDS advice.
**2.3 Other hazards:** PBT/vPvB, endocrine-related information where applicable under the verified current legal text and thresholds; non-classified hazards such as dust explosion, oxygen displacement or processing emissions when evidenced. Avoid 'no other hazards' merely because no CLP classification.
**Checks:** source CLP version/date; 2.1 vs 11/12; §2.2 vs label; EUH inclusion; non-classified risks vs handling/storage; PBT/ED facts vs §3/§11/§12.

## Section 3 — Composition/information on ingredients (ECHA pp. 46–57; Annex II §3)
**3.1 Substances:** main constituent/identity; classified relevant impurities/stabilisers as applicable; SCL, ATE, M-factor where available/applicable; nanoforms if relevant.
**3.2 Mixtures:** apply separate Annex II substance-disclosure rules for **classified mixtures** and **non-classified mixtures**. Consider identities, appropriate concentration or ranges, CLP classifications, relevant EUH, EC/REACH identifiers, SCL, ATE, M-factor, nanoform, and reporting triggered by hazard class, SCL, M-factor-adjusted thresholds, OEL, PBT/vPvB, SVHC and endocrine-related status under applicable law. Do not use one universal 1% rule or assume mixture classification drives all disclosures.
**Concentration ranges:** ECHA p. 51 states that in the absence of mixture-level effects, hazards described using ranges should account for highest ingredient concentrations; consult applicable Annex II and actual classification engine for exact rules. Do not disclose confidential full formulation where lawful SDS ranges suffice, and do not hide legally reportable ingredients.
**Evidence table per ingredient:** CAS/EC/index/REACH ID, composition concentration/range + basis, hazard class/categories, SCL/M-factor/ATE, EU OEL, status flags, threshold applied, source and date, `classification_contribution` / `sds_disclosure_trigger` / `safe_use_relevance` separately. Ingredient can be reportable for a reason other than affecting the mixture's classification.
**Checks:** 3 vs 2, 8.1 (OEL), 11/12, 15; mixture vs substance selection; classification status; conflicts between provided composition and disclosed ranges.

## Section 4 — First aid (ECHA pp. 57–59; Annex II §4)
**4.1** first aid by exposure route: inhalation, skin, eye, ingestion; self-protection of first aider and any necessary immediate action; only advice suitable for actual product and evidence.
**4.2** most important acute and delayed symptoms/effects, not generic 'no symptoms known' without basis.
**4.3** immediate medical attention, special treatment, relevant delayed monitoring or antidotes when supported; distinguish actions for lay first-aider and physician.
**Inputs:** acute/corrosive/sensitising hazards, solvent aspiration risk, pH and other effects, credible component data. Cross-check §2, §8, §11.

## Section 5 — Firefighting (ECHA pp. 59–61; Annex II §5)
**5.1** suitable and **unsuitable** media with product-specific reasons (e.g. reactive with water or spreading liquid).
**5.2** special hazards from combustion and fire proximity, decomposition products, potentially hazardous reactions.
**5.3** firefighter PPE, respiratory protection and containment advice where supported.
**Inputs:** ignition/flash point and flammability, oxidising/reactive traits, fire scenarios, incompatible media. Cross-check §7/§9/§10/§14; do not infer non-flammability from missing flash point.

## Section 6 — Accidental release (ECHA pp. 61–63; Annex II §6)
**6.1** distinguish non-emergency and emergency responder precautions; PPE, ignition control, evacuation, ventilation, inhalation/skin exposure, dust/mist risk.
**6.2** environmental precautions: drains/soil/water and actions proportionate to the material.
**6.3** containment and cleaning/neutralisation/absorbents/collection, including methods not to use; distinguish large/small spills if needed.
**6.4** references to other sections, particularly §8/§13.
**Checks:** ecological statements vs §12; disposal handling vs §13; spill PPE vs §8; high pH/reactivity vs cleanup method.

## Section 7 — Handling and storage (ECHA pp. 63–68; Annex II §7)
**7.1** safe handling by identified use: prevent ignition, aerosol/dust formation, environmental release, incompatible processes and occupational hygiene; do not add incompatible 'avoid' restrictions without evidence.
**7.2** storage conditions consistent with §§9/10: temperature, sunlight/humidity, ventilation, container/packaging compatibility, quantities, static/ignition sources, segregation, stabilisers where relevant.
**7.3** identified specific end use(s) and applicable sector-specific instructions; align §1.2 and received ESs.
**Checks:** use scenario, handling environment and exposed users; §8 controls; concentration/physical form; storage compatibility vs §10.

## Section 8 — Exposure controls/personal protection (ECHA pp. 68–77; Annex II §8)
**8.1** applicable workplace exposure limit values (Union and relevant Member State), biological limit values, DNELs/PNECs where relevant and supported, exposure monitoring methods/context. An ingredient can be Section 3 listed because of an OEL even absent mixture hazard classification; national-only OEL can influence controls even where §3 obligation differs.
**8.2** engineering/technical controls, suitable respiratory/hand/eye/skin protection and environmental exposure controls; products, materials, performance/standards and breakthrough times only if justified. Do not automatically recommend disposable gloves or a specific respirator solely because an H statement exists. Different use and exposure scenarios may require different controls.
**Checks:** OEL tables vs §3, physical state/vapour/mist risk vs §9, use vs §1.2/§7, PPE consistency with §4/§6/§11 and ES.

## Section 9 — Physical and chemical properties (ECHA pp. 77–93; Annex II §9)
**9.1** record each required physical/chemical property from the legally applicable schedule: physical state, colour, odour, melting/freezing, boiling/range, flammability, explosion limits, flash point, auto-ignition, decomposition, pH, kinematic viscosity, solubility, partition coefficient, vapour pressure, density/relative density, relative vapour density and particle characteristics where relevant. Preserve proper units, reference temperature, conditions, method and mixture-vs-ingredient basis.
**9.2** additional relevant hazard-class properties and other safety characteristics. A missing property is **not** equivalent to a negative test, safe result or non-applicability. ECHA p. 78 explicitly distinguishes lack of relevance, lack of data and actual negative results. Some items are substance/physical-state specific; give a reason when a requested field cannot apply (e.g. the guide notes flash point does not apply to gases, aerosols or solids).
**Checks:** 2/5/7/10/14 consistent with actual values and methods; do not invent common-looking default values.

## Section 10 — Stability and reactivity (ECHA pp. 93–97; Annex II §10)
**10.1** reactivity; **10.2** chemical stability under ordinary/proposed storage; **10.3** possible hazardous reactions; **10.4** conditions to avoid; **10.5** incompatible materials; **10.6** hazardous decomposition products. Treat stability as condition-specific. Distinguish normal conditions from fire situations and only mention substantiated reactions.
**Checks:** pH/solvent/water-reactivity §9; incompatibilities and storage §7; decomposition in fire §5.

## Section 11 — Toxicological information (ECHA pp. 97–103; Annex II §11)
**11.1** information on CLP hazard classes/endpoints; routes, symptoms and related acute/delayed effects; meaningful product-specific evidence and mixture/substance basis; avoid declaring absence of effects on insufficient data.
**11.2** information on other hazards, including endocrine-related health effects if applicable under current Annex II. Link source and applicability, not arbitrary mechanistic assertions.
**Checks:** 2.1/2.3 and §3 ingredients, §4 first aid, §8 controls. Where the guide predates later CLP hazard classes, **verify current legal scope separately**.

## Section 12 — Ecological information (ECHA pp. 103–109; Annex II §12)
**12.1** toxicity; **12.2** persistence/degradability; **12.3** bioaccumulative potential; **12.4** mobility in soil; **12.5** PBT/vPvB assessment; **12.6** endocrine disrupting properties; **12.7** other adverse effects. Document mixture versus ingredient evidence and justify absent/not-applicable data; avoid asserting environmental harmlessness merely because mixture is not CLP-classified.
**Checks:** 2.1/2.3, §3 status, §6 environmental release prevention, §13 disposal, §14 marine pollutant/environmental hazards.

## Section 13 — Disposal considerations (ECHA pp. 109–111; Annex II §13)
**13.1** safe treatment of product and contaminated packaging, including process restrictions and sewage disposal as applicable. Waste codes need legally and contextually supported classification (intended waste stream and local practice matter); do not hallucinate a European List of Waste code for every chemical product.
**Checks:** environmental characteristics §12 and handling §6/§7; container type and residues; waste versus unused product.

## Section 14 — Transport information (ECHA pp. 111–115; Annex II §14)
**14.1** UN number or ID number; **14.2** UN proper shipping name; **14.3** transport hazard class(es); **14.4** packing group; **14.5** environmental hazards; **14.6** special precautions for user; **14.7** maritime transport in bulk according to IMO instruments. Consider actual ADR/RID/ADN, IMDG and air transport regimes, as applicable; different modes can differ. If not applicable, verify and explain; no UN number may be inferred solely from CLP physical hazard categories.
**Checks:** independent transport input + flash point and other §9 data, hazardous properties and §2/§12; packaging, quantity, shipping mode and revisions.

## Section 15 — Regulatory information (ECHA pp. 115–118; Annex II §15)
**15.1** specific relevant EU and **target Member State** safety/health/environment legislation and required operational implications; restrictions/authorisations and statuses where factually verified; do not transcribe outdated example law names uncritically. The guidance p.117 emphasises that national regulatory information **cannot simply be translated** from one Member State's SDS to another.
**15.2** whether chemical safety assessment has been carried out; verify supplier/registrant facts, never automatically claim no CSA.
**Checks:** target market, supplier/regulatory obligations, Section 1 use, restrictions and ES; status current as of publication date.

## Section 16 — Other information (ECHA pp. 118–120; Annex II §16)
No mandatory numbered first-level subsections under Annex II Part B, unlike 1–15. Include when relevant: revision details and replaced version; acronyms/abbreviation legend; data references; mixture classification evaluation method under CLP Article 9; full H/EUH/P statement texts not written out elsewhere; worker-training advice. Can provide ES index if helpful. Explain the classification method for hazardous endpoints without inventing methodology or rerunning classification. Disclaimers do not relieve Annex II compliance.
**Checks:** revision data vs page 1; Section 2/3 abbreviations/H statements vs full texts; exposure scenario cross-references; classification method provenance.

## Baseline decision principle
For each subsection record `REQUIREMENT | PRODUCT_FACTS | UNCERTAINTY | APPROVED_PHRASE_IDS | WHY_SELECTED | WHY_NOT_SELECTED | LEGAL_SOURCE_VERIFICATION | HUMAN_REVIEW_STATUS`. No required subsection can be justified solely by a pleasant-sounding stock phrase.
