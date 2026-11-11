# REACH Annex II Section 3: ingredient-disclosure decision engine

**Primary source:** Full REACH (consolidated 22 June 2026), Annex II §§3.1–3.2.4, PDF pp.122–127. **Do not confuse the three different tests:** (1) is an SDS required by Article 31; (2) is an individual ingredient disclosed under §3; (3) does an ingredient contribute to CLP mixture classification? These have different rules.

## Required input per formulation and constituent

```yaml
mixture:
  is_mixture: true
  clp_mixture_classified: true | false | UNKNOWN
  target_country: 'Member State'
  issue_date: 'YYYY-MM-DD'
  validated_classification_source: 'reference/date'
ingredient:
  substance_identifier: 'CAS/EC/name and source'
  concentration: 'exact or controlled range; percent mass or volume'
  physical_basis: 'gas/non-gas'
  component_clp_classifications: ['hazard category with source and effective date']
  specific_concentration_limits: ['value, hazard endpoint, source, date']
  generic_concentration_limits: ['relevant CLP item']
  generic_cutoffs: ['relevant CLP item']
  m_factor: 'value and CLP source if applicable'
  ate: 'route/value/source if applicable'
  union_oel: 'yes/no/unknown with legal basis'
  pbt_vpvb: 'status/source/date'
  candidate_list: 'status/reason/source/date'
  endocrine: 'status under relevant criteria/source/date'
  is_nanoform: 'yes/no/unknown; characteristics and registration/CSR status'
```

## Decision A: mixture CLP classified (`Annex II §3.2.1`)

For each ingredient **posing a health/environmental CLP hazard**, include it if its individual concentration meets **the lowest applicable** disclosure comparator. Verify all relevant alternatives:

1. Generic **cut-off** values, CLP Annex I Table 1.1.
2. Generic **concentration** limits, CLP Annex I Parts 3–5, and table notes relevant to SDS on request; special aspiration threshold **>=1%** in this clause.
3. Harmonised **SCL**s, CLP Annex VI Part 3.
4. CLP Annex VI **M-factor-adjusted** generic cutoff under CLP Annex I §4.1.
5. Specific concentration limits provided to CLP C&L Inventory (after checking relevance/authority).
6. **One tenth of the specific concentration limit** for a skin/respiratory sensitiser with SCL.
7. Relevant concentration limits in **CLP Annex II**.
8. C&L Inventory **M-factor-adjusted** generic cutoff under CLP Annex I §4.1.

`§3.2.1(a)(i)–(viii)`, PDF p.123. **Do not use CLP cutoffs as the entire decision**, or assume each numerical cutoff is a universal classification threshold; disclosure is a different operation.

Also include:
- **Substances with a Union workplace OEL** not already included under (a), `§3.2.1(b)` p.124. This clause does *not* impose a universal 1% minimum for this branch.
- **PBT, vPvB, Article 59(1) Candidate List for other reasons, or ED status defined by the cited EU criteria** at **>=0.1%** per substance, `§3.2.1(c)` p.124.

### REACH Annex II Table 1.1 (p.124–125) — one input to rule, not the whole algorithm

| Hazard component category | Table 1.1 minimum (%) |
|---|---:|
| Acute toxicity 1–3 | 0.1 |
| Acute toxicity 4 | 1 |
| Skin corrosion/irritation 1/1A/1B/1C/2 | 1 |
| Eye damage/irritation 1/2 | 1 |
| Respiratory sensitiser 1/1B | 0.1 |
| Respiratory sensitiser 1A | 0.01 |
| Skin sensitiser 1/1B | 0.1 |
| Skin sensitiser 1A | 0.01 |
| Germ-cell mutagenicity 1A/1B | 0.1 |
| Germ-cell mutagenicity 2 | 1 |
| Carcinogenicity 1A/1B/2 | 0.1 |
| Reproductive toxicity 1A/1B/2 and lactation | 0.1 |
| STOT SE 1/2/3 | 1 |
| STOT RE 1/2 | 1 |
| Aspiration toxicity | 1 |
| Aquatic Acute 1 | 0.1 |
| Aquatic Chronic 1 | 0.1 |
| Aquatic Chronic 2/3/4 | 1 |
| Hazardous to ozone layer | 0.1 |

