# Framework Reference: Scoring, Causal Bridges, Sector Adaptations, Setup Matrix

Apply these definitions verbatim in every analysis. Do not redefine a grade to fit a stock. When a grade does not fit, assign the nearest state and record the mismatch instead of bending the definition.

## 1. EPS revision states

Score the likely direction and breadth of consensus 12-month forward EPS revisions over the forecast window. Score revisions, not reported growth: a company growing 30% against estimates assuming 35% is a downgrade state.

| State | Definition | Cumulative 12M revision |
|-------|------------|-------------------------|
| U2 | Broad upgrades across multiple independent drivers | likely > +10% |
| U1 | Modest upgrades, narrower driver base | +3% to +10% |
| N | Estimates roughly correct | within ±3% |
| D1 | Modest downgrades | −3% to −10% |
| D2 | Broad downgrades across multiple drivers | worse than −10% |

Meet the evidence bar before assigning a state. When evidence is mixed, assign toward N and record what would move the grade.

**U2** — Evidence bar: at least two independent ledger variables accelerating versus what consensus models assume, with at least one already confirmed in reported financials, not only in KPIs or management claims. Typical pattern: volume and price/mix rising together, incremental margins expanding, raise-and-beat guidance cadence. False positives: demand pull-forward graded as structural; easy year-ago comparisons read as acceleration; a single large order or contract annualized into a trend.

**U1** — Evidence bar: one dominant variable improving with a verified or supported evidence state, and no material offsetting variable deteriorating. Typical pattern: steady low-single-digit beats, guidance nudged up, revision breadth positive but concentrated in one line item. False positives: beats produced by tax rate, FX, buybacks, or one-offs rather than operations; cost cuts graded as demand strength.

**N** — Evidence bar: variables tracking in line; beats and misses small and offsetting; revision breadth near zero for 90+ days. Typical pattern: reiterated guidance, stable consensus, price driven by the multiple. False positives: quiet estimates masking a decelerating leading indicator; "in line" preserved only by a bar that has already been cut.

**D1** — Evidence bar: the dominant variable decelerating versus consensus assumptions, or a secondary variable deteriorating with no offset. Typical pattern: guidance "maintained" while quality deteriorates underneath it (mix, pricing, backlog); shrinking beats; whisper above the print. False positives: one soft quarter in a noisy series; a transient cost spike graded as demand weakness.

**D2** — Evidence bar: broad deterioration across independent variables, or the dominant variable breaking with structural or cyclical persistence, visible in reported financials. Typical pattern: guidance cut, revision breadth strongly negative, incremental margins compressing on decelerating revenue. False positives: kitchen-sink resets that mark the estimate trough; cyclical troughs graded as structural decline.

## 2. Narrative score

Score the market's compressed causal belief about the stock, not news sentiment.

| Score | Definition |
|-------|------------|
| +2 | Strengthening narrative, financially confirmed: the story is broadening and reported numbers validate it |
| +1 | Improving narrative, multiple-only: the story is gaining adherents but earnings have not yet confirmed it |
| 0 | Stable or contested: no dominant direction, or bull and bear stories offset |
| −1 | Deteriorating: the story is losing adherents; burden of proof sits on the bulls |
| −2 | Broken or financially contradicted: reported numbers refute the story |

Tag every score with:
- Momentum: improving, stable, or worsening. Score the first derivative separately from the level; a +1 worsening is a different setup from a +1 improving.
- Half-life: event-driven (weeks), medium-cycle (quarters), or structural (years). Match holding period and catalyst cadence to the half-life. Do not run a structural thesis on an event-driven narrative.

Burden-of-proof rules:
- At +2 and +1, the bears own the burden: the stock punishes them until reported numbers contradict the story.
- At −1 and −2, the bulls own the burden: reiterations, buybacks, and conference commentary do not clear it; only financial confirmation does.
- At 0, assign the burden to whichever side needs the next data point, and name the release that decides it.
- A narrative that cannot be financially confirmed or contradicted within the forecast window is unfalsifiable; cap its contribution to the setup at ±1.

## 3. Durability grades

Grade every ledger variable:

| Grade | Expected half-life | Estimate persistence |
|-------|--------------------|----------------------|
| Structural | years | Full flow-through into out-year estimates; compounds |
| Cyclical | 2–8 quarters | Flows into the 12M window; fade it beyond the cycle turn |
| Transient | 1–2 quarters | Moves the next print, not the run-rate; exclude from out-year revisions |
| One-off | single period | Strip from the EPS basis; zero persistence |

Treat a durability grade as a claim about persistence, not about size. A large one-off moves no estimate beyond its quarter; a small structural variable compounds. When management calls an item one-off for the third consecutive quarter, regrade it cyclical or structural.

## 4. Causal bridge templates

