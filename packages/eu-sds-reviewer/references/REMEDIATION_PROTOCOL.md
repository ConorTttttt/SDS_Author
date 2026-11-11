# Remediation and verification protocol — fixing SDS issues without inventing facts

## One finding → one testable correction
Every fix must specify:
1. **Observed defect**: verified short quotation/omission and precise SDS page/subsection/version.
2. **Authority**: for LEGAL_NONCOMPLIANCE, exact binding law and clause shown to apply; for recommendations, guidance/internal basis explicitly called nonbinding. For unresolved legal cases, mark verification pending.
3. **Cause category**: heading/metadata; missing information; inaccurate fact; technically inadequate risk control; contradictory advice; label/classification mismatch; country/legal-version mismatch; supply/revision process; wording control.
4. **Remedy**: the actual information to add/remove/correct **where** it belongs, not vague 'update SDS'.
5. **Prerequisite**: evidence, competent specialist decision, classification verification, source law, measured value, OEL database or upstream SDS needed before editing.
6. **Owner**: SDS competent author, classification specialist, laboratory, occupational hygienist, transport adviser, supplier, translator or regulatory/legal reviewer.
7. **Closure test**: objectively examine revised wording AND supporting input and compare affected sections. Mark `RESOLVED` only if fulfilled.
8. **Priority**: CRITICAL/MAJOR/MINOR/ENHANCEMENT independently of class; safety-led urgency.

## Action types and concrete examples

| Observed issue | Candidate class only when proved | Appropriate action | Acceptable closure evidence |
|---|---|---|---|
| Full, legible SDS has no Section 14 heading | LEGAL_NONCOMPLIANCE if Article 31/Part B apply | Add exact Section 14, 14.1–14.7 as applicable; commission transport review where needed. | Corrected SDS pages, cited current law, transport evidence or justified statuses. |
| First page says “Revision 4” but has no revision date or predecessor identification | LEGAL_NONCOMPLIANCE if Annex II 0.2.5 applies and full first page checked | Insert verified revision date and replaced version, document changes in §16 or elsewhere. | Controlled history/source file and corrected first page. |
| Section 8 glove phrase says only “wear suitable gloves” | POTENTIAL_NONCOMPLIANCE if missing legally required specific advice is plausible but use/exposure facts absent | Obtain use-specific compatibility and glove selection evidence; determine relevant material/thickness/breakthrough detail and update 8.2 accordingly. | Qualified PPE assessment and revised use-appropriate Section 8.2. |
| User's phrase notebook has no approval entry for a legally adequate factual Section 9 sentence | RECOMMENDATION (internal-control finding) | Request phrase approval or follow an authorised factual text policy, without mislabelling a statutory breach. | Company wording approval only; underlying data separately verified. |
| Composition dossier not provided, Section 3 seemingly short | NOT_VERIFIED or POTENTIAL_NONCOMPLIANCE depending on specific evidence | Request confidential ingredient matrix, validated statuses/SCL/ATE/M factors/limits; evaluate 3.2.1 or 3.2.2 per product. | Auditable per-ingredient disclosure decisions and checked revised Section 3. |
| SDS 'not regulated for transport' conflicts with signed ADR classification | POTENTIAL_NONCOMPLIANCE until legal/modal review and records reconciled, then possible LEGAL_NONCOMPLIANCE | Verify transport regime, configuration, mode and legally applicable particulars; correct Section 14 if contradiction substantiated. | Competent dated multimodal transport decision and revised §14. |
| December 2020 ECHA guidance suggests clearer phrase than technically and legally sufficient SDS | RECOMMENDATION | Rewrite more clearly only if faithful to validated facts and approved phrase rules; no automatic legal breach. | Competent person review, optional improved wording. |
| Supplier allegedly failed to email updates to prior customers | NOT_VERIFIED from PDF alone | Request recipient/dispatch logs, update triggers and dates for Article 31(9) process check. | Relevant supply/recipient records, actual delivery evidence. |

**Do not copy these example classifications into a real report without checking their conditions.**

## Targeted correction text
- Prefer a **change instruction** with precise facts, subsection and reason rather than silently editing a regulatory document.
- If replacement text is requested, put it in a separately labelled `PROPOSED REPLACEMENT — COMPETENT PERSON VERIFICATION REQUIRED` block, never as an issued statement. Fill only facts supported by the supplied product record. Any unknown appears as author-only square-bracket requirement, not a misleading 'not applicable'.
- If an approved phrase notebook is specifically required, select only verbatim APPROVED phrase ID/version/locale after applicability screening. If none exists, return a phrase-approval dependency and **do not invent an approved ID**.
- Official CLP H/EUH/P phrase text, where needed, must come from current authoritative CLP and verified label decisions, distinct from approved discretionary safety prose.
- A recommendation alone should not trigger mandatory issue block; legal/significant safety problems and unresolved critical facts should be escalated to the competent person for release decision.

## Re-review checklist
For each previous ID:
- Locate changed subsection and new wording; confirm document revision/version and original finding rationale.
- Match verified evidence, law and dates; check that the remedy treats the correct substance/mixture and applicable country.
- Retest linked sections; ensure no new contradiction or disclosure problem created.
- Use status `RESOLVED / PARTIALLY_RESOLVED / UNRESOLVED / NOT_VERIFIED` plus evidence reference and reason.
- An issue isn't 'resolved' because wording was added if the added information remains unsupported, inapplicable or inconsistent with other sections.
- Separate resolved **document text** from still unverified **external delivery/process** tasks.
