# Controlled phrase notebook — exact retrieval and applicability

The approved phrase notebook is **external user-controlled content**. No wording in this package, the ECHA guide, REF-11, REACH itself or a sample SDS is automatically an approved reusable phrase.

## Candidate retrieval
Query every requested subsection with a combination of (1) exact subsection; (2) confirmed whole-product CLP hazards/H codes; (3) relevant **ingredient** properties even if they do not drive whole-mixture classification; (4) product state, flash point/pH/solubility/reactivity, dust/aerosol/volatility; (5) identified use, handling conditions and exposure route; (6) market/language and (7) critical absence/presence of evidence.

Search synonyms, hazards and family-specific terms (acids/alkalis, flammable solvents, oxidisers, aqueous surfactants, powders, reactive products, aerosols) only to **find** entries; family membership alone is not proof that any phrase is applicable. Retrieve multiple plausible options. If the notebook cannot be reliably queried, label `NOTEBOOK NOT VERIFIED`, not `no phrase exists`.

## Approval gate
A candidate may be `SELECTED` only when all are true:
1. Real unique ID, version/revision, exact verbatim text and original notebook source resolved.
2. Actual approval status `APPROVED` at the relevant date; not draft/retired.
3. Language, Member State, product scope, subsection, use scenario and conditions match.
4. Required factual predicates are verified; no exclusion predicate holds; missing predicate is **UNKNOWN**, not false.
5. Prescribed placeholders, if any, can be filled exclusively with verified data under the phrase record's substitution rules.
6. No conflict with other selected phrases, product evidence, actual label or other sections.
7. Wording is **sufficient for the legal information requirement**; if not, set `APPROVED BUT INCOMPLETE`, not a false pass.

Statuses:
- `SELECTED`: eligible, wording exact, supported.
- `CONDITIONAL`: plausible but one or more evidence/locale/approval details are unresolved; cannot appear as asserted text.
- `REJECTED`: known mismatch or conflict, with exact reason.
- `NOT VERIFIED`: text, ID, status or notebook access cannot be proven.
- `APPROVED BUT INCOMPLETE`: eligible as far as it goes but does not satisfy the required subsection's information needs.

## Verbatim and provenance
Keep `notebook name | notebook revision | phrase ID | phrase revision | exact text | evidence used | subsection | conflicts/alternatives` in an author-only ledger. Never silently change punctuation, word order, tense, language or concatenate two phrase halves into a new stock phrase. Do not infer approval merely because a phrase sounds familiar or appears in an example SDS.

Official CLP statement wording, numeric values, unit symbols and supplier identifiers are handled as separately verified legally required or factual content. A library's approval does not establish the technical truth of a statement.

## Response shape
`subsection | candidate ID/revision | EXACT wording | status | evidence | matched/unmet conditions | rejected alternative | notebook/source`.

If suitable approved text cannot be found, include an **author-only** marker `[APPROVED PHRASE REQUIRED: subsection/topic]` and list targeted searches, missing facts and approval action. Do not put AI-proposed wording in the actual SDS.
