# Language drafts for the 27 member states

Agent output, not data. Nothing here renders anywhere: not the bundle, the web app, the PDFs or `/ask`.
The plan that would admit them is [`docs/plans/localisation-plan.md`](../plans/localisation-plan.md);
the strings they cover and the official languages per state are in [`STRINGS.md`](STRINGS.md).

How the files were made, 2026-10-12:

1. Two agents on two models drafted the tables, each for half the states: agent A, claude-opus-5-5, for
   AT BE BG CY CZ DE DK EE EL ES FI FR HR HU; agent B, claude-fable-5-1, for IE IT LT LU LV MT NL PL PT
   RO SE SI SK. Each file names its drafter.
2. Each agent then reviewed every cell of the other's files, never its own, and appended a `## Review`
   table with `ok` or `fix` per key and language, a note, and a suggested wording for every `fix`.
3. `python3 model/i18n_drafts.py check` reads every file and fails on a missing key, a missing language,
   an `en` cell that differs from the source, a dropped "EU-27" or ellipsis, a disclaimer that is not a full
   translation, a file without a review, a review by its own drafter, a language without its BCP 47 tag or
   with a tag that differs from `STRINGS.md`, a file that is not Unicode NFC, or a cell with stray whitespace
   (`STRINGS.md` § The standards the drafts follow).
4. `python3 model/i18n_drafts.py summary` rewrites the table below from the files.

No person who speaks these languages has read them yet. That reading is stage 1 of the plan, and until it
is recorded on a file the file is a machine draft of a page that says, in its own notice, that no person
has reviewed it.

## What the cross-review found, 2026-10-12

1,440 cells, 1,400 `ok`, 40 `fix`. None of the fixes is applied yet; that is stage 1 of the plan, done by the
drafter and re-reviewed. The findings that matter:

- **The honesty notice was weakened in six of agent B's thirteen drafts** (IT, MT, PT, RO, SK and, in a
  different way, SI and IE): "machine-checked" came out as a word that means *verified* ("Verificato",
  "Ivverifikat", "Verificado", "Verificat", "overené"), which is the one claim the notice exists to deny.
  Agent A caught all of them and suggested the word for *checked* in each language. Agent A's fourteen
  disclaimers kept every claim at full strength, agent B found. This is why a translated notice renders
  only after a review on another model and a reading by a person.
- **"Exposure" dropped or turned into causation** in section.exposure in five languages (de for AT and DE,
  lt, lv, de and lb for LU, bg): the heading read as "dependence on abroad" rather than "exposure to it".
- **A word that reads as money** in RO ("fond" for a data holding) and in NL and FR variants a less idiomatic
  phrasing; a noun where the navigation wants an imperative in Greek (CY, EL); "Verificación de datos" in
  Spanish colliding with "data" on a data-centre site.
- **No fix at all** in CZ, DK, EE, FR, HR, HU and SE.

The per-file review tables carry every verdict with its note and suggested wording.

## Summary

<!-- summary:start -->
| ISO | State | Languages | Drafted by | Reviewed by | ok | fix |
|---|---|---|---|---|---|---|
| AT | Austria | de | agent A, claude-opus-5-5, 2026-10-12 | agent B, claude-fable-5-1, 2026-10-12 | 42 | 3 |
| BE | Belgium | nl, fr, de | agent A, claude-opus-5-5, 2026-10-12 | agent B, claude-fable-5-1, 2026-10-12 | 132 | 3 |
| BG | Bulgaria | bg | agent A, claude-opus-5-5, 2026-10-12 | agent B, claude-fable-5-1, 2026-10-12 | 44 | 1 |
| CY | Cyprus | el | agent A, claude-opus-5-5, 2026-10-12 | agent B, claude-fable-5-1, 2026-10-12 | 44 | 1 |
| CZ | Czechia | cs | agent A, claude-opus-5-5, 2026-10-12 | agent B, claude-fable-5-1, 2026-10-12 | 45 | 0 |
| DE | Germany | de | agent A, claude-opus-5-5, 2026-10-12 | agent B, claude-fable-5-1, 2026-10-12 | 42 | 3 |
| DK | Denmark | da | agent A, claude-opus-5-5, 2026-10-12 | agent B, claude-fable-5-1, 2026-10-12 | 45 | 0 |
| EE | Estonia | et | agent A, claude-opus-5-5, 2026-10-12 | agent B, claude-fable-5-1, 2026-10-12 | 45 | 0 |
| EL | Greece | el | agent A, claude-opus-5-5, 2026-10-12 | agent B, claude-fable-5-1, 2026-10-12 | 44 | 1 |
| ES | Spain | es | agent A, claude-opus-5-5, 2026-10-12 | agent B, claude-fable-5-1, 2026-10-12 | 44 | 1 |
| FI | Finland | fi, sv | agent A, claude-opus-5-5, 2026-10-12 | agent B, claude-fable-5-1, 2026-10-12 | 89 | 1 |
| FR | France | fr | agent A, claude-opus-5-5, 2026-10-12 | agent B, claude-fable-5-1, 2026-10-12 | 45 | 0 |
| HR | Croatia | hr | agent A, claude-opus-5-5, 2026-10-12 | agent B, claude-fable-5-1, 2026-10-12 | 45 | 0 |
| HU | Hungary | hu | agent A, claude-opus-5-5, 2026-10-12 | agent B, claude-fable-5-1, 2026-10-12 | 45 | 0 |
| IE | Ireland | ga | agent B, claude-fable-5-1, 2026-10-12 | agent A, claude-opus-5-5, 2026-10-12 | 43 | 2 |
| IT | Italy | it | agent B, claude-fable-5-1, 2026-10-12 | agent A, claude-opus-5-5, 2026-10-12 | 43 | 2 |
| LT | Lithuania | lt | agent B, claude-fable-5-1, 2026-10-12 | agent A, claude-opus-5-5, 2026-10-12 | 44 | 1 |
| LU | Luxembourg | fr, de, lb | agent B, claude-fable-5-1, 2026-10-12 | agent A, claude-opus-5-5, 2026-10-12 | 129 | 6 |
| LV | Latvia | lv | agent B, claude-fable-5-1, 2026-10-12 | agent A, claude-opus-5-5, 2026-10-12 | 44 | 1 |
| MT | Malta | mt | agent B, claude-fable-5-1, 2026-10-12 | agent A, claude-opus-5-5, 2026-10-12 | 44 | 1 |
| NL | Netherlands | nl | agent B, claude-fable-5-1, 2026-10-12 | agent A, claude-opus-5-5, 2026-10-12 | 44 | 1 |
| PL | Poland | pl | agent B, claude-fable-5-1, 2026-10-12 | agent A, claude-opus-5-5, 2026-10-12 | 43 | 2 |
| PT | Portugal | pt | agent B, claude-fable-5-1, 2026-10-12 | agent A, claude-opus-5-5, 2026-10-12 | 42 | 3 |
| RO | Romania | ro | agent B, claude-fable-5-1, 2026-10-12 | agent A, claude-opus-5-5, 2026-10-12 | 40 | 5 |
| SE | Sweden | sv | agent B, claude-fable-5-1, 2026-10-12 | agent A, claude-opus-5-5, 2026-10-12 | 45 | 0 |
| SI | Slovenia | sl | agent B, claude-fable-5-1, 2026-10-12 | agent A, claude-opus-5-5, 2026-10-12 | 44 | 1 |
| SK | Slovakia | sk | agent B, claude-fable-5-1, 2026-10-12 | agent A, claude-opus-5-5, 2026-10-12 | 44 | 1 |
<!-- summary:end -->
