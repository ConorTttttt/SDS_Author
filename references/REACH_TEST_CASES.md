# REACH full-regulation regression scenarios (v4)

These are **test specifications, not test results**. Each scenario requires actual applicability and product evidence checks; do not report as a verified product decision without that evidence. All clauses refer to the supplied 22 June 2026 consolidated text. Source key: Articles 31–32 pp.39–43; Annex II pp.117–152.

## Article 31 / Article 32 decision tree

| Test | Scenario | Verified legal clause (supplied PDF) | Required behaviour |
|---|---|---|---|
| A01 | Hazardous mixture supplied to a professional recipient | Art.31(1)(a); 31(8) | SDS required subject to actual scope; supply at first delivery; evidence of classification needed. |
| A02 | Hazardous mixture offered to general public with sufficient information | Art.31(4) | Check exception; if requested by downstream user/distributor provide SDS. |
| A03 | Pure substance meeting Annex XIII PBT criteria though not CLP-classified | Art.31(1)(b) | SDS trigger assessed independently of CLP hazard classification. |
| A04 | Nonclassified mixture includes hazardous constituent at 0.99% w/w | Art.31(3)(a) | Do not trigger 1% branch alone; other branches and precision still checked. |
| A05 | Nonclassified mixture includes hazardous constituent at exactly 1.00% w/w | Art.31(3)(a) | On-request branch triggered at equality, assuming other conditions satisfied. |
| A06 | Nonclassified gas mixture with hazardous constituent at 0.20% v/v | Art.31(3)(a) | On-request branch triggered; use gas volume basis. |
| A07 | Nonclassified mixture has constituent with Union OEL at 0.03% | Art.31(3)(c) | Check request rule without inventing 1% cutoff for Union OEL branch. |
| A08 | Nonclassified mixture contains Candidate List substance at 0.1% w/w | Art.31(3)(b) | Assess on-request duty and qualifying listing reasons. |
| A09 | No SDS duty under Article 31; relevant restriction exists | Art.32(1)(c) | Do not declare no communication duty; assess Article 32. |
| A10 | Product manufactured under a registration exemption | Art.2,31 | Do not infer Title IV exemption from mere registration exemption. |
| A11 | English SDS to Member State requiring local official language | Art.31(5) | Flag language issue; do not treat English as universally sufficient. |
| A12 | SDS only sent after first delivery | Art.31(8) | Supply process finding, do not assume product PDF demonstrates delivery. |

## Annex II Section 3 disclosure

| Test | Scenario | Verified legal clause (supplied PDF) | Required behaviour |
|---|---|---|---|
| S01 | Classified mixture Skin Sens.1A ingredient at exactly 0.01% | §3.2.1(a) Table 1.1 | Apply >=0.01%, then check any lower comparator; equality counts. |
| S02 | Classified mixture Aquatic Acute1 M-factor present | §3.2.1(a)(iv)/(viii) | Calculate CLP adjusted disclosure cutoff from validated M factor; do not reuse 0.1% blindly. |
| S03 | Classified mixture SCL lower than generic Table 1.1 | §3.2.1(a)(iii) | Use lower applicable comparator; avoid 1% generic assumption. |
| S04 | Classified mixture sensitiser with SCL | §3.2.1(a)(vi) | Include one-tenth SCL comparator; no generic 0.1% shortcut. |
| S05 | Classified mixture ingredient has Union OEL but no hazardous CLP class | §3.2.1(b) | Separate disclosure branch; do not force universal 1% cutoff. |
| S06 | Unclassified mixture ingredient with Union OEL at 0.9% w/w | §3.2.2(a) | Do not reuse classified-mixture OEL rule; explicit 1% condition here. |
| S07 | Unclassified gas with qualifying hazardous ingredient 0.2% v/v | §3.2.2(a) | Disclose at equality, using volume basis. |
| S08 | Unclassified mixture Resp.Sens.1A 0.010% | §3.2.2(d) | Disclose at equality. |
| S09 | Unclassified mixture Carc.2 0.1% | §3.2.2(c) | Disclose at equality. |
| S10 | Unclassified mixture Repr.2 0.1% | §3.2.2(f) | Disclose at equality. |
| S11 | Unclassified mixture relevant ED constituent 0.1% w/w | §3.2.2(b) | Status-based disclosure; do not rely only on CLP mixture classification. |
| S12 | Ingredient nonclassified but disclosed for OEL | §3.2.3 | Explain why ingredient appears; not mislabeled hazardous. |
| S13 | Disclosed ingredient has known ATE, SCL and M factors | §3.2.3 | Present relevant available parameters and sources. |
| S14 | Disclosed ingredient ATE unavailable | §3.2.3 | Never fabricate ATE; reflect if available requirement. |
| S15 | Ingredient concentration range 0.05–0.5% and no mixture effect data | §3.2 opening | Assess health/environmental hazard wording against upper end of range. |
| S16 | Ingredient does not drive classification but qualifies for disclosure | §3.2.1/3.2.2 | Keep classification contribution and disclosure status separate. |

