Indicator Playbook
Purpose
Support reference for Analyze Stock Macro Regime. It supplies the state definitions, thresholds, scores, and crisis override that the workflow cites. Apply it in workflow order: Fed setup, liquidity, valuation, dominant theme, combination.
Treat every threshold below as a current-regime calibration, not a constant. Adapt thresholds when market structure changes — a new Fed operating framework, a reserve-regime shift, changed issuance mechanics — and explain material deviations next to the classification they affect.
1. Fed setup classification
Judge both sides of the dual mandate before assigning a state. Classify from direction and 3-month momentum, not single prints. Do not classify from the policy-rate path alone; classify from the data that forces the path.
Labor evidence (inspect all):
	• unemployment rate: level relative to the Fed's full-employment estimate plus its 3-month trend;
	• payrolls: 3-month average; treat persistent downward revisions as an independent weakening signal;
	• initial claims 4-week MA: below 240k healthy; 240–280k softening; above 280k deteriorating;
	• quits and hires: falling quits means fading worker bargaining power; falling hires leads layoffs.
Inflation evidence (inspect all):
	• core PCE YoY and 3-month annualized; treat the 3-month run rate as the leading edge and YoY as the anchor;
	• breadth: share of spending categories running above 3% annualized;
	• wage growth against the roughly 3.5% productivity-consistent pace;
	• shelter versus services ex-shelter: shelter disinflation is mechanical and lagged; services ex-shelter shows the underlying pressure.
Assign exactly one state:
	• Hike — core PCE 3M annualized above 3.5% or re-accelerating with widening breadth; wages above 4.5%; labor tight (claims 4-week MA under 240k, unemployment at or below full employment, quits high). Communication: "not sufficiently restrictive," "further firming may be appropriate," dots drifting up. Equities: multiple compression dominates earnings; longest-duration growth loses most. Transition: two consecutive months of decelerating core momentum, or claims through 240k, → hold with hike bias.
	• Hold with hike bias — core 3M annualized 2.8–3.5% and sticky; breadth mixed; wages 4–4.5%; labor still solid (payrolls 3M average above 100k, claims under 260k). Communication: "prepared to tighten further if appropriate," "higher for longer," no near-term cuts in the dots. Equities: multiples range-bound; earnings must carry the index. Transitions: up → hike on re-acceleration with widening breadth; down → neutral hold after two months of core deceleration with labor intact.
	• Neutral hold — core PCE YoY 2.2–2.8% with the 3M run rate at or below YoY; wages 3.5–4% and converging to the productivity-consistent pace; labor balanced (unemployment stable, payrolls near replacement, claims under 250k, quits and hires normalized). Communication: "well positioned," "risks broadly balanced," patience. Equities: macro fades as the driver; earnings and theme dominate. Transitions: up → hold with hike bias on inflation re-acceleration; down → hold with cut bias when labor risk rises (claims trending above 260k, negative payroll revisions, unemployment ticking up).
	• Hold with cut bias — disinflation on track (core 3M annualized at or below 2.5%) or labor softening faster than inflation cools: unemployment up ~0.3pp from its cycle low, payrolls 3M average below 100k with downward revisions, claims 240–280k, quits falling. Communication: "risks to employment have risen," "gaining confidence," "it will likely be appropriate to begin dialing back restraint." Equities: cut anticipation supports multiples while growth holds; duration and quality cyclicals work. Transitions: → benign cut when cuts begin with growth intact; → defensive or crisis cut if labor cracks (claims above 280k and rising, payrolls near zero) or funding stress confirms.
	• Benign cut — cuts delivered while growth is intact: core inflation converging to 2%, payrolls positive, claims under 260k, credit spreads calm, unemployment rising slowly if at all. The cut is a recalibration toward neutral, not a rescue. Communication: "recalibration," "policy remains restrictive," labor-market strength cited alongside inflation progress. Equities: historically the friendliest state — multiples and breadth expand while EPS holds; do not extrapolate it to all cuts. Transitions: → neutral hold as policy nears neutral; → defensive or crisis cut if growth data break during the cutting cycle.
	• Defensive or crisis cut — cuts forced by deteriorating growth or funding stress: payrolls 3M average near zero or negative, claims above 280k and rising, unemployment up 0.5pp or more from its 12-month low, or confirmed funding stress per Section 6. Communication: 50bp-plus moves, intermeeting action, facilities announced alongside cuts, financial-stability language. Equities: cuts do not offset the shock at first; EPS downgrades and deleveraging dominate. Transition: → a benign path only after the Section 6 all-clear conditions are met.
