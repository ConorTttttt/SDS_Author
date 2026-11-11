# Product dossier and evidence for EU SDS writing

Capture **only what is needed for the requested section(s)**; a full SDS needs broader evidence. The supplied `templates/product_dossier.json` is a starting shape, not a regulatory declaration.

## Fact record
`name/field | actual value | unit and test conditions | substance vs mixture scope | original document | revision/date | verifier | status | SDS subsection(s)`.

Controlled statuses:
- `SUPPORTED_VALUE`: traced measured/validated fact.
- `SUPPORTED_NEGATIVE_TEST`: specific test genuinely showed a negative result; do not generalise.
- `NOT_AVAILABLE`: absent/inaccessible data; do not imply no hazard.
- `NOT_DETERMINED`: assessment not performed.
- `NOT_APPLICABLE_WITH_REASON`: genuine non-applicability with rationale.
- `PENDING_VERIFICATION`: supplied but evidence/date/conditions unconfirmed.
- `CONFLICT`: sources, phrases or statements disagree.

Do not use bare `N/A` where the distinction matters. Do not infer physical properties, concentration limits, ingredient identities, toxicological safety, transport classification, emergency contact details or PPE performance.

## Required evidence classes for complete authoring
**Product/market:** substance or mixture, label identifier, REACH registration where applicable, identified uses, supplied form/concentration, EU Member States, language, SDS date/revision, supplier competent contact, emergency details and their limitations.

**Hazards/ingredients:** current verified whole-product CLP endpoint classification, actual label text, ingredient identities/concentration or valid ranges with basis, ingredient CLP classifications, SCL/M-factor/ATE when relevant and available, applicable Union and national OEL information, PBT/vPvB/SVHC/ED/nanoform information where relevant. Ingredient Section 3 eligibility requires independent Annex II assessment; do not confuse it with mixture classification contribution.

**Physical/chemical:** physical state, colour, odour, Section 9.1/9.2 properties with method, conditions, units and reasoned missing-data statuses. Storage compatibility and stability require actual chemistry/product evidence.

**Exposure/emergency:** handling settings, worker/consumer use, inhalation/skin/eye routes, engineering control/ventilation evidence, glove material/thickness/breakthrough suitability, respiratory filtration type, tested first-aid/fire/spill guidance and exposure scenario information when relevant.

**Impact/other sections:** toxicology and ecological evidence (whole mixture vs ingredient), disposal/packaging and waste classification inputs, independently established applicable transport classifications by mode, regulatory statuses and revision sources.

## Priority conflict questions
- Does the supplier or sample SDS describe **a different product concentration, formulation or market**?
- Is the CLP classification dated and validated, and does Section 2 reflect the real label?
- Are flash point, pH, viscosity, solubility and stability backed by actual evidence?
- Are exposure limits target-country-specific, with correct unit, fraction, notation and effective date?
- Is `not applicable` technically justified rather than a label for an unavailable test?
- Is an approved phrase technically suitable **for this formulation and this use**?

When evidence is absent, draft only what is supported and keep missing claims out of the printable document.