## Annex II quality and cross-section rules

| Test | Scenario | Verified legal clause (supplied PDF) | Required behaviour |
|---|---|---|---|
| Q01 | SDS contains reassuring phrase harmless despite classification | §0.2.4 | Flag impermissible assurance and phrase exclusion. |
| Q02 | One mandatory subsection is blank | §0.4; Part B | Fail completeness despite other 15 sections present. |
| Q03 | Updated SDS has no superseded version or Section 16 changes | §0.2.5; §16 | Missing revision control and change notification. |
| Q04 | No page numbers on SDS annex | §0.3.2 | Flag missing numbered pages/annex. |
| Q05 | UFI is present in SDS subsection 2.2 rather than 1.1 | §1.1 | Flag placement; do not infer universal display duty. |
| Q06 | Registration number shortened without supplier 7-day process | §1.1 or §3.2.4 | Request conditional basis and process evidence. |
| Q07 | Supplier address provided but no competent-person email | §1.3 | Flag required contact detail. |
| Q08 | Nonclassified mixture Section 2.1 blank | §2.1 | Require clear non-classified statement. |
| Q09 | Gloves required but only generic protective gloves approved phrase | §8.2.2.2(b)(i) | Phrase permitted only if scientifically suitable; material/thickness/breakthrough gaps highlighted. |
| Q10 | OEL copied from wrong Member State | §8.1.1 | Flag legal basis and national mismatch. |
| Q11 | Liquid has blank flash point field | §9.1 | Request measured value or supported unavailability; cannot infer N/A. |
| Q12 | Different formula colour variants with same other properties | §9.1(b) | Consider various only for colour, not unspecified all property differences. |
| Q13 | Section 9.2 entirely absent | §9.2; Part B | Flag missing subsection and relevant information. |
| Q14 | Section 16 omits mixture classification methodology | §16(d) | Flag missing Article 9 CLP methods disclosure. |

## One SDS for multiple products

| Test | Scenario | Verified legal clause (supplied PDF) | Required behaviour |
|---|---|---|---|
| G01 | Two products same CLP hazards but different Section 8 PPE | §1.1 one-SDS permission | Reject automatic grouping; common text insufficient unless products separately addressed. |
| G02 | Two products same hazard codes but one solvent has lower flash point | §1.1, §9.1 | Require product-specific property/hazard and fire/transport coverage. |
| G03 | Mixture variants differ in colour only | §1.1; §9.1(b) | Common SDS may express colour various if all other coverage checks pass. |
| G04 | Two mixtures Section 3 disclosure ingredients differ | §1.1; §3.2 | No single undifferentiated ingredient table; variant-specific coverage required. |
| G05 | Products shipped to two Member States with different national OELs | Art.31(5); §8.1.1 | Account for language/country requirements; no one-size-fits-all OEL assumption. |
| G06 | Two variants have no tested pH data for one formulation | §1.1; §9.1 | Return unresolved, not grouping approved. |

