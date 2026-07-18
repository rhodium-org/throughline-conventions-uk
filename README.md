# throughline-conventions-uk

The **British-English conventions** content axis, expressed as a
[throughline](https://pypi.org/project/throughline/) **source** — a standalone,
grounded requirements graph that a consuming project composes with
[throughline-compose](https://github.com/timebacksolutions/throughline-compose).

This repository holds no application code. It is a directory of small YAML items with
permanent UIDs, validated by `tl check`. Consumers import it under a namespace and
reference its rules as `conventions:SR-0004` or its conventions as `conventions:UR-0002`.

## One orthogonal axis, on purpose

This source is **only** the surface-conventions axis for **one dialect** — British
English: spelling, punctuation, capitalisation, numbers and abbreviation formatting.
It deliberately says nothing about:

- **readability** (word choice, sentence length, active voice) — see `throughline-plain-language`
- **tone / register** (formal, informal, playful)
- **genre / purpose** (inform, instruct, persuade, negotiate)
- **medium / channel** (web page, email, microcopy, slide deck)
- **brand voice** (an organisation's own personality)

Each of those is its own throughline source. A US house style is a **sibling** source
(`throughline-conventions-us`), not a branch of this one, because the two dialects are
different axes rather than editions of one axis. Keeping the axes separate is the
whole point: a task like *"a plain, formal, UK-English web page"* becomes a **compose**
of `plain` + `tone-formal` + `conventions-uk` + `medium-web` — the same way a security
project composes `asvs` + `gds` + `wcag`.

## What's in the graph

<!-- tl:count type == 'user_requirement' -->
5
<!-- tl:end --> conventions as `user_requirement`s, each `derives_from` the root
intent, and
<!-- tl:count type == 'system_requirement' -->
17
<!-- tl:end --> concrete rules as `system_requirement`s, each `implements` its
convention. The published spec is generated from the graph at
[`docs/spec.md`](docs/spec.md).

- `INT-0001` — the root intent (why one consistent house style matters), `normative: false`.
- Conventions `UR-0001`…`UR-0005` — spelling, punctuation, capitalisation, numbers,
  abbreviations.
- Rules `SR-0001`…`SR-0017` — the concrete instructions, each carrying its GOV.UK
  heading in `attrs.source_ref` and its owning convention in `attrs.principle`.

The counts above are rendered from the live graph by the `tl:count` directive, so they
cannot drift.

## Source & licensing

The content is a faithful re-expression of the **GOV.UK style guide**
(https://www.gov.uk/guidance/style-guide), Crown copyright, published under the **Open
Government Licence v3.0**. Downstream use must preserve the OGL attribution in
[`NOTICE`](NOTICE).

## Extending the source

Items are hand-authored static YAML — one file per item, one permanent UID per file.
To add a rule, create the next `SR-00NN.yml` by hand (never renumber an existing one)
and link it with `implements` to its convention. Then:

```sh
tl check --strict      # the graph must stay sound
tl docs                # regenerate docs/spec.md
tl docs --check        # CI gate: docs must match the graph
```