Benign-cut versus defensive-cut discriminator. Run this table whenever cuts are underway or priced:
| Dimension | Benign cut | Defensive or crisis cut |
|---|---|---|
| Why cuts happen | Inflation converging to 2%; recalibration toward neutral | Growth breaking or funding stress; rescue |
| Growth data | Payrolls positive; claims 4-week MA under 260k | Payrolls near zero or negative; claims above 280k and rising; unemployment +0.5pp off its low |
| Credit spreads | Stable or narrowing; HY OAS under 350bp | Widening fast; HY OAS +150bp or more within a month |
| Curve shape | Gradual bull steepening; front end reprices in orderly steps | Violent bull steepening; the 2-year collapses ahead of the Fed |
| Equity mechanism | Multiple expansion on intact EPS | EPS downgrades plus deleveraging swamp the rate relief |
Treat "the Fed is cutting" as a question, not an answer. Report the current state, the likely next transition, and the evidence that would confirm or falsify it.
2. Liquidity classification
Analyze three layers, then map the combination to one of five states. Rule: quantity explains, price confirms, symptoms corroborate. Do not call crisis from symptoms alone, and do not call ample from quantity alone while the price layer disagrees.
Quantity layer:
	• Fed balance sheet (WALCL): direction versus the announced QT or QE pace;
	• reserve balances (WRESBAL) as a share of nominal GDP: above ~13% ample; 10–13% adequate; below ~10% scarce — the core regime calibration; re-derive the bands if the Fed changes its floor framework;
	• TGA (WTREGEN): rebuilds drain reserves, drawdowns add them; swings above $150B in a month move the system;
	• ON RRP (RRPONTSYD): a buffer — while it holds balances, drains hit the RRP, not reserves; near zero, every drain hits reserves directly;
	• net Treasury issuance: heavy coupon supply absorbs private balance sheet even when reserves look stable.
Price layer — the most honest layer; read it before accepting the quantity story:
	• SOFR minus IORB: below 0 ample; 0–5bp normal; 5–15bp tightening; above 15bp sustained = stress, run the Section 6 override check;
	• EFFR minus IORB: a turn positive signals scarcity migrating into fed funds;
	• standing repo facility: persistent non-quarter-end usage means private repo is pricing above the ceiling.
Symptom layer — confirmation, not initiation:
	• IG OAS: under 100bp calm; 100–150bp tightening; above 150bp stress. HY OAS (BAMLH0A0HYM2): under 350bp calm; 350–500bp tightening; above 500bp stress. Rate of widening matters more than level;
	• VIX regime: under 15 suppressed; 15–25 normal; 25–35 stressed; above 35 crisis-like; a term-structure inversion flags forced hedging;
	• MOVE above ~120: Treasury volatility wide enough to raise haircuts and shrink dealer capacity;
	• Treasury market depth: thinning depth plus a MOVE spike = dysfunction risk, not mere volatility;
	• breadth: a narrowing advance-decline line under a rising index means liquidity is thinning beneath the surface;
	• broad dollar: sharp rallies alongside risk-off signal a global funding squeeze;
	• Bitcoin: a corroborating high-beta liquidity symptom only. Discount it for crypto-specific drivers — ETF flows, regulation, stablecoin supply, leverage unwinds, protocol events. Never let Bitcoin alone set the liquidity state.
Check calendar risks before classifying: quarter-end, tax dates, Treasury cash rebuilding, yen carry positioning, large forced liquidations.
Map to one state:
	• Broad easing — balance sheet or reserves rising, SOFR−IORB at or below 0, spreads narrowing, breadth wide, dollar soft.
	• Improving — drains ending or buffers refilling, SOFR−IORB back inside 0–5bp and falling, spreads off their wides, breadth and Bitcoin recovering.
	• Neutral or mixed — layers disagree without direction: QT ongoing but the ON RRP absorbing it, SOFR−IORB 0–5bp, spreads calm.
	• Tightening — reserves falling toward 10% of GDP with the ON RRP near zero, SOFR−IORB 5–15bp or grinding up, spreads widening slowly, breadth narrowing, dollar firming.
	• Deleveraging or crisis — price layer at stress with symptoms confirming: SOFR−IORB above 15bp sustained, HY OAS widening fast, correlated selling across risk assets. Apply the Section 6 override.
