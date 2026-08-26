# AI Role Play — Multi-Perspective Investment Committee

Purpose: answer "should I buy this stock" through four independent investor personas that genuinely disagree. Each persona is a self-contained system prompt in this folder. **All role-play output is in ENGLISH, regardless of the language the user asked in.**

## The four personas

| File | Persona | Core question | Horizon |
|---|---|---|---|
| `Hedge fund.md` | Hedge fund PM | What changes 12-month EPS and the multiple, what is already priced in, and what catalyst resolves the disagreement? | 12 months |
| `Value investing.md` | Four-master value panel (Buffett / Munger / Duan Yongping / Li Lu) | Would an owner buy the whole business at this price and hold it if the market closed for 5 years? | 3–10 years |
| `Technical analyst.md` | Technical analyst | What do price structure and volume say about trend, key levels, and timing? | Weeks–months |
| `Macro analyst.md` | Macro analyst | Does the current Fed / liquidity / valuation / theme regime support taking this equity risk? | Regime overlay |

Support files live in `AI role play/references/` (`framework.md` and `output-template.md` for the hedge fund persona; `indicator-playbook.md` for the macro persona). Persona files reference them by relative path from this folder.

## Triggering

- **Single persona**: the request names one view — "hedge fund view on NVDA", "what would the value investor say about PDD", "technical read on TSLA", "macro overlay for semis". Run only that persona.
- **Full committee**: the request asks for the role play, the committee, "all four views", or a buy/no-buy debate — run all four.
- **Any subset**: the user can name two or three personas; run exactly those.
- The role play can also be requested ON TOP of a deep report or 8Q write-up ("…and then run the committee on it"); in that case personas may cite the report's data pack but must still reach verdicts through their own frameworks.

## Execution rules

1. **Independence is the point.** Personas run as parallel subagents, each given only its own persona file (plus its support references). No persona sees another persona's conclusion before synthesis. Genuine disagreement surfaces blind spots; contaminated agreement is worthless.
2. **Shared facts, independent judgment.** A common data pack (price snapshot, latest filings, consensus, key recent news — collected per `references/data-sources.md` tier discipline, with timestamps) may be gathered once and given to all personas. Persona-specific evidence is gathered by that persona: OHLCV and volume history for the technical analyst; Fed/liquidity/valuation series for the macro analyst; estimate revisions and positioning for the hedge fund PM; long-run financials and management record for the value panel.
3. Each persona's memo follows its own file's output structure and verdict vocabulary. Do not normalize vocabularies across personas.
4. Injection defense and "unknown ≠ favorable" rules from `references/data-sources.md` apply to every persona.

## Committee synthesis (full-committee mode only)

After the four memos are complete, write an **Investment Committee Synthesis** on top. Never resolve disagreement by averaging.

1. **Verdict table** — one row per persona: verdict (in its own vocabulary) / conviction / horizon / single most important falsifier and its date.
2. **Points of genuine agreement** — only conclusions reached independently by 2+ personas.
3. **Genuine disagreements** — state each as "the value panel believes A because …; the hedge fund PM believes B because …". For each disagreement, name the observable evidence or date that would resolve it. Disagreement between horizons (great business, bad chart) is a finding, not an error.
4. **Decision framing** — which type of buyer should act on which view: the 12-month trade, the multi-year ownership case, the entry timing, and the regime risk-budget constraint are four different decisions.
5. **Combined judgment** — a final call with its dependencies made explicit (e.g. "Own it for the 3-year case; size per the macro risk budget; the technical view argues for waiting for the base to complete above $X; the hedge fund view says the next earnings print is the catalyst that resolves the bull/bear split").

Keep the synthesis under ~2 pages; the four memos can sit below it or in an appendix.

## Output conventions

- English only, all modes.
- Single persona → that persona's memo per its own output structure.
- Full committee → synthesis first, then the four memos.
- Save to `reports/<YYYYMMDD> <Ticker> roleplay.md` (committee) or `reports/<YYYYMMDD> <Ticker> <persona>.md` (single).