**Critical:** These Table 1.1 values are **not blanket final disclosure results**. The §3.2.1(a) rule uses the **lowest** of *all eight* comparators where applicable. Confirm correct CLP revision, SCL, M-factor, classification, concentration basis and exclusions for every ingredient.

## Decision B: mixture NOT CLP classified (`Annex II §3.2.2`)

For each ingredient, test **independently**:
- **>=1% w/w non-gas** or **>=0.2% v/v gas** if a health/environmental hazardous substance OR substance with **Union** OEL. §3.2.2(a), p.125.
- **>=0.1% w/w** for PBT/vPvB, Candidate List for relevant other reasons, or specified ED status. §3.2.2(b), p.125.
- **>=0.1%** for Skin Sens. 1/1B, Resp. Sens. 1/1B or Carc. 2. §3.2.2(c), p.125.
- **>=0.01%** for Skin Sens. 1A or Resp. Sens. 1A. §3.2.2(d), p.125.
- **>=one tenth of specific concentration limit** for a skin/respiratory sensitiser with an SCL. §3.2.2(e), p.125.
- **>=0.1%** for Repr. 1A/1B/2 or lactation. §3.2.2(f), p.126.

The exact `>=` conditions include **equality**; do not convert them into `>` or round a value without knowing precision. A union OEL branch for **unclassified** mixtures is subject to a minimum in §3.2.2(a), unlike the distinct classified-mixture branch in §3.2.1(b). This difference must have a regression test.

## Decision C: what to show for disclosed components

`§3.2.3`, p.126:
- Component hazard classes/category codes; H/EUH codes and full text in §16 if abbreviated.
- If a component is **not CLP-classified but disclosed for an independent reason**, explain this reason (e.g. Union OEL or relevant status).
- SCL, M-factor and ATE **if available**, not generated from ignorance.
- Nanoform particle characteristics where required; check whether registered/addressed in downstream-user CSR versus non-registered case.

`§3.2.4`, pp.126–127:
- Ingredient name and **registration number if available**, plus EC number if available; conditions govern shortening joint registration numbers; authorised alternative chemical name under CLP Art.24 is **not** a universal trade-secret permission.
- CAS/IUPAC may be shown if available as permitted; do not fabricate identifiers.

`§3.2` introduction, pp.122–123:
- Report exact concentration or permitted ranges as appropriate. If ranges and no whole-mixture effect data, hazard information must account for **highest** concentration in each range; do not author at midpoint or min.
- Disclosing more ingredients is permitted (e.g. voluntary full formulation), but **do not reveal confidential composition** unless user-authorised and applicable law permits.

## Separate output record per ingredient

```json
{
  "ingredient_id":"[from product dossier]",
  "mixture_classification_branch":"CLASSIFIED | UNCLASSIFIED | UNKNOWN",
  "ingredient_concentration":"[number / range with basis]",
  "contributes_to_mixture_classification":"YES | NO | UNKNOWN — separate CLP assessment",
  "disclose_in_section_3":"REQUIRED | NOT_REQUIRED_BY_CHECKED_TRIGGERS | REVIEW_NEEDED",
  "triggered_clauses":["REACH Annex II §3.2.1(b)"],
  "comparator_values":["actual verifiable CLP source required"],
  "nonclassification_disclosure_reason":"[if relevant]",
  "values_to_print":{"ATE":"[verified value / not available]","SCL":"...","M_factor":"..."},
  "source_pdf_pages":[123,124,125,126],
  "source_verification_date":"YYYY-MM-DD",
  "reviewer_notes":"[unresolved conditions]"
}
```

Never set `NOT_REQUIRED_BY_CHECKED_TRIGGERS` if the CLP data, ingredient status, concentration or Union OEL information is unknown; use `REVIEW_NEEDED`. A **non-contributing ingredient** can still **require disclosure** and **affect safe-use instructions**.
