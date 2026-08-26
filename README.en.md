[中文](README.md) | **English**

# Secondary Market Research Agent

**A buy-side single-stock research agent.** Give it a company name or ticker; it runs a fixed nine-step pipeline and produces an auditable equity research report — sources tiered and timestamped, facts separated from judgment, and a valuation whose sensitivity to its own assumptions is stated rather than hidden.

## About

Getting a language model to *write something that looks like equity research* is easy. Getting output you can put in front of an investment committee is not. This repository is an attempt at the second thing, and it is organised around three failure modes that show up in practice:

| Failure mode | How this agent handles it |
|---|---|
| **Invented numbers** — the model fills in plausible-looking financials from memory | Sources are ranked in five tiers (Tier 1 regulatory filings → Tier 5 media). Every material financial figure **must** be supported by a Tier 1 primary document. If it can't be obtained, the report says "not obtained" — no empty table headers, no back-solved values passed off as facts |
| **Facts blended with opinion** — the reader can't tell disclosure from guesswork | Five information classes are kept visibly separate: reported fact / management view / consensus estimate / my estimate / inference. Every analytical judgment is signed "my view" |
| **Valuation as a numbers game** — a 1% change in the discount rate flips the conclusion, and the report doesn't mention it | Three methods with **explicit weights** (scenario 45% / relative 35% / perpetuity DCF 20%), a mandatory discount-rate sensitivity table, and an automatic downgrade to "sensitive to the discount rate" if the verdict label flips |

The agent doesn't guarantee that its conclusions are right. It guarantees that they can be **audited and falsified** — every number traces to a source, every assumption is positioned against a historical base rate, and every forecast carries a range plus a validation date.

