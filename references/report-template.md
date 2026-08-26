# 报告模板：

严格按以下章节顺序输出。**撰写前先读 `references/output-format.md`**（结论框/Tearsheet/本章要点/数字规范/football field 画法均在其中）。没有的数据按报告语言写"未获取到"或"Not obtained"，不要留空表头。

格式约定：标题按报告语言生成；中文用 `# 公司名（代码）个股投资研究报告`，英文用 `# Company (Ticker) Equity Research Report`。副标题标"撰写日期 / 数据截止日 / 报告币种"或英文等价 `"Report date / Data cutoff / Reporting currency"`

1. Business description
Build an evidence-based map of how a company makes money, which businesses drive its current financials, and which variables can drive future revenue and profit. Make the result understandable to a reader with no finance or industry background.
Set the Scope
    1. Identify the exact company, ticker, listing, fiscal year-end, reporting currency, analysis date, and requested language.
    2. Use the latest completed fiscal year as the default basis for revenue mix and the latest reported period for recent trends. Label any mixed periods explicitly.
    3. Prefer the company's reportable operating segments. Do not silently mix reportable segments with products, geographies, customer types, or management-created categories.
    4. State material scope limitations rather than blocking the analysis. Use N/D for information the company does not disclose.
    5. Keep the analysis focused on the business model and segment economics. Do not add valuation or an investment recommendation unless the user requests it.
Research the Evidence
Use current information when the user asks about a current company. If the user supplies filings or data, use them first and supplement only when necessary.
Apply this source hierarchy:
    1. Annual reports, 10-K/20-F filings, and segment footnotes
    2. 10-Q/6-K filings, earnings releases, and financial supplements
    3. Investor presentations, investor-day materials, and earnings calls
    4. Company product documentation and official customer examples
    5. Consensus estimates and reputable industry sources for forecasts or TAM
Record source dates and cite factual claims. Distinguish:
    • Reported fact: disclosed by the company or another source
    • Management view: guidance, target, or qualitative claim
    • Consensus estimate: externally compiled forecast
    • Analytical estimate: derived by the analyst
    • Inference: interpretation supported by evidence but not explicitly disclosed
Read references/financial-definitions.md before calculating segment mix, growth, margins, or estimates.
Build the Segment Financial Map
    1. Reconcile segment revenue with consolidated revenue before calculating shares.
    2. Use external segment revenue where available. Identify intersegment revenue, eliminations, corporate items, and unallocated costs.
    3. Use restated historical segments after reporting changes. If history is not recast, mark the periods non-comparable and avoid a misleading CAGR.
    4. Calculate revenue mix, true 3-year CAGR, latest-year growth, latest margin, and 3-year margin change using the definitions in the reference.
    5. Label the exact margin measure. Prefer segment operating margin; otherwise use disclosed segment gross margin or a clearly defined segment-profit margin. Never present different measures as directly comparable without a warning.
    6. Note acquisitions, disposals, currency effects, accounting changes, and 53-week years that materially affect growth.
Explain Each Business in Plain Language
Answer the same questions for every material segment:
    1. What product or service does it sell?
    2. Who buys it?
    3. What customer problem does it solve?
    4. Why does the customer choose it instead of an alternative?
    5. How does the company charge: subscription, usage, unit sale, transaction fee, advertising, licensing, or project work?
    6. What makes the segment economically different from the others?
Use this explanation pattern when helpful:
    You can think of this business as __. When a customer needs to __, it uses __. The company earns money by __.
Define unavoidable jargon on first use. Add one or two concrete examples for complex businesses, but do not let examples substitute for the actual revenue model.
Translate Growth Stories into Financial Drivers
Analyze revenue growth separately from margin expansion.
For each segment, test these revenue drivers:
    • Market or TAM growth
    • Market-share gain or loss
    • Customer growth and retention
    • Usage or units per customer
    • Price and product mix
    • New products, customer groups, or geographies
    • Acquisitions and divestitures
