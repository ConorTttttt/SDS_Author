# Recommended approved-phrase notebook design

## Notebook concept
Name the attached notebook **EU SDS — Approved Phrases** and add one or more structured documents/tables. Keep regulatory text and drafting phrase approvals distinguishable. A notebook is a retrieval source, not an authoritative rule engine or a guarantee that a particular entry was retrieved. The human-maintained master phrase library should remain version-controlled outside the model.

## Minimum per-phrase record
Store one entry per phrase or per approved alternative with fields:

| Field | Meaning |
|---|---|
| phrase_id | Stable unique ID, never reused for different meaning |
| wording | Exact approved English phrase, including authorised placeholders |
| approval_status | APPROVED / DRAFT / RETIRED |
| version | Version or approval date and owner |
| jurisdiction | EU/EEA and explicit exclusions if any |
| language | e.g. en |
| section | SDS section, e.g. 7 |
| subsection | SDS subsection, e.g. 7.1 |
| topic/tags | e.g. handling, eye contact, solvent, aerosol, strong alkali |
| applies_when | Explicit evidence-based inclusion conditions |
| excludes_when | Explicit exclusion/conflict conditions |
| required_inputs | Facts needed for a responsible decision |
| regulatory_basis | Article/Annex citation if relevant; distinguish mandatory vs guidance |
| approved_source | Owner, provenance or approval record |

Optional useful fields: `chemical_family`, `physical_form`, `intended_use`, `hazard_classes`, `ingredient_hazards`, `temperature_or_process_conditions`, `companion_phrase_ids`, `mutually_exclusive_group`, `placeholder_rules`, `product_scope`, `retirement_reason`, `replacement_id`, `last_reviewed`, `jurisdiction_version`.

## Example record: STRUCTURE ONLY — NOT AN APPROVED PHRASE

```yaml
phrase_id: EXAMPLE-7-001
wording: "[VERBATIM APPROVED WORDING WOULD GO HERE]"
approval_status: DRAFT
version: "0.0-example"
jurisdiction: EU/EEA
language: en
section: 7
subsection: "7.1"
topic: "Handling"
applies_when: "Only when documented conditions are met"
excludes_when: "When a product-specific contradiction exists"
required_inputs: ["physical state", "intended use", "relevant hazards"]
regulatory_basis: "Verify precise REACH Annex II subsection if cited"
approved_source: "Example - not for use"
```

**Do not upload the example as if it were part of the actual approved phrase collection.**

## Important notebook quality controls
- Do not mix unapproved or obsolete phrases in the same notebook unless approval status is machine-readable and every selection checks it.
- If the master list lives in spreadsheets, use a searchable table export with one row per phrase and unambiguous labels; in addition keep a readable per-section index.
- Do not rely only on H-code matching: physical properties, intended use, supplier evidence and component hazards affect suitability.
- Include phrase IDs in the text of entries so retrieval can return an auditable identifier.
- Regulatory sources are separate from phrase approval. A regulatory quote is not automatically an approved discretionary phrase.
- When notebook retrieval appears incomplete, treat results as a candidate list, never as proof that no other phrase exists.

## v2 guidance-inspired upgrade — phrase selection eligibility
Treat the phrase library as a **read-only repository of approved wording**. Each phrase may cover *zero, one, or multiple* specific product scenarios; a Section 7.1 topic tag is not a sufficient eligibility condition. Add the following fields where your data structure permits (none should be fabricated at selection time):

| Extra field | Use |
|---|---|
| `approval_owner` / `approval_date` | Whose approval and which controlled revision authorises verbatim use. |
| `phrase_checksum` | Optional method for independently checking the exact approved words have not been altered. |
| `legal_vs_guidance_vs_internal` | Separate legal text obligations from guidance suggestions and company authoring preferences. |
| `hazard_endpoint` | More precise classification/mixture endpoint instead of only an H-code tag. |
| `component_hazard_relevance` | Can apply even if mixture is not classified at the same endpoint. |
| `measurable_trigger` | pH, flash point, viscosity, physical form, particle generation, dilution/use, exposure conditions, actual OEL, etc. |
| `scope_required_inputs` | Evidence needed before use (e.g. supported ventilation assessment for respiratory-protection claim). |
| `data_state_compatibility` | Compatible with supported positive/negative values, explicit no-data or non-applicability. |
| `selection_priority` | Help choose between precise and generic expressions without violating other conditions. |
| `exclusion_group` | Phrases that may not coexist (e.g. mutually contradictory storage conditions). |
| `companion_phrases` | Another phrase needed to avoid incomplete or misleading advice. |
| `applies_as_of` / `retires_as_of` | Time-bounded validity independent of SDS issue date. |
| `approved_variables` | Names, units, value sources, permitted formats and any allowed punctuation around placeholders. |

