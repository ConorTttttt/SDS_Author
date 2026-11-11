# Section 3 writing rules — disclosure, not a CLP classification engine

This module exists **solely to populate and review the composition/information on ingredients section**. It does not calculate classification, advise grouping or decide whether an SDS must be supplied. Source: supplied REACH consolidation 22 June 2026, Annex II §§3.1–3.2.4, PDF pp.122–127, subject to current-law/date verification.

## First select the correct subsection
- Substance SDS: `3.1 Substances`.
- Mixture SDS: `3.2 Mixtures`.
Do not put both headings into a single-product SDS merely to make the outline look complete.

## Classified mixture (§3.2.1)
For each hazardous ingredient, test whether disclosure is triggered by **the lowest applicable** comparator under §3.2.1(a)(i)–(viii), including: CLP generic cutoffs; relevant generic concentration limits/notes; harmonised SCL; M-factor-adjusted cutoffs; applicable C&L Inventory specific limits or M factors subject to source verification; one-tenth SCL for skin/respiratory sensitisation; and relevant CLP Annex II limits. A blanket 1% rule is invalid.

Independently examine:
- §3.2.1(b): a substance with a **Union** workplace OEL (no blanket 1% minimum in that branch).
- §3.2.1(c): relevant PBT/vPvB, Candidate List or endocrine status at the specified **0.1%** trigger.

These are **disclosure** conditions, not proof of whole-mixture classification or ingredient contribution.

## Mixture not classified under CLP (§3.2.2)
Check each separate branch (source and date required):
- §3.2.2(a): relevant hazardous or Union-OEL constituent at **≥1% w/w** (non-gas) or **≥0.2% v/v** (gas).
- §3.2.2(b): specified PBT/vPvB, Candidate List or endocrine status at **≥0.1% w/w**.
- §3.2.2(c): Skin/Resp. Sens. 1 or 1B or Carc. 2 at **≥0.1%**.
- §3.2.2(d): Skin/Resp. Sens. 1A at **≥0.01%**.
- §3.2.2(e): a sensitiser with an SCL at **≥one-tenth of that SCL**.
- §3.2.2(f): relevant Repr. categories/effects at **≥0.1%**.

These thresholds are a **navigation summary from v4**, not a substitute for checking the actual applicable clause and relevant ingredient datasets. Do not silently round values at equality thresholds or assume unknown status means absent.

## What to print (§§3.2.3–3.2.4)
Use sourced identity, concentration or valid range, relevant EC/CAS/registration identifiers, constituent classification and H/EUH codes, and SCL/M-factor/ATE **if available and applicable**. Explain the relevant disclosure reason for a non-CLP-classified reported constituent. Use the rules governing alternative chemical names and truncated registration numbers only when verified. Nanoform characteristics require product-specific assessment where applicable.

Mixture ranges require careful assessment, including upper-end hazard implications where Annex II so requires. Confidential formulation content not legally required in the SDS must not be exposed without approval.

## Mandatory author-only ingredient ledger
`ingredient | disclosed concentration/range and basis | ingredient hazards | SCL/ATE/M factor | Union OEL/status flags | verified applicable disclosure comparator/clause | disclose YES/NO/PENDING | evidence | source/date`.

If classification data, ingredient concentrations or status evidence are incomplete, use `PENDING`, never assume `NO`. Clarify **classification input**, **Section 3 disclosure**, and **safe-use relevance** as separate aspects; no standalone classification calculation is part of this package.
