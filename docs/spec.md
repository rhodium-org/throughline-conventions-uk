# British-English Conventions — throughline source

This document is **generated from the graph** by `tl docs`; `tl docs --check` gates
it in CI. The prose headings are hand-owned — everything between `tl:*` markers is
injected from the YAML items, so the published spec can never drift from the graph.

This source is the **British-English conventions axis** only: spelling, punctuation,
capitalisation, numbers and abbreviation formatting for one dialect. It says nothing
about readability, tone, genre, medium or brand voice — each of those is its own
throughline source, so a consumer composes exactly the axes a task needs. Every
convention is a `user_requirement`; every rule is a `system_requirement` that
`implements` its convention. The throughline UIDs are this source's own and immutable
— a consumer cites a rule as `conventions:SR-0004`, never by its GOV.UK heading, which
lives in `attrs.source_ref`.

It carries
<!-- tl:count type == 'user_requirement' -->
5
<!-- tl:end --> conventions and
<!-- tl:count type == 'system_requirement' -->
17
<!-- tl:end --> rules.

## Purpose

<!-- tl:item INT-0001 -->
**INT-0001 — Text follows one consistent British-English house style** — `intent`, status `approved`

> Surface conventions — spelling, punctuation, capitalisation, numbers and abbreviation formatting — must be uniform and unambiguous across a body of content, whatever that content says or however it is toned. Consistent conventions remove distraction and signal care; inconsistent conventions make a reader doubt everything else. This axis governs the British-English dialect only; a US house style is a separate sibling source.

**source_ref**: GOV.UK style guide
<!-- tl:end -->

## 1. Spell in British English

<!-- tl:item UR-0001 -->
**UR-0001 — Spell in British English** — `user_requirement`, status `approved`

> Use British-English spelling throughout.

*Derives from:* INT-0001

**source_ref**: GOV.UK style guide — spelling
<!-- tl:end -->

<!-- tl:table attrs.get('principle') == 'UR-0001' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0001 | system_requirement | approved | Use British spellings |
| SR-0002 | system_requirement | approved | Use "-ise" and "-isation" endings, not "-ize" and "-ization" |
| SR-0003 | system_requirement | approved | Keep the noun/verb distinction |
<!-- tl:end -->

## 2. Punctuate to British convention

<!-- tl:item UR-0002 -->
**UR-0002 — Punctuate to British convention** — `user_requirement`, status `approved`

> Apply British punctuation conventions consistently.

*Derives from:* INT-0001

**source_ref**: GOV.UK style guide — punctuation
<!-- tl:end -->

<!-- tl:table attrs.get('principle') == 'UR-0002' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0004 | system_requirement | approved | Do not use the Oxford (serial) comma unless it removes a genuine ambiguity |
| SR-0005 | system_requirement | approved | Use one space after a full stop, never two |
| SR-0006 | system_requirement | approved | Use a spaced en dash for a parenthetical dash, not an em dash |
| SR-0007 | system_requirement | approved | Use double quotation marks for direct quotations, and single marks for a quot... |
<!-- tl:end -->

## 3. Capitalise sparingly

<!-- tl:item UR-0003 -->
**UR-0003 — Capitalise sparingly** — `user_requirement`, status `approved`

> Reserve capitals for the start of a sentence and for proper nouns.

*Derives from:* INT-0001

**source_ref**: GOV.UK style guide — capitalisation
<!-- tl:end -->

<!-- tl:table attrs.get('principle') == 'UR-0003' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0008 | system_requirement | approved | Use sentence case for all headings, titles and labels |
| SR-0009 | system_requirement | approved | Do not capitalise words for emphasis or to signal importance |
| SR-0010 | system_requirement | approved | Lowercase job titles and roles unless they form part of a name |
<!-- tl:end -->

## 4. Write numbers, dates and times the GOV.UK way

<!-- tl:item UR-0004 -->
**UR-0004 — Write numbers, dates and times the GOV.UK way** — `user_requirement`, status `approved`

> Follow the GOV.UK conventions for figures, dates and times.

*Derives from:* INT-0001

**source_ref**: GOV.UK style guide — numbers
<!-- tl:end -->

<!-- tl:table attrs.get('principle') == 'UR-0004' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0011 | system_requirement | approved | Use numerals for all numbers, including 1 to 9 |
| SR-0012 | system_requirement | approved | Write dates as "1 July 2026" |
| SR-0013 | system_requirement | approved | Use "to" in number, date and time ranges, not a dash |
| SR-0014 | system_requirement | approved | Write times in the 12-hour clock |
<!-- tl:end -->

## 5. Format abbreviations and symbols

<!-- tl:item UR-0005 -->
**UR-0005 — Format abbreviations and symbols** — `user_requirement`, status `approved`

> Format short forms and symbols consistently. Whether to define a term for the reader is a readability concern, handled on a separate axis.

*Derives from:* INT-0001

**source_ref**: GOV.UK style guide — abbreviations
<!-- tl:end -->

<!-- tl:table attrs.get('principle') == 'UR-0005' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0015 | system_requirement | approved | Do not use full stops in abbreviations |
| SR-0016 | system_requirement | approved | Use "and", not an ampersand, except within a proper name |
| SR-0017 | system_requirement | approved | Use the "%" symbol with a numeral, not the words "per cent" |
<!-- tl:end -->
