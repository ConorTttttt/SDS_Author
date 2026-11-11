# EU SDS structure, data-state definitions and release gates

**Now verified against supplied REACH Annex II Part B, consolidated 22 June 2026, PDF pp.150–152 (subject to applicable-date/OJ verification). Prior baseline source:** ECHA *Guidance on the compilation of safety data sheets*, v4.0 (December 2020), §§2.6–2.12 pp.16–20, §§3.1–3.16 pp.33–120. **Legal source to verify:** REACH Annex II, Part A and Part B, as amended/applicable on the SDS issue date. This is a checklist, not a claim that the 2020 guidance reflects all amendments in 2026.

## Exact section heading + subsection skeleton (REACH Annex II format)

```text
SECTION 1: Identification of the substance/mixture and of the company/undertaking
  1.1. Product identifier
  1.2. Relevant identified uses of the substance or mixture and uses advised against
  1.3. Details of the supplier of the safety data sheet
  1.4. Emergency telephone number
SECTION 2: Hazards identification
  2.1. Classification of the substance or mixture
  2.2. Label elements
  2.3. Other hazards
SECTION 3: Composition/information on ingredients
  3.1. Substances                         [for a substance only]
  3.2. Mixtures                           [for a mixture only]
SECTION 4: First aid measures
  4.1. Description of first aid measures
  4.2. Most important symptoms and effects, both acute and delayed
  4.3. Indication of any immediate medical attention and special treatment needed
SECTION 5: Firefighting measures
  5.1. Extinguishing media
  5.2. Special hazards arising from the substance or mixture
  5.3. Advice for firefighters
SECTION 6: Accidental release measures
  6.1. Personal precautions, protective equipment and emergency procedures
  6.2. Environmental precautions
  6.3. Methods and material for containment and cleaning up
  6.4. Reference to other sections
SECTION 7: Handling and storage
  7.1. Precautions for safe handling
  7.2. Conditions for safe storage, including any incompatibilities
  7.3. Specific end use(s)
SECTION 8: Exposure controls/personal protection
  8.1. Control parameters
  8.2. Exposure controls
SECTION 9: Physical and chemical properties
  9.1. Information on basic physical and chemical properties
  9.2. Other information
SECTION 10: Stability and reactivity
  10.1. Reactivity
  10.2. Chemical stability
  10.3. Possibility of hazardous reactions
  10.4. Conditions to avoid
  10.5. Incompatible materials
  10.6. Hazardous decomposition products
SECTION 11: Toxicological information
  11.1. Information on hazard classes as defined in Regulation (EC) No 1272/2008
  11.2. Information on other hazards
SECTION 12: Ecological information
  12.1. Toxicity
  12.2. Persistence and degradability
  12.3. Bioaccumulative potential
  12.4. Mobility in soil
  12.5. Results of PBT and vPvB assessment
  12.6. Endocrine disrupting properties
  12.7. Other adverse effects
SECTION 13: Disposal considerations
  13.1. Waste treatment methods
SECTION 14: Transport information
  14.1. UN number or ID number
  14.2. UN proper shipping name
  14.3. Transport hazard class(es)
  14.4. Packing group
  14.5. Environmental hazards
  14.6. Special precautions for user
  14.7. Maritime transport in bulk according to IMO instruments
SECTION 15: Regulatory information
  15.1. Safety, health and environmental regulations/legislation specific for the substance or mixture
  15.2. Chemical safety assessment
SECTION 16: Other information
  [no mandatory numbered subsection headings; see content requirements]
```

**Critical:** This skeleton records the 2020/878-era requirements described in the uploaded guide. Before treating it as a legal checklist for an actual SDS, compare against current Annex II Part B and Member State provisions. Do NOT reproduce bracketed drafting notes in an issued SDS. Every relevant subsection must contain substantive information, a justified non-applicability statement or an explicit explanation of unavailable data. Section 3 needs only 3.1 or 3.2 (as appropriate); §16 has no mandatory subheadings. ECHA pp.16–17, 119.

## Controlled information states

| Status | Evidence and drafting consequence |
|---|---|
| `SUPPORTED_VALUE` | Actual value/text supported by a source, date and appropriate measurement/reporting context. |
| `SUPPORTED_NEGATIVE_TEST` | Documented test establishes a negative outcome under stated method/conditions; do not generalise beyond the method. |
| `NOT_AVAILABLE` | Relevant parameter is not documented or accessible; do not imply it is safe or inapplicable. Give reason if known. |
| `NOT_DETERMINED` | A scientific/regulatory assessment has not been performed; do not imply negative status. |
| `NOT_APPLICABLE_WITH_REASON` | The characteristic genuinely does not apply to the physical form/scenario or is legally inapplicable; document the reason. |
| `CONFLICT` | Different verified sources disagree, or approved phrase conflicts with evidence; withhold affected claim pending resolution. |
| `PENDING_VERIFICATION` | Source supplied but lacks date/method/approval or legislation check; block legally material claims. |

## Mandatory section-by-section authoring gates

**Gate 1 — Identify applicable regime:** Member State, language, product type, applicable REACH/CLP editions, relevant transition/placing-on-market data, Article 31 SDS obligation type and supplier status.

**Gate 2 — Validate product inputs:** composition + source; validated classification for substance/mixture; confirmed labels; physical, toxicological and eco data; national OELs and restrictions where relevant; transport independently classified. Do not treat a marketing specification as proof of safety.

**Gate 3 — Regulatory-content coverage:** verify current mandatory Annex II first-level headings and content; do not accept a phrase hit as proof of regulatory completeness. A blank section, a repetitive generic 'N/A' or 'not classified' in lieu of missing data fails.

**Gate 4 — Phrase eligibility:** exact notebook+ID+version, status APPROVED, jurisdiction, language, use-scenario, product-family, evidence conditions, exclusions, placeholders, mutually exclusive logic, retired replacement, optional companion phrases. On failed retrieval, say `NOT VERIFIED FOUND`, not conclusively `NO APPROVED PHRASE EXISTS`.

**Gate 5 — Cross-sectional assertions:** link all relevant claims. At minimum:

| Claim/check | Sections to cross-examine |
|---|---|
| Product identity, intended use, supplier, issue date, country, UFI | 1, 2, 3, 15, 16 |
| Hazard classification & component reporting independently | 2, 3, 8, 11, 12, 15, 16 |
| Skin/eye/respiratory/aspiration hazards and first aid | 2, 3, 4, 7, 8, 11 |
| Flash point, volatility, oxidising ability, fire and fire-related decomposition | 2, 5, 7, 9, 10, 14 |
| Spills, environmentally sensitive release, waste handling | 6, 7, 8, 12, 13, 14 |
| Chemical storage, incompatibilities and stability | 5, 7, 9, 10 |
| Exposure scenario operational conditions and RMMs | 1.2, 7, 8, SDS annex; 4/6 if implicated |
| Hazard/label P-statements and classification method | 2, 7, 8, 16, product label |
| Target Member State, exposure limits, restrictions and emergency details | 1, 8, 15 |

**Gate 6 — Issue/revision control:** first-page date/version/superseded revision, Section 16 change log, applicable language, actual label consistency, appropriate ES attachment/integration, accurate regulatory source register, signoff by trained competent person.