For each material driver, state:
    1. Mechanism — how it changes a measurable operating variable
    2. Evidence — historical trend, company disclosure, or external data
    3. Timing — near term, 2–3 years, or longer term
    4. Constraint — competition, capacity, regulation, cannibalization, execution, or cyclicality
    5. Financial landing point — revenue growth, gross margin, operating margin, or cash generation
Do not equate TAM growth with company growth. Explain the conversion chain from market demand to customers or usage, then to company revenue.
Analyze margin expansion through scale, pricing, product mix, utilization, automation, distribution efficiency, procurement, or lower investment intensity. Do not call margin expansion a source of revenue growth.
Estimate the next 2–3 years of segment revenue growth as a range or directional category unless reliable forecasts justify precision. Label the estimate as company guidance, consensus, or analytical; assign High, Medium, or Low confidence; and show the main assumptions.
Explain How the Segments Fit Together
Test for, rather than assume, connections through:
    • Shared customers and cross-selling
    • Shared distribution or customer acquisition
    • Shared technology, data, infrastructure, or intellectual property
    • Product dependencies and bundling
    • Ecosystem or network effects
    • Shared procurement, manufacturing, or logistics
    • Brand reinforcement
    • Capital allocation from mature businesses to growth businesses
Also identify cannibalization, channel conflict, resource competition, incompatible economics, or businesses that are largely independent. Describe the relationship as a flywheel only when the links are supported by evidence.
Produce the Analysis
Follow references/output-format.md. Always include:
    1. A plain-language company snapshot
    2. **One** business-line financial summary table (see "拆一次" rule below)
    3. A structured explanation of each material segment, including its unit economics
    4. The relationships among segments
    5. A consolidated growth and profit conclusion
    6. Data limitations, estimate labels, and source notes

**"拆一次" 规则（硬性）**：整章**只允许出现一次业务拆分**，且以**业务逻辑**为轴（这条业务卖什么、向谁收钱、单位经济如何），不是以披露口径为轴。常见错误是先按"可报告分部/收入类型"拆一张表，再按"渠道/地域/客户类型"拆第二张表，最后再单独写一节单位经济——三节讲同一件事，读者要自己拼。正确做法：

- 选一个**能解释盈利机制**的拆分维度做主表（通常是可报告分部；单一分部公司用产品线或收费方式）。
- 公司披露的其他口径（商业/政府、美国/国际、渠道 mix）**作为主表的补充列或表下 2–4 行注释**出现，不另起一节。用它们回答"增长的质量如何"，而不是重复"收入有多少"。
- **单位经济（量 × 价 × 单位成本 × 单位毛利）并入该业务线的说明**，不单列一节——它是这条业务线的经济学，不是一个独立话题。
- 若某个口径差异会改变增长结论（例如政府研究收入混入商业收入、并购贡献混入有机增长），把**剔除后的口径**直接写进主表的"历史增长"列，原始口径放括号。

**多年财务全貌表（必附，与业务线主表并列）**：覆盖最近 3–5 个完整财年 + 最新中期，逐行给出收入、成本、各项费用、经营利润、净利润、EBITDA/调整后 EBITDA、经营现金流、资本开支。硬性排版要求：

- **总收入行下方必须紧跟一行 `% YoY`**，逐年算出同比增速——绝对额只说明规模，增速才说明趋势；读者不应被迫心算。
- **净利润/亏损行下方必须紧跟一行 `% margin`**（净利润 ÷ 总收入）。同理，若表中含毛利、经营利润、EBITDA，各自下方也加 `% margin` 行。亏损公司照写负利润率，不许因为"不好看"省略。
- 百分比行用缩进或斜体与绝对额行区分（如 `  % YoY` / `  *% margin*`），保持表格可扫读。
- 期间不完整时（如 1H）在列头标注，且 `% YoY` 与同期比而非与全年比。
- 若某年因并购、会计准则变更、53 周或分部重述导致不可比，在该年 `% YoY` 单元格加脚注标记，并在表下一句说明桥接。