3. Valuation percentile framework
Compute the forward 12-month P/E percentile within 5-, 10-, and 20-year windows. Band on the 10-year percentile and cross-check against the other two:
	• cheap — below the 30th percentile;
	• fair — 30th–60th;
	• elevated — 60th–80th;
	• expensive — 80th–95th;
	• extreme — above the 95th.
Cross-checks:
	• CAPE against its own 20-year percentile; a one-band disagreement with forward P/E means earnings are cyclically inflated or depressed — state which;
	• equity versus bonds: forward earnings yield minus the 10-year UST yield. Above ~3% equities clearly compensated; 1–3% normal; 0–1% thin; below 0 equities yield less than Treasuries — history's expensive tail. Let this move the final band by at most one notch;
	• concentration: when top-10 index weight is near its historical high (above ~30%), also compute the equal-weight forward P/E; if the median stock sits two or more bands cheaper, report both numbers and route the concentration risk to the theme test, not to this band.
Discipline: valuation is an amplifier of outcomes and a constraint on future returns, not a timing tool. Expensive markets rise for years; cheap markets stay cheap without a catalyst. Use valuation to size the consequence of being wrong, not to date the turn.
4. Dominant theme test
Assign one verdict from evidence patterns, not from narrative volume:
	• Accelerating — capex guides raised again; upward revisions broadening to second-order beneficiaries; leadership widening; stocks rise even on in-line results.
	• Intact — revisions positive but flattening; capex steady; price reactions to news roughly symmetric.
	• Selective — winners narrowing to a few names; second-tier beneficiaries missing while leaders beat; dispersion inside the theme rising.
	• Increasingly debated — bulls and bears citing the same data; monetization and ROI questions dominating earnings calls; stocks flat-to-down on good results.
	• Deteriorating — capex growth guided down; downward revisions appearing at the leaders; breadth inside the theme contracting; leaders breaking on in-line results.
	• Broken — a thesis-defining metric contradicted; capex cancellations; leaders falling on strong results and continuing to fall.
Apply the strong-results rule: one leader falling on strong results is a warning; the same reaction repeated across the theme's leaders within a quarter is evidence that expectations have outrun fundamentals — downgrade the verdict at least one notch and shift the burden of proof to the bulls.
Watch price-reaction asymmetry as the leading indicator: when good news is sold harder than bad news is bought, the verdict is migrating down regardless of the next fundamentals print.
5. Scoring and combination
Score each layer after classifying it. Do not score before the crisis check in Section 6.
	• Fed setup: benign cut +2; hold with cut bias +1; neutral hold 0; hold with hike bias −1; hike −2; defensive or crisis cut −2 plus a mandatory override check.
	• Liquidity: broad easing +2; improving +1; neutral or mixed 0; tightening −1; deleveraging or crisis −2 plus the override.
	• Valuation (a constraint — upside capped at +1): cheap +1; fair 0; elevated −1; expensive −2; extreme −2.
	• Theme: accelerating +2; intact +1; selective 0; increasingly debated −1; deteriorating −2; broken −2.
Map the composite (−8 to +7) to a risk-budget stance expressed relative to the investor's normal budget, never as absolute allocations:
	• +4 or higher — aggressive: above the normal risk budget;
	• +1 to +3 — normal;
	• −2 to 0 — reduced: below normal;
	• −5 to −3 — defensive: materially below normal; trim leverage first;
	• −6 or lower — minimum: lowest sustainable exposure.