Built for [Claude Code](https://claude.com/claude-code): open this repository as the working directory and `CLAUDE.md` loads automatically as the agent's dispatch instructions.

> **Start here** → **[docs/OUTPUT-GUIDE.md](docs/OUTPUT-GUIDE.md)** — what the output looks like, what's in each chapter, how to read it. This is the file to send a colleague first.
>
> Blank structure with field-level annotations → **[docs/report-skeleton.md](docs/report-skeleton.md)**
>
> Note: **finished reports and valuation cases are not version-controlled.** They embed investment conclusions on specific tickers and stay local (see [`.gitignore`](.gitignore)). Every figure in the documentation comes from the synthetic `scripts/dcf.py --example` case and is reproducible.

---

## Four output modes

The agent infers the mode from how you ask. You don't specify it.

| Mode | How you'd ask | Output | Scale |
|---|---|---|---|
| **Deep research report** (default) | "research TSMC", "write me a report on ASML" | Seven chapters + appendices, full evidence chain | 8,000–15,000 words |
| **Earnings deep-dive** | "analyse NVDA's quarter", "TSM 3Q25", "how was Tencent's print" | Nine chapters, treating the print as an event that re-tests the thesis | 5,000–10,000 words |
| **8Q write-up** | "give me an 8Q on ASML", "short memo version" | Judgment condensed into eight fixed questions | 2,500–5,000 words |
| **AI role play** | "hedge fund view on NVDA", "run the committee" | Four independent persona memos + committee synthesis (**English only**) | 1–2 pages per persona / 6–10 pages for the full committee |

Output language follows the language you asked in — except role play, which is always English.

## Execution pipeline (nine steps, none skipped)

```
1. Parse request     Company / ticker / listing / fiscal year-end / mode / language
                     Ambiguous tickers: confirm the primary listing first
2. Industry routing  references/industry-routing.md → 1 primary appendix + up to 2 segment appendices
3. Load the specs    data-sources.md (collection discipline) + financial-definitions.md
                     (measurement conventions) + the selected industry appendices
                     A-share / HK names also load markets-cn-hk.md
4. Collect data      Four parallel tracks: disclosure / expectations / communication / market
                     Every figure carries a source and timestamp; material financials need
                     at least one Tier 1 primary document
5. Forensic check    forensic-accounting.md minimum check set → credibility grade A/B/C/D
                     Grade C → the "undervalued" buy label is disabled
                     Grade D → only avoid / sell conclusions are permitted
6. Analysis          Template chapters + the industry appendix's value-driver tree and KPI dictionary
7. Valuation         scripts/dcf.py: three scenarios × three weighted methods, 5-year horizon
                     Key assumptions annotated with their base-rates.md percentile;
                     anything above the 80th percentile needs a structural reason
8. Writing           output-format.md: conclusion first, verdict box / tearsheet,
                     paragraphs ≤5 lines, precision matched to uncertainty
9. Quality gate      Run the template's checklist; attach the source-and-timestamp list
                     and the valuation assumption summary
```

## Repository layout

```
CLAUDE.md                        Agent dispatch file (mode detection, pipeline, hard rules, file map)
│
references/                      11 specification files — the agent's working manual
├── report-template.md           Deep report: seven-chapter structure and per-chapter requirements
├── earnings-mode.md             Earnings mode: nine-chapter structure and reconciliation protocol
├── 8q-framework.md              8Q skeleton + global prose discipline
├── output-format.md             Layout, number conventions, confidence self-assessment, forecast register
├── data-sources.md              Source tiers, fallback paths, reconciliation, injection defence
├── financial-definitions.md     Revenue / growth / margin / return / per-share conventions
├── valuation-methods.md         Methods, 5-year three-scenario framework, method weights, position sizing
├── base-rates.md                Historical distributions for growth, margins, ROIC (outside view)
├── forensic-accounting.md       Earnings-quality checks and credibility grading
├── industry-routing.md          Industry → industries/*.md routing table
└── markets-cn-hk.md             A-share / HK disclosure, standards, comp-set differences
│
industries/                      20 industry appendices: KPI dictionaries, value-driver trees,
                                 valuation methods, earnings-season focus points
                                 (an appendix's KPI and valuation conventions override the
                                 generic template wherever they conflict)
│
scripts/dcf.py                   Valuation CLI (pure standard library, JSON input)
│
AI role play/                    Four-perspective committee: 4 personas + dispatch rules + support files
.claude/skills/analyze-earnings/ Earnings skill (dispatches earnings-mode + routing + pre-print branch)
│
docs/
├── OUTPUT-GUIDE.md              ★ Output guide — read this first
└── report-skeleton.md           Blank seven-chapter template with field-level requirements
│
workspace/                       Local working directory (valuation cases, intermediates — not tracked)
reports/                         Output directory (not tracked)
```

## Quick start

**Run a report**

Open this repository as the working directory in Claude Code, then just say:

```
research ASML
```

Output goes to `reports/<YYYYMMDD> <company> <mode>.md`; the valuation JSON to `workspace/<ticker>/`. Both directories are gitignored — research output stays local and isn't distributed with the repo.

**Run the valuation calculator on its own**

`scripts/dcf.py` is standalone, has no dependency on the agent, and uses only the Python standard library:

```bash
python3 scripts/dcf.py --example > case.json   # annotated input template
python3 scripts/dcf.py case.json               # prints the report, writes case_output.json
```

It outputs: the method-weighted × probability-weighted fair value across three scenarios, a reverse DCF (what the current price implies), discount-rate sensitivity, expected return / asymmetry ratio / P(loss) / Kelly-lite position reference, and a probability robustness check that pushes the scenario weights to the combination least favourable to the conclusion and reports whether the verdict label flips.

## Method weights (why the DCF only gets 20%)

| Method | Weight | Rationale |
|---|---:|---|
| Scenario-weighted (5-year exit multiple) | **45%** | Every assumption lands on an observable operating variable. Discounts five years with no perpetuity term, so it is the least sensitive to the discount rate |
| Relative valuation (warranted multiple) | **35%** | Benchmarks directly against what the market actually pays for comparable assets. Shares the operating assumptions with the scenario method, so any divergence must come from the multiple judgment itself |
| Perpetuity DCF (Gordon) | **20%** (cap 30%) | A 1% move in WACC shifts the value 30–50%; terminal value routinely accounts for 70%+ of the total. **It isn't down-weighted because it's wrong — it's down-weighted because its errors can't be verified** |
| Reverse DCF | **0** (diagnostic) | Answers "what does the current price imply?" It never produces a fair value and is always shown separately |

The scenario horizon is fixed at **five years** — long enough to span a full product / capital / regulatory cycle. A three-year window misreads cyclical troughs as structural decline and one-off tailwinds as durable capability.

## Known gaps

- Consensus estimates rely on public aggregators (no FactSet / LSEG / Bloomberg entitlement). Aggregator forecast figures **frequently contain order-of-magnitude errors** — I've seen a $181mm revenue estimate rendered as $9bn — so `references/data-sources.md` requires cross-checking at least two sources.
- Alternative data is capped: it can change a confidence level but never a conclusion label on its own.

## Disclaimer

See [DISCLAIMER.md](DISCLAIMER.md). This repository is a research-methodology toolkit, not investment advice; the author is not a licensed investment adviser. All figures in the documentation come from a synthetic case and involve no real company.
