# REACH Annex II authoring map — write the specified SDS, not other regulatory outputs

This checklist reflects the supplied 22 June 2026 REACH Annex II consolidation, particularly Part B pp.150–152 and Part A pp.117–150. Before issuing an SDS, verify the applicable version, market and national requirements. Numbered headings shown below are the default legal structure. For a **substance** use 3.1; for a **mixture** use 3.2. Do not silently leave applicable subsections blank; use a transparent working-draft gap where evidence is missing. Section 16 has no prescribed first-level number.

## Complete heading scaffold

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
  3.1. Substances [substance only] / 3.2. Mixtures [mixture only]
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
```

## Writing requirements, by section
| Section | Product-specific writing input | Important drafting guardrail |
|---|---|---|
| 1 | Identity; specified uses; supplier contact; actual emergency service | Verify Member State, service hours/conditions and conditional UFI/nanoform content. |
| 2 | Validated whole-product CLP endpoint conclusions and real label elements | Don't derive classification or label P-statements from raw ingredients by guess; separate 2.3 hazards. |
| 3 | Ingredient identity, percentages/ranges, CLP details, special limits/status | Apply `SECTION3_WRITING.md` **independently** of whole-mixture classification contribution. |
| 4 | Evidence of relevant exposure routes, first aid, acute/delayed effects | No unsafe generic first aid; 4.1–4.3 distinct. |
| 5 | Fire characteristics, suitable/unsuitable media, products of combustion | Check actual state/reactivity; do not assume water is suitable. |
| 6 | Physical form, incident scale, spill hazard, PPE, drains/soil, method | Cleanup and PPE must align 8 and waste advice in 13. |
| 7 | Identified work/use conditions, ignition, storage, incompatibility | Phrase choice from hazards **and actual use**, not hazard class alone. |
| 8 | EU/Member State OEL, DNEL/PNEC where applicable, engineering control and PPE test evidence | Detail appropriate to actual material/contact scenario, including glove performance. |
| 9 | Actual test/specification property results, state, methods/conditions | Address all §9.1 items and relevant §9.2; unavailable is not N/A. |
| 10 | Stability, incompatible substances, hazardous reaction/decomposition evidence | Product-specific chemistry; no unsupported blanket stability claims. |
| 11 | Health endpoints, route, mixture vs constituent data, other hazards | Do not say ‘no data’ and ‘not toxic’ interchangeably. |
| 12 | Ecotoxicity, degradability, mobility, PBT/vPvB, ED, other harms | Source mixture vs constituent evidence; align 2, 6, 13. |
| 13 | Waste streams, packaging, treatment method, national waste context | Do not invent waste catalogue codes. |
| 14 | Independent mode-specific dangerous goods determination | Do not treat CLP output as an ADR/IMDG/IATA assessment. |
| 15 | Verified applicable legal status and CSA info | Specific use and current legal status required. |
| 16 | Data sources, abbreviation explanations, full statements, change description, classification method from validated source | Do not call methodology verified if none was supplied. |

### Section 9.1 full sub-property check
Physical state; colour; odour; melting/freezing point; boiling point/initial boiling point and range; flammability; lower/upper explosion limits; flash point; auto-ignition temperature; decomposition temperature; pH; kinematic viscosity; solubility; partition coefficient n-octanol/water (log value); vapour pressure; density and/or relative density; relative vapour density; particle characteristics. Include relevant 9.2 other safety characteristics. Check units, temperature, test method, measurement versus estimate, substance versus mixture and justified unavailable/non-applicable status. For detailed legal qualifiers inspect REACH Annex II §9, not the list alone.
