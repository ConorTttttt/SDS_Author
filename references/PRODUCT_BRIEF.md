# Product information checklist for EU SDS authoring

Provide what is known. Unknown fields should remain explicitly unknown. Do not infer values from trade names or generic product families.

## Document & regulatory context
- Product identifier / SKU / supplier name and contact information
- Target EU/EEA Member State(s) and SDS language(s)
- SDS issue/revision date; earlier SDS revision and change log
- Substance / mixture; industrial / professional / consumer uses; relevant sector
- Whether product was placed on market before any relevant transitional date
- Connected approved phrase notebook name and version/date

## Classification and components
- Verified mixture/substance CLP classification, hazard categories, H/EUH statements, source and regulatory version; label elements / P-statements if independently validated
- Full internal formulation (if available), with ingredients' CAS, EC and other identifiers, ranges, concentrations, classifications, SCLs, ATEs, M-factors, and evidence/version
- Relevant Section 3 disclosure facts, including occupational exposure limits, SVHC, PBT/vPvB, endocrine-related or other legally applicable triggers
- Any UFI or additional label requirements where relevant; whether data are approved for publication

## Properties, risks and controls
- Physical state, colour, odour, melting/freezing point, initial boiling point, flash point, flammability, lower/upper explosion limits, auto-ignition temperature, decomposition temperature, pH and its conditions, kinematic viscosity, solubility, partition coefficient, vapour pressure, density/relative density, particle characteristics when relevant, and known non-applicable parameters with reasons
- Foreseeable exposure, handling operations, temperatures, aerosols/mists/dust generation, ventilation, PPE, hygiene, occupational exposure limits
- First-aid, firefighting, accidental release, storage incompatibilities and stability evidence
- Toxicological and ecotoxicological information, PBT/vPvB and endocrine-related assessments where required, mobility/degradability/bioaccumulation, disposal and waste information
- Transport classification evidence for ADR/RID/ADN/IMDG/ICAO-IATA, and any specific applicable exclusions/conditions
- Regulatory restrictions/authorisations and exposure scenarios if applicable

## Evidence quality
For each major claim, record: source document, version/date, section/page or field, owner, and whether verified. Missing numeric fields remain `not supplied`, not `not applicable` by default.

## v2 evidence ledger and authoring dossier
When the user submits a partial set of product facts, proceed as far as evidence allows; do not require the entire checklist just to recommend one subsection's phrases. Store each used input with: `fact_id, parameter, value, unit, test conditions/method (if relevant), data source, effective date, reviewed by, confidence, confidentiality, applicable target markets`.

**Per-ingredient regulatory impact record** (important for SDS Section 3 and safe-use phrasing):
- `ingredient_id` and verified CAS/EC/REACH identifiers, name and concentration or controlled concentration range.
- Hazard class(es), H/EUH statement codes, exact SCLs, ATEs (with route) and M-factors where known.
- Actual impact on **mixture classification** (`contributes`, `below applicable cutoff`, `aggregate-method component`, `not assessed`, etc.), keeping it separate from whether classification is present.
- Whether **Section 3 disclosure** is triggered (with legal basis and applicable cutoff), **OEL** relevance, PBT/vPvB/endocrine status, **EUH** effects and **safe-use** relevance.
- Evidence documents + expiry/review date and outstanding uncertainty. **Do not assume a component below a classification cutoff has no SDS relevance.**

**Required contextual fields** for meaningful recommendations: available product tests and their conditions, processing conditions (temperature, aerosolisation, dust generation), realistic exposure routes/controls, intended use/recipient, transport modes and packaging when relevant, and Member State-specific OEL/emergency/regulatory information. Set `NOT_DETERMINED` where assessment not made.

**External approval control**: final SDS signoff owner, issue date/version, approval record and changed sections. Gemini never supplies this approval itself.

## V3: REF-11-sensitive product evidence requests

Request these extra inputs *only as needed for the user's selected sections*:
- §1: actual label/product identifier, placement-on-market/use and packaging conditions relevant to UFI, final supplier chain contact, target country emergency service and availability.
- §2/§3: source-verified full classification and label, every reportable ingredient and its identity, hazard codes, available **route-specific ATE / SCL / M-factor**, disclosure threshold rationale and any applicable authorisation decision/use.
- §8.1: each OEL's **destination country, legal source/version, units, notation and type**; don't assume values transfer between markets.
- §8.2: workplace/process conditions, routes of exposure, engineering controls, glove compatibility **material/thickness/breakthrough** support, respirator type/selection evidence, environmental-release controls. Do not infer detailed PPE performance from generic hazard classes.
- §9.1/9.2: data provenance, test methods and conditions, reasons for nonapplicability or missing data, particle/nanoform characteristics where relevant, other physical hazards.
- Nanoform/ED: current regulatory basis and presence/status per relevant component, with special care about mixture §1.1 nanoform nuance and newer CLP hazard classes.
- §15/§16: current Member State legislation, restriction/authorisation terms, reviewed changes/version, classification method and acronym legend.
- Supply-chain compliance: actual sending/update history and ES annex/integration proof (not inferable from the content of an SDS PDF alone).

Use `references/REF11_ENFORCEMENT_QA.md` to decide which product evidence must be collected before selecting or validating each phrase.

## V4 optional formulation group assessment fields

For `MULTI_PRODUCT_COVERAGE`, supply a product list with each unique product ID, formulation revision, concentration ranges, ingredient disclosures, CLP classification/label, pH/flash point/viscosity/colour/state, exposure/handling/storage/PPE, intended uses, markets/languages, transport status and authorisation/restriction checks. The `REACH_MULTI_PRODUCT_SDS_COVERAGE.md` matrix must return per-product section coverage, not just a family-level Yes/No.