Decompose every material variable through the standard bridge:
volume × price/mix/take rate → revenue → gross profit → operating profit → pretax profit → net income → diluted EPS

Sector templates:
- **Subscription software**: NRR × seat/customer growth → net new ARR → recognized revenue (with lag) → gross margin (hosting, support) → S&M efficiency → operating margin → EPS. Revisions hide in: SBC and the resulting share count, deferred-revenue timing, FX on international ARR.
- **Semiconductors**: units × ASP × cycle position → revenue → utilization and mix → gross margin → opex leverage → EPS. Revisions hide in: inventory write-downs and reversals, tax-rate jurisdiction mix, one-time licensing income.
- **Banks**: earning assets × NIM − provisions ± fee income → pre-provision profit → net income; capital return sets the share count → EPS. Revisions hide in: provision assumptions, buyback pace, rate marks and AOCI.
- **Consumer**: traffic × ticket × mix → comparable sales → gross margin (freight, promo, shrink) → SG&A leverage → EPS. Revisions hide in: FX translation, lease accounting, 53rd-week and calendar effects.
- **Platform/internet**: users × monetization per user × take rate → revenue → content and infrastructure cost → operating margin → EPS. Revisions hide in: SBC, other income and investment marks, tax rate on foreign earnings.

Before attributing any beat or miss to operations, check the below-the-line items where revisions usually hide: tax rate, diluted share count, FX, and stock compensation. A beat driven by these is a quality downgrade, not an upgrade.

## 5. Setup matrix

Map EPS state × narrative score × pricing/positioning into one classification. Pricing/positioning enters as two inputs: hurdle versus ledger (what the reverse-engineered price requires versus what the variables support) and crowding.

| EPS state | Narrative score | Pricing/positioning | Classification |
|-----------|-----------------|---------------------|----------------|
| U1/U2 | +1/+2 | Hurdle below ledger; not crowded | Clean Long |
| U1/U2 forming | −1/0 | Pessimism priced; hurdle low | Contrarian Long |
| N | +1/+2 improving | Multiple expanding without EPS support | Narrative-Only / Tactical |
| N | 0 | Hurdle ≈ ledger; no dated catalyst | Wait / Random-Walk Candidate |
| Any, unresolvable | Contested or unfalsifiable | Distribution too wide to underwrite | Avoid |
| D1 | 0/−1 | Hurdle above ledger; dated catalyst inside 0–3M | Tactical Short |
| D2 | −1/−2 | Break not yet fully priced; borrow gate passed | Structural Short |
| Correctly analyzed, any | Any | Fully priced, crowded, or catalyst beyond horizon | Correct View, Bad Trade / No Trade |

**Clean Long**
- Entry: U1/U2 with verified or supported evidence, narrative +1/+2, hurdle below the ledger, crowding not extreme.
- Must be true: the dominant variable keeps confirming at each observation date; revisions arrive before the narrative saturates.
- Typical failure: buying after the revision cycle is priced; the last upgrade marks the top.
- Exit/stop: exit on one EPS grade down or narrative momentum turning worsening; do not average into a broken ledger.
- Holding period: 2–4 quarters, aligned to the revision cycle.

**Contrarian Long**
- Entry: U1/U2 forming while the narrative sits at −1/0; the market has not conceded; the hurdle implies little improvement.
- Must be true: a dated catalyst forces financial confirmation the narrative cannot ignore.
- Typical failure: being early — the EPS inflection is real but arrives after the catalyst window; value-trap drift.
- Exit/stop: exit if the confirming catalyst passes without moving revisions or narrative; time-stop after two missed evidence dates.
- Holding period: 2–6 quarters; size smaller until first confirmation.

**Narrative-Only / Tactical**
- Entry: narrative +1/+2 and improving, EPS state N; the multiple is the only engine.
- Must be true: momentum stays improving and no financial contradiction lands during the hold.
- Typical failure: holding through the print that tests the story; treating a multiple trade as a thesis.
- Exit/stop: exit on momentum flattening or at the first confirmation event, whichever comes first; hard stop on financial contradiction.
- Holding period: weeks, matched to the event-driven half-life.

**Wait / Random-Walk Candidate**
- Entry: no position. N state, narrative 0, hurdle ≈ ledger; near-term path is unpriceable noise.
- Must be true to stay out: no ledger variable approaching a confirm or falsify threshold.
- Typical failure: manufacturing a thesis out of boredom; labeling Wait to avoid a call the evidence already supports.
- Exit/stop: re-classify when any variable changes evidence state or a dated catalyst appears.
- Holding period: n/a; set the next review date.

**Avoid**
- Entry: no position at any currently offered price. The distribution is unpriceable: unfalsifiable narrative, binary outcome without edge, or unreliable disclosure.
- Must be true: the impediment to underwriting persists.
- Typical failure: confusing Avoid with a short; an unanalyzable stock can still double.
- Exit/stop: re-classify only when disclosure or setup structure improves.
- Holding period: n/a.