### Required retrieval behaviour in Gemini
1. Search the attached notebook by `section + subsection + subject`, then by `hazard endpoint`, `component hazard`, `physical state`, `use`, and likely exclusions. Do not assume a global semantic search returns every eligible entry.
2. Before showing a phrase, retrieve the **record itself** and verify exact wording, ID, approval/version and all required applicability fields; if a search result only gives a summary or shortened quote, mark `CONDITIONAL: EXACT APPROVED TEXT NOT VERIFIED`.
3. Where a phrase depends on missing evidence, classify it as `CONDITIONAL`, never present it as a selected sentence in the clean SDS body.
4. Where a phrase is plausible but contradicted by values or another approved phrase, classify as `EXCLUDED` and say why.
5. Notebook retrieval is probabilistic. Report `NO VERIFIED MATCH RETRIEVED`, not a definitive assertion that the master database contains no applicable wording. For critical sections consider a deterministic source-of-truth CSV/export in addition to the notebook.
6. Keep official legally prescribed H/EUH/P statements separate from the stock-phrase library, with exact applicable legal texts from controlled official regulatory wording datasets or verified regulation. Never turn a guidance example into an approved entry.

### Example source chunk (template ONLY; not a phrase)

```text
[PHRASE_ID: <REAL_APPROVED_ID>]
APPROVAL_STATUS: APPROVED
LIBRARY_REVISION: <REVISION>
LANGUAGE: en
JURISDICTION: EU/EEA
SDS_SUBSECTION: 7.1
APPROVED_WORDING: <EXACT_TEXT_FROM_YOUR_LIBRARY>
REQUIRED_INPUTS: <LIST>
APPLIES_WHEN: <TESTABLE_CONDITIONS>
DO_NOT_USE_WHEN: <CONFLICTS>
APPROVED_PLACEHOLDERS: <IF_ANY>
SOURCE_RECORD: <MASTER_REFERENCE>
```

**Do not upload a template as an approved phrase source.** Use these field names to label real, reviewed entries.

## V3: phrase adequacy and REF-11 inspection metadata

Add **optional** control fields to the master phrase record (do not invent them for existing phrases):

- `ref11_qa_tags`: applicable `R11-XX` inspection-review IDs, such as `R11-13` for glove detail.
- `content_claims_covered`: narrowly identified content elements actually communicated by the approved text.
- `required_factual_companions`: data that must accompany wording when applicable (e.g. actual glove material, breakthrough conditions, OEL source, measured flash point).
- `only_valid_with_evidence_ids`: explicit product evidence types that must exist before selecting phrase.
- `plausibility_conflicts`: warnings and contradictory combinations to search for in Sections 2/3/8/9/11/12.
- `country_scoped_claim`: whether a phrase assumes a country-specific OEL, emergency number, regulatory restriction or local waste requirement.

Selection now has **four distinct outcomes**: (1) `APPROVAL_VERIFIED` (exact wording matches controlled library); (2) `ELIGIBILITY_VERIFIED` (facts support use); (3) `CONTENT_COVERAGE_VERIFIED` (required elements actually covered); (4) `RELEASE_NOT_GRANTED` pending SDS competent-person approval. An APPROVED phrase may fail (2) or (3); **do not alter or discard that distinction**. When incomplete, ask for factual data or additional approved text; never make up detailed glove/PPE specifications simply to pass a REF-11 check.

For a `RECOMMEND` table include optional `ref11_qa_tags` and `unmet_content_requirements` columns when relevant. The report's stock examples and questionnaire wording are **not** approved phrases by virtue of appearing in `sources/`.

## V4 phrase-to-requirement coverage (do not alter existing approved phrases)

The authoring skill needs the following **external metadata**, derivable as a separate mapping table if your phrase notebook cannot be edited. These are *not* new approved phrases: `REACH_ANNEXII_CLAUSE`, `CONDITION_FOR_USE`, `PHRASE_COMPLETENESS_SCOPE`, `NEEDED_FACTS`, `COMPANION_FIELDS_REQUIRED`, `PRODUCT_VARIANT_ELIGIBILITY`, `EXCLUSIONS`, `VERIFIED_ON`, and `LEGAL_VERSION`. A phrase may be approved and **still insufficient** to satisfy a clause (e.g., "Wear chemical-resistant gloves" vs §8.2.2.2 glove material/thickness/breakthrough). Report `PHRASE_MATCHED_BUT_INCOMPLETE` and request validated values/approved companion text rather than embellishing the phrase. If the notebook cannot reliably return an exact ID/text, mark `RETRIEVAL_NOT_VERIFIED` and do not manufacture one.
