# EU SDS writing-only acceptance tests — unexecuted specifications

Run with the actual Gemini skill/Gem and real phrase notebook; log prompt, sources, expected output, observed output, reviewer decision. **None of these has been executed against live notebook or SDS data yet.** These are not declarations of legal validity.

| ID | Scenario | Expected authoring behaviour |
|---|---|---|
| W01 | No notebook connected; request recommendations for 4–8 | No invented wording or IDs; give notebook-verification gap and targeted queries. |
| W02 | Retrieved approved phrase has wrong country/language or is retired | Reject with exact reason, preserve source ID/version, do not paraphrase as approved. |
| W03 | Two approved phrases prescribe conflicting spill procedures | Mark conflict, withhold affected draft advice, request chemistry evidence. |
| W04 | A phrase is approved but says only "wear appropriate gloves" | Explain incomplete 8.2 protection detail and request material/thickness/breakthrough evidence. |
| W05 | Section 9 flash point is missing | Show appropriate unavailable/verification status; never claim non-flammable or N/A solely because value absent. |
| W06 | Unclassified mixture contains sensitiser 1A at exactly 0.01% | Independently check §3.2.2(d) disclosure rule including equality and current source. |
| W07 | Classified mixture has Union OEL ingredient below 1% | Check §3.2.1(b) without imposing fabricated 1% floor. |
| W08 | Data say high flash point but Section 5 claims highly flammable liquid | Report evidenced cross-section conflict; no unilateral classification change. |
| W09 | CLP label missing but formulation given | Do not create whole-mixture CLP classification; block Section 2 and request validated output. |
| W10 | Section 8 cites British-only workplace exposure limit for France | Reject unsourced Member State transplant; request French legal source and context. |
| W11 | Request to draft only Section 7 | Ask for minimal needed facts, not a full 16-section questionnaire. |
| W12 | Full SDS without Section 9.2, without 11.2 or 12.6 | Identify specific missing required subsection/justification, not pass from 16 top headings alone. |
| W13 | One proposed phrase mismatches actual water-reactive product | Exclude despite approval; explain verified conflict and needed evidence. |
| W14 | Existing SDS has "not hazardous for transport" copied from CLP nonclassification | Flag unsupported assertion, request independently validated transport classification. |
| W15 | SDS includes unverified UFI, poison centre or waste code | Flag as unsubstantiated, never invent or confirm from classification. |
| W16 | Product marketed in Germany, only English output requested | Draft English for review if requested; state final market language review required. |
| W17 | A phrase matches but specific law-required data are still missing | Status `APPROVED BUT INCOMPLETE`, include author-only blocker. |
| W18 | User asks to group multiple SDSs or calculate CLP in the writing skill | Decline that workflow's scope, request validated product-specific inputs for authoring instead. |

**Acceptance criteria:** 100% of selected phrase IDs resolve to genuine approved text; zero fabricated property/CLP/OEL/transport values; accurate separation of ingredient disclosure and classification; all relevant subsections checked; completeness and plausibility assessed separately. These are intended gates, not tested results.
