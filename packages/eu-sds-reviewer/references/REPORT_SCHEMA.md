# Reviewer output contract — report and structured records

## Report envelope (mandatory)
- `report_id`, `review_date`, `review_mode`, `reviewer_type = AI decision support`.
- `sds_file_name`, `document_revision`, `document_issue_date`, `page_count_checked`, `document_scope` (FULL/PARTIAL/SELECTED_SECTIONS).
- `product_identifier`, `substance_or_mixture`, `recipient_member_states`, `document_language`, `target_regulatory_date`.
- `legal_sources_checked` (instrument, edition, date, pinpoint checked, status), `legal_source_status` (VERIFIED_FOR_FINDINGS/PARTIAL/NOT_VERIFIED).
- `product_evidence_available` and `not_checked_scope`.
- `findings_by_class` with four separate counts; optional counts by severity; overall status **NOT_CERTIFIED**. No pass percentage or claim of government inspection.

## Finding fields (mandatory for each)
| Field | Meaning |
|---|---|
| `finding_id` | Stable review prefix and number, e.g., `EU-SDS-R-001`. |
| `finding_class` | Exactly one: LEGAL_NONCOMPLIANCE, POTENTIAL_NONCOMPLIANCE, RECOMMENDATION, NOT_VERIFIED. |
| `priority` | CRITICAL, MAJOR, MINOR or ENHANCEMENT (orthogonal to class). |
| `review_track` | DOCUMENT_COMPLETENESS, TECHNICAL_PLAUSIBILITY, LEGAL_VERSION_AND_JURISDICTION, SUPPLY_AND_REVISION_PROCESS, INTERNAL_WORDING_CONTROL. |
| `sds_reference` | Actual subsection, page and concise observed quote OR verified absence in fully reviewed pages; no made-up evidence. |
| `issue` | Specific problem or unresolved check, with product scope. |
| `legal_basis` | Binding citation: instrument, exact clause, text examined, applicable date and jurisdiction. **Required for proven breach**; otherwise null or explicitly unverified. |
| `nonbinding_basis` | Guidance/report/internal policy citation (if used); separate from binding citation. |
| `applicability_test` | Trigger facts, exceptions, transitional result and basis. |
| `proof_status` | COMPLETE, PARTIAL, UNAVAILABLE (COMPLETE required for a proven breach). |
| `why_it_matters` | Practical effect on safe use, accurate hazard communication or verified legal duty. |
| `fix_action` | Exact correction and affected fields/subsections, not just 'review/update'. |
| `evidence_needed` | Specific independent evidence, if any; empty only when fully supported. |
| `owner` | Responsible reviewer/function. |
| `closure_test` | Objective test of corrected SDS + supporting records. |
| `resolution_status` | OPEN, RESOLVED, PARTIALLY_RESOLVED, UNRESOLVED, NOT_VERIFIED. |
| `related_sections` | Other sections to check for regressions. |

Machine-readable contract: `templates/finding_record.schema.json` describes one finding. A review report contains a list of such findings plus scope/coverage. Validation requires human assessment of **truth** in addition to schema validity.

## Minimal example — demonstrated failure *only if* the complete SDS and correct law are checked
- ID: EU-SDS-R-001
- Class: LEGAL_NONCOMPLIANCE
- Priority: MINOR
- SDS: “page 1 of 12” (verified document) while pages 2–12 contain no page numbering
- Law: REACH Annex II 0.3.2, applicable version confirmed, and actual document pages validated
- Fix: add continuous numbering plus appropriate page extent/continuation to every page including annexes
- Closure: inspect every page of the corrected issued-form PDF and verify all pages display required information.

## Minimal example — clear improvement without proof of breach
- ID: EU-SDS-R-002
- Class: RECOMMENDATION
- Priority: ENHANCEMENT
- SDS: Section 7 has a comprehensible but verbose instruction
- Basis: editorial clarity preference or ECHA authoring guidance (nonbinding); **no identified unmet legal provision**
- Fix: suggest shorter equivalent instruction preserving all verified safety details and phrase approval rules
- Closure: reviewed readability and no change to product facts.

## Summary wording
“Reviewed [files, pages, sections, jurisdiction, date]. Identified N proven legal breaches, N potential legal breaches, N recommendations and N checks not verified. These totals are findings, not a compliance percentage. [Unexamined material]. Legal sources were [verification status]. Report is **regulatory decision support only; no certification or release approval**.”

## Sample format and severity
See `templates/review_report.md` and `references/REMEDIATION_PROTOCOL.md`. Count a unique issue only once. Where a recommendation describes a separate enhancement, create another ID and make clear it does not itself create a legal duty.