**Tactical Short**
- Entry: D1, narrative 0/−1, hurdle above ledger, dated catalyst inside 0–3 months, borrow-cost gate passed.
- Must be true: the catalyst prints below the whisper, not merely below consensus.
- Typical failure: right on the quarter, wrong on the reaction — the low bar was already priced; squeeze on crowded shorts.
- Exit/stop: cover on the catalyst regardless of outcome unless it re-dates; hard stop above the level that implies the variable re-accelerated.
- Holding period: weeks to one quarter.

**Structural Short**
- Entry: D2 with structural-durability deterioration, narrative −1/−2 but not yet fully priced, borrow-cost gate passed, no near-term positive catalyst.
- Must be true: each reporting period confirms the decline; no credible reset (new management, balance-sheet fix, take-out) intervenes.
- Typical failure: valuation-only shorting of a declining but cheap business; squeezes and buyout risk on high short interest.
- Exit/stop: cover on one EPS grade up, on the decline thesis moving to disproved, or on rising take-out risk; respect the asymmetry — short losses are unbounded.
- Holding period: 2–4 quarters, resized after each confirmation.

**Correct View, Bad Trade / No Trade**
- Entry: no position despite a correct fundamental view.
- Must be true: at least one disqualifier holds — fully priced, crowded, catalyst beyond the horizon, or unacceptable path dependency.
- Typical failure: overriding the disqualifier because the work was good; the market pays for unpriced correctness, not correctness.
- Exit/stop: re-classify when the disqualifier clears — price resets, crowding unwinds, or the catalyst re-dates inside the window.
- Holding period: n/a; monitor the disqualifier, not the thesis.

Modifier rules — apply after the base classification, in this order:
1. Crowding penalty: when positioning is one-sided against the intended direction, downgrade one notch toward Wait / Random-Walk Candidate or cut intended size; crowding converts small disappointments into large price moves.
2. Catalyst-distance penalty: if the nearest thesis-relevant catalyst sits beyond 6 months, downgrade active classifications one notch; beyond the 12-month window, re-classify as Correct View, Bad Trade / No Trade.
3. Valuation-extreme override: at valuation extremes versus the stock's own history and sector, cap the setup — no Clean Long at an extreme premium without U2, no Structural Short at an extreme discount without D2.
4. Borrow-cost gate: for any short, verify borrow availability and cost before classification; when annualized borrow cost consumes a material share of expected downside, or recall risk is high, downgrade to Avoid regardless of EPS state.

## 6. Sector adaptations

| Sector | Ledger variables that dominate | Whisper conventions | Revision seasonality |
|--------|-------------------------------|---------------------|----------------------|
| Software | NRR, net new ARR, seat growth, S&M efficiency | Buyside whisper sits above guidance; a beat-and-raise below the ARR whisper trades down | Conservative fiscal-year-start guides; upgrades cluster in H2 |
| Semis | Bookings, backlog, ASP, utilization, inventory | Cycle whispers lead prints by 1–2 quarters; distributor and peer prints set the bar | Revisions herd around cycle turns; sector moves swamp single names |
| Banks | NIM trajectory, loan growth, provisions, buyback pace | Whisper keys off NII guidance and the rate path, not EPS | Revisions cluster around FOMC shifts and annual stress-test/capital-return dates |
| Consumer | Traffic, ticket, comp sales, promo intensity, freight | Card and foot-traffic data set the whisper before the print | Holiday-quarter guidance dominates the year; weather and calendar shifts pollute single quarters |
| Industrials/cyclicals | Orders, backlog, book-to-bill, price/cost spread | Short-cycle orders whispered off PMIs and peer prints | Revisions lag PMIs by roughly one quarter; annual guides reset in Q4 prints |
| Healthcare | Volume/utilization, pricing, pipeline and approval dates, payer mix | Script data and trial-readout handicapping set the whisper | Event-driven around FDA dates; January conference guidance resets the year |
| Platforms/internet | User growth, engagement, ad pricing or take rate, SBC | Third-party engagement trackers set the whisper; in-line users with soft monetization misses it | Q4 ad seasonality; annual frameworks reset at Q4/Q1 prints |
| Energy | Production volumes, realized price versus strip, capex discipline, reserve replacement | The strip sets consensus mechanically; the whisper is about capital discipline, not EPS | Revisions track the commodity strip continuously; EPS beats on price alone are not upgrades |

## 7. Usage rules

- Grade the EPS state and narrative score independently before consulting the matrix. Do not back-fit grades to a preferred classification.
- When two classifications fit, choose the one with the tighter falsifier and state why.
- Re-run the matrix at every evidence date named in the update rule. A classification without a next review date is stale.