Valuation cap: when valuation is expensive, the stance may not exceed normal regardless of the composite; when extreme, it may not exceed reduced. Valuation never forces the stance up.
Do not average away a contradiction: when the Fed and liquidity scores disagree by three points or more, present both scenarios instead of the midpoint.
6. Crisis override
The override precedes and outranks all scores. Trigger it when either cluster is confirmed:
	• funding stress: SOFR−IORB above 15bp sustained for a week or more; or HY OAS widening more than 150bp within a month; or Treasury market dysfunction (depth collapse plus a MOVE spike plus failing intermediation);
	• deleveraging symptoms: a correlated selloff across equities, credit, and commodities; gold and yen bid; Bitcoin crashing with other high-beta assets — the pattern of forced selling, not rotation.
On trigger:
	1. Ignore the composite score, the Fed state, and valuation. Cheap gets cheaper in a deleveraging.
	2. Cut gross exposure first — both sides — before adjusting net. Correlations converge and hedges pay less than expected.
	3. Do not buy rate cuts delivered inside the stress window; classify them as defensive.
Re-enter only when all three all-clear conditions hold:
	• spread normalization: HY OAS retraces at least half its widening or narrows for 15-plus sessions, and SOFR−IORB is back below 5bp;
	• policy response delivered and transmitting: a facility or cut that funding spreads visibly respond to;
	• basing behavior: the index holds a prior low on a retest with improving breadth, and leaders stop making new lows.
Re-add exposure in steps, not in one move. Record the trigger date and the all-clear date in the output.
7. Monitoring cadence
| Indicator | Source | Frequency | Alert threshold |
|---|---|---|---|
| Fed total assets | FRED WALCL | Weekly (Wed) | Direction change versus announced QT/QE pace |
| Reserve balances | FRED WRESBAL | Weekly | Below 11% of GDP watch; below 10% scarce |
| TGA | FRED WTREGEN | Daily | Swing above $150B within a month |
| ON RRP | FRED RRPONTSYD | Daily | Approaching zero — buffer exhausted |
| SOFR − IORB | FRED SOFR, IORB | Daily | Above 5bp tightening; above 15bp sustained = override |
| EFFR − IORB | FRED EFFR, IORB | Daily | Turns positive |
| Standing repo facility | New York Fed | Daily | Persistent non-quarter-end usage |
| HY OAS | FRED BAMLH0A0HYM2 | Daily | +150bp in a month = override; above 500bp stress |
| IG OAS | FRED BAMLC0A0CM | Daily | Above 150bp stress |
| VIX | CBOE | Daily | Regime shift through 25; term-structure inversion |
| MOVE | ICE BofA | Daily | Above 120 |
| Treasury market depth | New York Fed / dealer data | Weekly | Depth collapse alongside a MOVE spike |
| Core PCE | FRED PCEPILFE | Monthly | 3M annualized crossing 2.5% or 3.5% |
| Payrolls | FRED PAYEMS | Monthly | 3M average below 100k; persistent negative revisions |
| Claims 4-week MA | FRED IC4WSA | Weekly | Above 240k; above 280k |
| Unemployment | FRED UNRATE | Monthly | +0.5pp above its 12-month low |
| Quits rate | FRED JTSQUR | Monthly | Sustained decline below the pre-tightening norm |
| 2s10s curve | FRED T10Y2Y | Daily | Rapid bull steepening out of inversion |
| Broad dollar | FRED DTWEXBGS | Daily | Sharp rally during risk-off |
| Bitcoin | Market data | Daily | Drawdown above 20% in days alongside equity selling |
| Forward P/E percentile | LSEG / FactSet / S&P | Weekly | Band change per Section 3 |
| Top-10 index weight | Index provider | Monthly | New concentration high |
Quality gate
Thresholds here are current-regime calibrations, not constants. Adapt them when market structure changes — a new Fed framework, a reserve-regime shift, a structurally empty ON RRP, changed issuance mechanics — and explain material deviations in the output.
Before finalizing a classification pass, verify that it:
	• assigns exactly one state per layer and shows the evidence behind each;
	• distinguishes benign from defensive cuts with the discriminator table, not the rate path;
	• reads the liquidity price layer before accepting the quantity story;
	• uses Bitcoin as corroboration only, with its crypto-specific caveats stated;
	• treats valuation as amplifier and constraint, never as a timing signal;
	• applies the strong-results rule to the theme verdict;
	• runs the crisis override before adding any scores;
	• expresses the stance relative to the investor's normal risk budget;
	• states, for every classification, the evidence that would falsify it.
