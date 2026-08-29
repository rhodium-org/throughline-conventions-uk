"""British-English conventions source content, authored for the throughline source generator.

This is original guidance by Dr Henry J Grech-Cini, informed by the GOV.UK style guide and
UK publishing convention. Those sources are *referenced*, never reproduced: each item's
`source_ref` names the guidance area it elaborates, and no GOV.UK text is copied here.

Titles are authored, not derived — see the sibling note in the plain-language source. A
title must be a complete statement; `uid` is authored data and permanent (REQ-0004),
stated here because `source_ref` names a shared guidance area and cannot key an item.
"""

INTENT = {
    "uid": 'INT-0001',
    "title": 'Text follows one consistent British-English house style',
    "text": (
        'Surface conventions — spelling, punctuation, capitalisation, numbers and '
        'abbreviation formatting — must be uniform and unambiguous across a body of content, '
        'whatever that content says or however it is toned. Consistent conventions remove '
        'distraction and signal care; inconsistent conventions make a reader doubt everything'
        ' else. This axis governs the British-English dialect only; a US house style is a '
        'separate sibling source.'
    ),
    "source_ref": 'GOV.UK style guide',
}

PRINCIPLES = [
    {
        "uid": 'UR-0001',
        "source_ref": 'GOV.UK style guide — spelling',
        "title": 'Spell in British English',
        "text": 'Use British-English spelling throughout.',
    },
    {
        "uid": 'UR-0002',
        "source_ref": 'GOV.UK style guide — punctuation',
        "title": 'Punctuate to British convention',
        "text": 'Apply British punctuation conventions consistently.',
    },
    {
        "uid": 'UR-0003',
        "source_ref": 'GOV.UK style guide — capitalisation',
        "title": 'Capitalise sparingly',
        "text": 'Reserve capitals for the start of a sentence and for proper nouns.',
    },
    {
        "uid": 'UR-0004',
        "source_ref": 'GOV.UK style guide — numbers',
        "title": 'Write numbers, dates and times the GOV.UK way',
        "text": 'Follow the GOV.UK conventions for figures, dates and times.',
    },
    {
        "uid": 'UR-0005',
        "source_ref": 'GOV.UK style guide — abbreviations',
        "title": 'Format abbreviations and symbols',
        "text": (
            'Format short forms and symbols consistently. Whether to define a term for the '
            'reader is a readability concern, handled on a separate axis.'
        ),
    },
]

