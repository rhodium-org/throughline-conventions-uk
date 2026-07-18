#!/usr/bin/env python3
"""Generate the British-English mechanics throughline source from the table below.

The content is a faithful re-expression of the GOV.UK style guide
(https://www.gov.uk/guidance/style-guide), Crown copyright, published under the
Open Government Licence v3.0. This script owns the UID<->convention mapping; UIDs
are assigned positionally, so re-running is idempotent and existing UIDs stay stable
as long as the table is appended to (never reordered or deleted).

Run from the repo root:  python tools/generate_mechanics_uk.py
Then:                    tl check --strict && tl docs
"""
from __future__ import annotations
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

INTENT = dict(
    uid="INT-0001",
    title="Text follows one consistent British-English house style",
    text=(
        "Surface mechanics — spelling, punctuation, capitalisation, numbers and "
        "abbreviation formatting — must be uniform and unambiguous across a body of "
        "content, whatever that content says or however it is toned. Consistent "
        "mechanics remove distraction and signal care; inconsistent mechanics make a "
        "reader doubt everything else. This axis governs the British-English dialect "
        "only; a US house style is a separate sibling source."
    ),
    source_ref="GOV.UK style guide",
)

PRINCIPLES = [
    (
        "Spell in British English",
        "Use British-English spelling throughout.",
        "GOV.UK style guide — spelling",
        [
            ('Use British spellings — "organise" not "organize", "colour" not "color".',
             "GOV.UK — spelling"),
            ('Use "-ise" and "-isation" endings, not "-ize" and "-ization".',
             "GOV.UK — spelling"),
            ('Keep the noun/verb distinction — "licence"/"license", "practice"/"practise".',
             "GOV.UK — spelling"),
        ],
    ),
    (
        "Punctuate to British convention",
        "Apply British punctuation conventions consistently.",
        "GOV.UK style guide — punctuation",
        [
            ("Do not use the Oxford (serial) comma unless it removes a genuine ambiguity.",
             "GOV.UK — commas"),
            ("Use one space after a full stop, never two.",
             "GOV.UK — full stops"),
            ("Use a spaced en dash for a parenthetical dash, not an em dash.",
             "GOV.UK — dashes and hyphens"),
            ('Use double quotation marks for direct quotations, and single marks for a quote within a quote.',
             "GOV.UK — quotes"),
        ],
    ),
    (
        "Capitalise sparingly",
        "Reserve capitals for the start of a sentence and for proper nouns.",
        "GOV.UK style guide — capitalisation",
        [
            ("Use sentence case for all headings, titles and labels — capitalise only the first word and proper nouns.",
             "GOV.UK — capitalisation"),
            ("Do not capitalise words for emphasis or to signal importance.",
             "GOV.UK — capitalisation"),
            ("Lowercase job titles and roles unless they form part of a name.",
             "GOV.UK — capitalisation"),
        ],
    ),
    (
        "Write numbers, dates and times the GOV.UK way",
        "Follow the GOV.UK conventions for figures, dates and times.",
        "GOV.UK style guide — numbers",
        [
            ("Use numerals for all numbers, including 1 to 9.",
             "GOV.UK — numbers"),
            ('Write dates as "1 July 2026" — no ordinal suffix and no comma.',
             "GOV.UK — dates"),
            ('Use "to" in number, date and time ranges, not a dash — "5 to 9", "2010 to 2012".',
             "GOV.UK — ranges"),
            ('Write times in the 12-hour clock — "5pm", "midday", "midnight".',
             "GOV.UK — times"),
        ],
    ),
    (
        "Format abbreviations and symbols",
        "Format short forms and symbols consistently. Whether to define a term for the reader is a readability concern, handled on a separate axis.",
        "GOV.UK style guide — abbreviations",
        [
            ('Do not use full stops in abbreviations — "US", "eg", "am".',
             "GOV.UK — abbreviations"),
            ("Use \"and\", not an ampersand, except within a proper name.",
             "GOV.UK — ampersands"),
            ('Use the "%" symbol with a numeral, not the words "per cent".',
             "GOV.UK — percentages"),
        ],
    ),
]


def scalar(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


def title_from(text: str) -> str:
    head = text.split(" — ")[0].split(";")[0].rstrip(".")
    return head if len(head) <= 80 else head[:77].rstrip() + "..."


def write_register(folder: str, prefix: str, title: str) -> None:
    d = ROOT / folder
    d.mkdir(exist_ok=True)
    (d / ".register.yml").write_text(f"prefix: {prefix}\ndigits: 4\ntitle: {title}\n")


def write_item(folder: str, lines: list[str]) -> None:
    uid = next(l.split("uid: ")[1] for l in lines if l.startswith("uid: "))
    (ROOT / folder / f"{uid}.yml").write_text("\n".join(lines) + "\n")


def main() -> None:
    write_register("intents", "INT", "Purpose")
    write_register("principles", "UR", "British-English mechanics conventions")
    write_register("requirements", "SR", "British-English mechanics rules")

    write_item("intents", [
        f"uid: {INTENT['uid']}",
        "type: intent",
        "status: approved",
        f"title: {scalar(INTENT['title'])}",
        f"text: {scalar(INTENT['text'])}",
        "normative: false",
        "attrs:",
        f"  source_ref: {scalar(INTENT['source_ref'])}",
    ])

    sr = 0
    for i, (ptitle, ptext, psrc, rules) in enumerate(PRINCIPLES, start=1):
        ur = f"UR-{i:04d}"
        write_item("principles", [
            f"uid: {ur}",
            "type: user_requirement",
            "status: approved",
            f"title: {scalar(ptitle)}",
            f"text: {scalar(ptext)}",
            "links:",
            f"- target: {INTENT['uid']}",
            "  type: derives_from",
            "attrs:",
            f"  source_ref: {scalar(psrc)}",
        ])
        for rtext, rsrc in rules:
            # attrs.principle mirrors the implements target purely as a docs
            # grouping key: tl:table filters cannot traverse links.
            sr += 1
            write_item("requirements", [
                f"uid: SR-{sr:04d}",
                "type: system_requirement",
                "status: approved",
                f"title: {scalar(title_from(rtext))}",
                f"text: {scalar(rtext)}",
                "links:",
                f"- target: {ur}",
                "  type: implements",
                "attrs:",
                f"  source_ref: {scalar(rsrc)}",
                f"  principle: {ur}",
            ])

    print(f"wrote 1 intent, {len(PRINCIPLES)} conventions, {sr} rules")


if __name__ == "__main__":
    main()
