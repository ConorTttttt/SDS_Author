# EU SDS Writer — independent Gemini authoring package (v5.0)

**Purpose:** write, edit, recommend wording for and quality-check **EU/EEA REACH Annex II SDSs** for a single specified product. This is deliberately **not** a product-grouping, CLP-calculation, Article 31 supply workflow, PCN filing or transport-classification package.

## Built from the current repository
Based on `SDS_Author` **v4.0**, main commit `043d2f1f4591f9d0184ff94452bb4c09987cf0fb` (11 November 2026). Retains its REACH consolidated 22 June 2026 source, ECHA 2020 drafting guidance and ECHA REF-11 2024 quality reference; strips out standalone functions not required to **write** the SDS. Original v4 files remain unchanged at repository root.

## Folder contents
- `SKILL.md`: primary Gemini CLI/skill instructions.
- `GEM_INSTRUCTIONS.md`: compact instructions for a Gemini Gem using an attached notebook.
- `references/SECTION_AUTHORING_MAP.md`: 16-section writing requirements.
- `references/SECTION3_WRITING.md`: ingredient-disclosure drafting safeguards, not a classification calculator.
- `references/PHRASE_NOTEBOOK.md`: phrase approval, retrieval and suitability contract.
- `references/PRODUCT_EVIDENCE.md`: evidence-status rules and minimum product dossier.
- `references/QUALITY_GATE.md`: REF-11-informed completeness/plausibility checks.
- `references/SOURCES_AND_VERSIONING.md`: regulatory hierarchy, provenance and date-scope protocol.
- `templates/product_dossier.json`: intentionally unpopulated authoring input.
- `templates/phrase_library.json`: intentionally empty controlled phrase export.
- `tests/AUTHORING_ACCEPTANCE.md`: review scenarios; **not** executed Gemini tests.
- `sources/`: exact PDFs from the upstream v4 repository; no text in them is automatically an approved phrase.

## Using in Gemini
**Gemini CLI skill:** place the complete `eu-sds-writer` directory under your supported skills directory (for example `~/.gemini/skills/eu-sds-writer/`), preserving `SKILL.md` at its root. Confirm that your Gemini environment actually loads this skill and can read the referenced files.

**Gemini Gem:** paste `GEM_INSTRUCTIONS.md` into the Gem's instructions, attach the applicable source files and connect your **separate controlled approved-phrase notebook** (or a structured approved phrase export). NotebookLM integration varies by account/interface: **do not assume** a notebook is connected or searchable until Gemini can quote exact IDs and text from it.

**Authoring:** provide a real dossier, verified mixture classification/label, applicable country/language/date, and source evidence. Start with `INTAKE Section 7` or `RECOMMEND Section 8` before drafting a full SDS.

## Important constraints
- **No approved phrases are bundled.** Do not use ECHA examples, an existing supplier SDS or prose in this skill as approved stock text.
- The 2026 REACH PDF is a **snapshot**; check current effective law and transitional provisions for the actual date and jurisdiction. ECHA guidance and REF-11 are nonbinding.
- A complete-looking output is not a verified SDS. Every draft needs appropriate competent-person authorisation before issue.
- This package was assembled and checked for structural consistency. Its decisions have **not** been validated against your live NotebookLM phrase library or real product cases.