RULES = [
    {
        "uid": 'SR-0001',
        "principle": 'UR-0001',
        "source_ref": 'GOV.UK — spelling',
        "title": 'Use British spellings',
        "text": 'Use British spellings — "organise" not "organize", "colour" not "color".',
    },
    {
        "uid": 'SR-0002',
        "principle": 'UR-0001',
        "source_ref": 'GOV.UK — spelling',
        "title": 'Use "-ise" and "-isation" endings, not "-ize" and "-ization"',
        "text": 'Use "-ise" and "-isation" endings, not "-ize" and "-ization".',
    },
    {
        "uid": 'SR-0003',
        "principle": 'UR-0001',
        "source_ref": 'GOV.UK — spelling',
        "title": 'Keep the noun/verb distinction',
        "text": 'Keep the noun/verb distinction — "licence"/"license", "practice"/"practise".',
    },
    {
        "uid": 'SR-0004',
        "principle": 'UR-0002',
        "source_ref": 'GOV.UK — commas',
        "title": 'Do not use the Oxford (serial) comma unless it removes a genuine ambiguity',
        "text": 'Do not use the Oxford (serial) comma unless it removes a genuine ambiguity.',
    },
    {
        "uid": 'SR-0005',
        "principle": 'UR-0002',
        "source_ref": 'GOV.UK — full stops',
        "title": 'Use one space after a full stop, never two',
        "text": 'Use one space after a full stop, never two.',
    },
    {
        "uid": 'SR-0006',
        "principle": 'UR-0002',
        "source_ref": 'GOV.UK — dashes and hyphens',
        "title": 'Use a spaced en dash for a parenthetical dash, not an em dash',
        "text": 'Use a spaced en dash for a parenthetical dash, not an em dash.',
    },
    {
        "uid": 'SR-0007',
        "principle": 'UR-0002',
        "source_ref": 'GOV.UK — quotes',
        "title": 'Use double quotation marks for direct quotations, and single marks for a quote within a quote',
        "text": (
            'Use double quotation marks for direct quotations, and single marks for a quote '
            'within a quote.'
        ),
    },
    {
        "uid": 'SR-0008',
        "principle": 'UR-0003',
        "source_ref": 'GOV.UK — capitalisation',
        "title": 'Use sentence case for all headings, titles and labels',
        "text": (
            'Use sentence case for all headings, titles and labels — capitalise only the '
            'first word and proper nouns.'
        ),
    },
    {
        "uid": 'SR-0009',
        "principle": 'UR-0003',
        "source_ref": 'GOV.UK — capitalisation',
        "title": 'Do not capitalise words for emphasis or to signal importance',
        "text": 'Do not capitalise words for emphasis or to signal importance.',
    },
    {
        "uid": 'SR-0010',
        "principle": 'UR-0003',
        "source_ref": 'GOV.UK — capitalisation',
        "title": 'Lowercase job titles and roles unless they form part of a name',
        "text": 'Lowercase job titles and roles unless they form part of a name.',
    },
    {
        "uid": 'SR-0011',
        "principle": 'UR-0004',
        "source_ref": 'GOV.UK — numbers',
        "title": 'Use numerals for all numbers, including 1 to 9',
        "text": 'Use numerals for all numbers, including 1 to 9.',
    },
    {
        "uid": 'SR-0012',
        "principle": 'UR-0004',
        "source_ref": 'GOV.UK — dates',
        "title": 'Write dates as "1 July 2026"',
        "text": 'Write dates as "1 July 2026" — no ordinal suffix and no comma.',
    },
    {
        "uid": 'SR-0013',
        "principle": 'UR-0004',
        "source_ref": 'GOV.UK — ranges',
        "title": 'Use "to" in number, date and time ranges, not a dash',
        "text": 'Use "to" in number, date and time ranges, not a dash — "5 to 9", "2010 to 2012".',
    },
    {
        "uid": 'SR-0014',
        "principle": 'UR-0004',
        "source_ref": 'GOV.UK — times',
        "title": 'Write times in the 12-hour clock',
        "text": 'Write times in the 12-hour clock — "5pm", "midday", "midnight".',
    },
    {
        "uid": 'SR-0015',
        "principle": 'UR-0005',
        "source_ref": 'GOV.UK — abbreviations',
        "title": 'Do not use full stops in abbreviations',
        "text": 'Do not use full stops in abbreviations — "US", "eg", "am".',
    },
    {
        "uid": 'SR-0016',
        "principle": 'UR-0005',
        "source_ref": 'GOV.UK — ampersands',
        "title": 'Use "and", not an ampersand, except within a proper name',
        "text": 'Use "and", not an ampersand, except within a proper name.',
    },
    {
        "uid": 'SR-0017',
        "principle": 'UR-0005',
        "source_ref": 'GOV.UK — percentages',
        "title": 'Use the "%" symbol with a numeral, not the words "per cent"',
        "text": 'Use the "%" symbol with a numeral, not the words "per cent".',
    },
    {
        "uid": 'SR-0018',
        "principle": 'UR-0004',
        "source_ref": 'GOV.UK — money',
        "title": 'Show money with the £ symbol',
        "text": (
            'Show money with the £ symbol, using decimals only for amounts that include pence'
            ' and omitting a trailing ".00" for whole amounts — for example "£75", "£75.50", '
            '"£1,240".'
        ),
    },
    {
        "uid": 'SR-0019',
        "principle": 'UR-0004',
        "source_ref": 'GOV.UK — numbers',
        "title": 'Use a comma for the thousands separator and a full stop for the decimal point',
        "text": (
            'Use a comma as the thousands separator and a full stop as the decimal point, so '
            'numbers read in the British style — for example "1,240", "£42.50" and '
            '"1,234.56", never the continental "1.240" or "1.234,56".'
        ),
    },
    {
        "uid": 'SR-0020',
        "principle": 'UR-0004',
        "source_ref": 'GOV.UK — numbers',
        "title": 'Use word form for large round numbers',
        "text": (
            'Use word form for large round numbers rather than long strings of zeros — for '
            'example "£3 million", "2 billion" and "£1m", not "£3,000,000".'
        ),
    },
    {
        "uid": 'SR-0021',
        "principle": 'UR-0002',
        "source_ref": 'GOV.UK — bullet points and steps',
        "title": 'Format bullet lists and numbered steps the GOV.UK way',
        "text": (
            'Introduce a list with a lead-in line. In a bullet list, start each bullet with a'
            ' lower-case letter unless it begins with a proper noun, keep each bullet to a '
            'single point, and do not end a bullet with a full stop or join bullets with '
            '"and" or "or". Numbered steps are full sentences, so start each with a capital '
            'letter and end it with a full stop.'
        ),
    },
]
