Analyze Stock as a Business Owner
Objective
Produce an owner's verdict on a stock over a 3–10 year horizon. Determine:
	1. what makes this business worth owning at all;
	2. whether the advantage is durable and what protects it;
	3. every credible path by which the investment dies;
	4. whether the next 10 years structurally favor or erode the business;
	5. what a rational owner would pay versus what the market is asking.
Run the target through four master lenses in fixed order: Duan Yongping (business essence), Buffett (moat and valuation), Munger (inversion and veto), Li Lu (civilizational trend and 10-year certainty). Each lens must close with a conclusion and a confidence level before the next lens opens.
Treat the exercise as buying the entire company with your own capital and no exit for years, not as renting a ticker. Do not reduce the conclusion to "good company" or "cheap stock." Force a single verdict — buy, hold, or pass — with a price range attached to each action.
Select the task mode
Infer one mode from the request:
	• Full analysis: run the complete four-lens workflow.
	• Valuation refresh: keep the prior business and moat conclusions, rerun step 6 with current prices and estimates.
	• Thesis update: preserve the prior synthesis table and show only the rows that changed and why.
	• Comparison: run two or more names through identical lenses, constraints, and currency frames; never compare a terminal value against a scenario-only number.
	• Watchlist triage: run steps 1, 3, and 5 only; output owns-further-work or discard, not a verdict.
Resolve ambiguous securities before making company-specific claims.
Information-quality pre-assessment
Grade the information environment before analyzing. The grade sets the dominant failure mode and caps final certainty.
	• Grade A: mature company, dense coverage, long filing history. The data are not the risk; consensus mirroring is. Stress-test in the opposite direction of the prevailing story.
	• Grade B: 1–3 years of public data. Tag every estimate with a confidence level. Do not extrapolate a short operating history into a terminal-value claim.
	• Grade C: sparse or pre-consensus information. Switch to first-principles questioning: who pays and why; what alternatives do customers have; could $1bn of capital replicate this; what do management's actual decisions reveal about what they believe.
Close the pre-assessment with the bias self-audit and record the answers:
	1. Would my conclusion flip if the available data were halved?
	2. If my analysis tracks consensus, what exactly is my edge?
Evidence rules
	• Browse for current data. State the ticker, listing, currency, price, price date, and analysis cutoff.
	• Prioritize primary sources: filings, annual letters, call transcripts, official operating and industry statistics. Follow the source tiers in ../references/data-sources.md (repository root).
	• Distinguish reported fact, management claim, consensus estimate, and analyst inference. Cite material claims near the claim.
	• Treat missing disclosure as unknown, not favorable. Prefer ranges to false precision. Never invent figures.
	• Use at least 5 years of financial history when it exists; explain any period excluded as non-comparable.
Workflow
1. Define the business essence (Duan Yongping)
Write one sentence answering: what makes this business worth owning? If the sentence needs a second clause to be true, the business is not yet understood.
Then record:
	• revenue decomposition: who pays, for what, at what frequency, with what pricing mechanism;
	• business-model taxonomy: product sale, subscription, platform take-rate, aggregation, licensing, or hybrid — and which element earns the profit;
	• stickiness and lock-in: what the customer would lose by leaving, measured in money, data, habit, or integration cost;
	• "right business, right people": whether the economics and the culture reinforce or fight each other.
Apply two diagnostics and record explicit answers:
	1. If the CEO retires tomorrow, does the advantage persist?
	2. If the market closed for 5 years, would I hold at this price?
A "no" on either is not an automatic pass, but it must reappear in the failure-path table and the verdict rationale.
2. Test the moat (Buffett)
Run the five moat tests. Score each pass, partial, or fail with one line of evidence:
	1. pricing power: can it raise prices without losing volume;
	2. switching costs: quantify what leaving costs the customer;
	3. network effects: does each user make the product better for others;
	4. scale economies: does size lower unit cost in a way entrants cannot match;
	5. patents or technology lead: how long before the lead is replicated.
Then state the moat trajectory: widening, stable, or narrowing over the past 5 years, and the expected direction over the next 10. A wide but narrowing moat is a melting ice cube; price it as one. Do not accept brand recognition or market share as a moat without one of the five mechanisms behind it.
3. Invert (Munger)
Before asking why this works, complete the failure analysis:
	• Build a failure-path table: every credible mechanism of permanent capital loss, each with mechanism, probability, and severity. Include the mundane paths — margin compression, channel shift, capital misallocation — not only the dramatic ones.
	• List historical analogs: similar companies that died or stagnated, and whether the killing mechanism applies here.
	• Run the cognitive bias audit on your own draft: narrative seduction, anchoring on the current price, survivorship in the analog set, consensus mirroring.
	• Answer directly: why would smart investors avoid or short this today? If no serious bear case exists, you have not found it yet.
Apply the red-flag veto list. Any confirmed item vetoes a buy verdict regardless of upside:
	1. accounting credibility: revenue recognition games, cash flow diverging from earnings, auditor changes — apply the ../references/forensic-accounting.md discipline (repository root) here;
	2. governance: controlling-shareholder extraction, related-party transactions, serial dilution;
	3. single point of failure: one customer, one supplier, one regulator, or one key person whose loss breaks the model.
Record the veto check result explicitly, even when clean.
4. Judge management
Assess management as capital allocators, not as storytellers:
	• trace 5–10 years of allocation decisions: buybacks and the prices paid, acquisitions and their outcomes, dividends versus reinvestment returns;
	• check incentive alignment: insider ownership, compensation structure, and whether pay tracks per-share value or empire size;
	• test candor: compare what management promised in past bad years with what happened;
	• for Grade C names, weight revealed decisions over stated strategy.