Use this six-column table structure:
Business segment    Revenue mix    Historical growth    Unit economics / margin profile    Next 2–3Y growth estimate    Growth logic
Keep growth logic to two to four short bullets per row. Put detailed reasoning below the table.
When a visual would materially improve comprehension, add one compact exhibit after the table:
    • Use a 100% stacked bar to show revenue mix.
    • Use a growth-versus-margin scatter plot with bubble size representing segment revenue to compare segment economics.
    • Use a simple flow or flywheel only when segment relationships are real and important.
Do not fabricate a chart from incomplete or incomparable segment data.
Quality Check
Before finishing, verify that:
    • Segment revenue reconciles to consolidated external revenue or the gap is explained.
    • Fiscal years, currencies, and units are consistent.
    • A stated 3-year CAGR uses four fiscal-year endpoints.
    • Organic, reported, constant-currency, and acquisition-driven growth are not mixed.
    • Revenue, bookings, ARR, billings, and GMV are not treated as interchangeable.
    • Margin definitions and allocation differences are explicit.
    • Historical facts, management claims, forecasts, and inferences are visibly separated.
    • Every growth thesis ends in a measurable revenue, margin, or cash-flow variable.
    • The writing is understandable without prior finance or industry knowledge.
    • Missing disclosure remains N/D rather than becoming an unsupported estimate

2. Growth potential

按 `references/8q-framework.md` Q1 的写法：开头一句结论；显式增长分解公式（量 × 价 × 份额 × 渗透率）；TAM 算术给出转换链而非直接等同公司增长；落到未来 3–5 年 CAGR 区间并标注（指引/共识/我的估算）与置信度；关键增速假设旁标注 `references/base-rates.md` 分位。

3. Competitive dynamics
Focus on Secondary market competitive dynamics. Key players, market share, each one's strategy, how do they differentiate from each other. 

4. Management, governance, and capital allocation
Insider alignment: Insider holdings and insider transactions, compensation structure of the management. 
How does the company allocate capital? 
Identify the business nature - capital heavy (how does the company fund itself) or capital light, historical payout (dividend + buyback)

5. Valuation

按 `references/valuation-methods.md` 执行：

- **三情景 horizon 固定 5 年**（长期持有口径），每个情景给出第 5 年退出倍数与归因。
- **方法权重必须显式列出并加权**：默认 情景加权 45% / 相对估值 35% / 永续 DCF 20%（上限 30%）/ 反向 DCF 0（诊断用）。偏离默认权重须写明理由。
- 全部计算用 `scripts/dcf.py`（`method_weights`、`scenarios.*.exit`、`relative.scenarios` 三块必填），脚本 `[2]` 的"方法 × 情景"矩阵直接搬进报告正文。
- **必附折现率敏感性**（脚本 `[4a]`）：WACC ±1.5% 下加权公允价值的波动与标签是否翻转；翻转则结论降级为"对折现率敏感"。
- 方法汇总画 football field（画法见 `references/output-format.md` 第 0 节），条目 = 三种方法各自的三情景区间 + 现价竖线。
- 给出结论标定（低估/合理/高估/显著高估）与赔率结构（期望收益、不对称比、P(loss)、Kelly-lite）。

6. Sell-side views

评级分布/目标价区间与中位数/近期调整；**共识 vs 我的分歧点**。

7. 监控清单**：3–5 个持续跟踪指标（KPI/估值锚/证伪信号），各给关注阈值；至少包含一条上行证伪和一条下行证伪，方向不得混用。

---

## 附录（必附）

1. **数据来源与时间戳清单**：| 数据项 | 来源 | 时间 |
2. **估值关键假设摘要**

英文报告附录使用等价标题：**Sources and timestamps**、**Key valuation assumptions and checker summary**
