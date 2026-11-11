# Multiple products or mixtures covered by one SDS — legal coverage test

**Primary legal provision:** REACH Annex II §1.1, supplied consolidated PDF p.119:
> "A single safety data sheet may be provided to cover more than one substance or mixture where the information in that safety data sheet fulfils the requirements of this Annex for each of those substances or mixtures."

**This is a permission conditional on content coverage, not an automatic 'same CLP classification = one SDS' rule.** Do not impose a fabricated percentage formula-variation allowance from REACH. Evaluate the proposed common document clause by clause for **every** distinct product/formulation, including Section 3 and all non-classification properties and safe-use measures.

## Matrix to test for each proposed grouping

| Question | Coverage must hold for EVERY member? | Relevant subsection(s) |
|---|---|---|
| Product identifiers and distinct product names clearly resolved | Yes | 1.1 |
| Identified uses / uses advised against and user populations | Yes | 1.2 |
| Supplier, jurisdiction, language, emergency service and SDS issue metadata | Yes for recipients/markets | 1.3–1.4; Art.31(5), Annex II 0.2.5 |
| Classification and label elements; other hazards including ED/PBT/vPvB where relevant | Yes | 2.1–2.3 |
| Required ingredient disclosures (all applicable formulas, ranges, special statuses, SCL/ATE/M-factors) | Yes | 3.2 |
| Route-specific first aid, firefighting, spills, storage, incompatibilities | Yes | 4–7, 10 |
| OEL, engineering controls and PPE details adequate for each intended use | Yes | 8 |
| Physical state, colour(s), flash point, pH, viscosity, volatility etc. (correctly variant-linked) | Yes | 9 |
| Toxicological/ecological details and applicable mixture data / uncertainty | Yes | 11–12 |
| Disposal, mode-specific DG classification, relevant legislation, revision history | Yes | 13–16 |

## Product-level coverage record

```text
Group proposal: [Group A]
Products included: [Product IDs / formulations and revision dates]
Assessment date / market: [date, Member State]
Coverage per product x subsection: PASS | NOT_APPLICABLE_WITH_REASON | FAIL | INSUFFICIENT_INFORMATION
Common clause or approved phrase applicable to each: YES | NO | UNVERIFIED
Product-specific variant table necessary: YES | NO | UNVERIFIED
Decision: CANDIDATE_COMMON_SDS | MUST_KEEP_SEPARATE_UNTIL_RESOLVED | REVIEW_NEEDED
Evidence and relevant Annex II clause for each exception:
```

## Hard stops / cautions

- **No identical hazards shortcut:** same H-codes can conceal different glove selection, solvent volatility, flash points, hazards below classification thresholds or Section 3 disclosure.
- **No one-formula-only Section 3 table:** if regulated listed ingredients differ between variants, the single SDS must make clear which constituents and concentration ranges pertain to which product, while satisfying §§3.2.1–3.2.4 for each.
- **No misleading property range:** one pH, flash point, colour, viscosity, DG class or OEL regime cannot stand for the entire group if it is not valid or clearly attributed. Annex II §9.1(b) explicitly allows 'various' for **colour** of mixture variants, not a general exemption from product-specific information (PDF p.134).
- **Member State language/limits:** one English document may require local versions for different markets; avoid merging incompatible target-country specific statements without explicit versioning.
- **Unevidenced group candidate is not 'approved for one SDS'.** The competent person approves the coverage only once all Annex II requirements are met for each formulation.

Use this module in `MULTI_PRODUCT_COVERAGE` mode, or when user asks if formulations may share an SDS. It can be run before choosing shared approved phrases. No automated grouping judgement may replace competent-person release review.