Classify management as owner-operators, competent stewards, or agents working for themselves. An agent classification caps position conviction and must appear in the synthesis table.
5. Test the civilizational trend and 10-year certainty (Li Lu)
Place the business inside its era:
	• Is the industry in a paradigm shift? Name the shift and the direction of the value migration.
	• Find the historical parallel from prior technology revolutions — rail, electricity, auto, internet — and state whether this company holds the position that captured value or the position that got commoditized.
	• Estimate the TAM ceiling and how much of the runway is already consumed.
	• Locate the company's value-chain position: does it own the bottleneck or rent access to someone else's?
Apply the diagnostic and record the answer: in 20 years, is this the Standard Oil of its era or the 3Com of today?
Enforce the certainty rule: a cheap stock with insufficient 10-year certainty is capped at hold. Cheapness buys a margin of safety, not a substitute for durability.
6. Value the business (Buffett)
Normalize the earnings base before any multiple or formula touches it:
	• start from owner earnings: reported net income adjusted for maintenance capex versus depreciation, stock compensation, working-capital games, and one-offs;
	• use through-cycle margins, not peak-year margins, for cyclical businesses;
	• reconcile the share count for pending dilution.
Build the 3-scenario, 3-year valuation: bear, base, and bull, each with an earnings path, an exit multiple justified by the moat trajectory, and a subjective probability; probabilities sum to 100%. Scenario arithmetic may reuse ../scripts/dcf.py (repository root); show the inputs in the memo either way.
For concentration candidates only, add a 10-year terminal value using terminal P/E = (1 − g/ROIC) / (r − g), under three hard constraints:
	1. C1 — currency alignment: r and g must be in the same currency frame. Baseline r ≈ 8% for CNY earnings, ≈ 10% for USD/HKD. Cap perpetual g at 2% for CNY and 4% for USD; nominal GDP is the ceiling, not a suggestion.
	2. C2 — spread floor: if r − g < 5 points, the terminal formula is unstable; mark the name "scenario-only" and publish no terminal value.
	3. C3 — discrete risks: delisting, VIE structure collapse, war, expropriation enter the scenario probabilities, never the discount rate. Inflating r to "account for" a binary risk destroys the arithmetic and hides the risk.
Apply the diagnostic and record the answer: if my discount rate is wrong by 2 points, does the conclusion invert? If yes, the verdict rests on precision you do not have; widen the required margin of safety.
Convert the scenarios into three prices: the buy-below price, the hold range, and the sell-above or pass level.
7. Synthesize and force the verdict
Assemble the synthesis table, one row each: business quality, moat, management, largest tail risk, civilizational tailwind, valuation. Each row carries a one-line conclusion and a confidence percentage.
Add one simulated line from each master, in his voice, on this specific stock — Duan on the business, Buffett on price versus value, Munger on what kills it, Li Lu on the decade. Keep each to a single sentence; the quote must be falsifiable, not atmospheric.
State two numbers and do not merge them:
	• analysis confidence: how sound this reasoning is given the available data;
	• investment certainty: how likely the thesis plays out over the horizon.
Cap them by information grade — A: analysis 85–95%, certainty 70–80%; B: 60–75% and 40–60%; C: 40–55% and 30–45%. High analysis confidence with low investment certainty is a legitimate and common state; report it as such.
Deliver the forced verdict: buy, hold, or pass, with the price range for each action. Then complete the action matrix:
	• long-only investor considering entry: act at what price, size within what conviction band;
	• current holder: hold, trim, or add, and at what levels;
	• exit signal: the observable event or threshold that ends the thesis;
	• add signal: the price or evidence that justifies increasing the position.
Do not hedge the verdict with "it depends." The scenarios already contain the dependency; the verdict is the probability-weighted decision.
Quality gate
Before finalizing, verify that the analysis:
	• leads with the verdict and price ranges, not company history;
	• contains a one-sentence business definition that survives the CEO-retirement and closed-market diagnostics;
	• scores all five moat tests with evidence and states the moat trajectory in both windows;
	• includes a failure-path table, at least one historical analog, and an explicit red-flag veto check;
	• enforces the veto: no buy verdict coexists with a confirmed red flag;
	• enforces the certainty cap: no buy verdict on a cheap stock with insufficient 10-year certainty;
	• obeys C1, C2, and C3 in every terminal-value calculation, or publishes scenario-only;
	• answers the discount-rate inversion diagnostic explicitly;
	• states analysis confidence and investment certainty as separate numbers within the grade caps;
	• includes the strongest bear case in the market's own words, not a strawman;
	• contains no both-sides hedging in the verdict.
Output structure
Write the memo in English only. Order:
	1. verdict line: buy, hold, or pass, with the price range for each action and both confidence numbers;
	2. as-of line: ticker, listing, currency, price, date, information grade;
	3. one-sentence business definition;
	4. synthesis table (six rows, conclusion plus confidence);
	5. four master quotes, one line each;
	6. moat scores and trajectory;
	7. failure-path table and veto check;
	8. valuation: three scenarios with probabilities, terminal value or scenario-only marker, constraint compliance;
	9. action matrix with exit and add signals;
	10. what is still unknowable, and the next evidence that would move the verdict.
Keep facts, management claims, and inferences visibly distinct throughout.
Update mode
When updating a prior analysis:
	• preserve the prior synthesis table, price ranges, and confidence numbers as the baseline;
	• show prior view → new evidence → revised view for every row that moved;
	• distinguish a change in the business from a change in the price; only the first can change the business-quality, moat, or certainty rows;
	• re-run the veto check and the certainty cap on every update, even when the request is only a price refresh;
	• do not rewrite prior reasoning to fit the new verdict.
