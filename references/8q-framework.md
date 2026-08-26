# 8Q Write-up 框架（Apeiron 风格）

来源：从 `Apeiron Write-up/` 全部范例（CATL、Adyen、ASML、AMD、Kaspi、PDD、HDFC、Atour、Brunello Cucinelli、Horizon Robotics、Melrose、UMG、QFIN、Euronext、TEVA、Disney 等）提炼。本文件定义 8Q write-up 的固定骨架、各节写法与文风纪律；同时作为深度研究报告的**写作风格来源**——深度报告的证据纪律按 `report-template.md`，但"怎么说话"参考本文件。

## 1. 定位

- 8Q 是 **2,500–5,000 词的投资判断 memo**，不是 30 页 initiation。价值在判断浓缩，不在覆盖完整。
- 与七章深度报告的分工：8Q = 快速形成/更新论点；深度报告 = 证据完备、可审计、可跟踪。两者估值纪律共用 `valuation-methods.md`。

## 2. 固定骨架（顺序不可变）

```text
公司名 (Ticker)
Market Cap: $X    Share Price: $X    Date: YYYY/MM/DD

Company overview
1. Is there sufficient potential of sales growth for the next 5 years?
2. What is your sustainable competitive advantage?
3. What is your culture?
4. Why do your customers like you?
5. Are your margins/return worthwhile?
6. How do you allocate capital?
7. Is it attractively valued?
8. Why doesn't the market understand this?
Conclusion

Author: [name]
[date]
(可选 Appendix：行业 101、单位经济长表、危机时间线等深度材料后置)
```

标题用问题原文（第二人称质问公司）。行业复杂时可在 Company overview 前加一段 ~800 词的行业 primer（如 Melrose 的 "Aircraft engine industry and RRSP 101"）。

## 3. 各节写法

| 节 | 篇幅 | 写法要点 |
|---|---|---|
| Company overview | 300–600 词 | 纯描述+量化 mix（分部收入/利润占比），**零观点**；用一个类比锚定认知（"the China Merchants Bank + Alipay + Taobao of Kazakhstan"）；把商业模式讲到收费方式层面（take rate、单价、抽佣） |
| Q1 增长 | 全文最长之一，常占 30–50% | 开头一句**加粗结论**（"In mid-term, 20% revenue growth is achievable for sure"）；显式增长分解公式（"增长 = GDP + 通胀 + debt/GDP 提升 + 份额"）；TAM 算术 = 量 × 渗透率 × ASP，落到个人 CAGR 区间（"I expect 20-30% revenue CAGR until 2030"）；渗透率对标他国/他业 |
| Q2 护城河 | 800–1,600 词，辩论核心 | 先竞争格局（玩家+份额+各自策略），再护城河来源；用几十年的行业叙事史当证据（ASML vs Nikon、AMD Bulldozer→Zen）；定性结论必须绑定财务证据 |
| Q3 文化 | 300–700 词 | 创始人故事+转折点决策（"Decision 1 – Leave SAE and start ATL"）；管理层持股与激励数字（"CEO holds 22.6% shares"、薪酬与持股对比）；直接引用管理层原话 |
| Q4 客户 | 可以只有 1–3 句 | 无争议就写短（"It's the only supplier. The whole supply chain relies on ASML."）；分商户/消费者两侧写价值主张 |
| Q5 利润率/回报 | 300–500 词 | **自己重算 unit economics**（Rmb/KWh、EUR/transaction、单店模型、NIM+fee−credit cost 结构）；分部分别给利润率；对报表口径保持怀疑并给出自己的调整表 |
| Q6 资本配置 | 150–350 词 | FCF 转化率、派息+回购历史；给历史并购**打分并附对价与倍数**（"ATI at $5.6bn... 50x P/E. In hindsight, it's a dumb deal"） |
| Q7 估值 | 250–400 词 + 表 | 见下节"估值写法" |
| Q8 变异认知 | 200–700 词 | 见下节"变异认知写法" |
| Conclusion | 1–3 句 | 复述 3–5 个买点，结尾给 **2–6 词的动作动词**："Buy." / "Wait for better entry point." / "Buy at below 25x fwd P/E." / "Avoid, neutral."；条件动作优先于目标价 |

## 4. 估值写法（Q7）

- **永远是情景 × 倍数的驱动表，8Q 里不写 DCF 长表**（深度报告里 DCF 用 `scripts/dcf.py` 做，8Q 只引用结果）。
- 结构：4–6 个驱动变量（量 × 价/take rate × 份额 × 利润率 × 倍数）→ 隐含市值 → Upside %。情景为 base/bull 或 bear/base/bull，**horizon 与深度报告一致取 5 年**。
- 倍数必须对照增长与同业 sanity check（"25x 2023E PE looks fair as CATL may maintain 30%+ profit growth"）。
- 另一常用变体：**IRR 框架**（BVPS CAGR + 股息率 + 重估 → "18-20% IRR"），适合金融股与稳态生意。
- **保守性显式声明**：期权性业务排除并标注（"Hepsi is valued at zero before we see any visibility"）；base case 取管理层指引下沿。
- 尽量从第二个角度交叉验证（P/B × ROE、每用户价值等）。

## 5. 变异认知写法（Q8）

两种范式，选其一：

1. **Steelman-and-rebut**：把空头论点列成加粗 bullet，逐条用数据反驳（"Overcapacity – a weak argument to be honest"），并指名下一个可验证催化剂（"The next watch will be the feedback from MSFT"）。
2. **Variant perception**：诊断市场的心理/结构性错误（"the short investment horizon among A-share investors"、锚定效应、指数技术性卖压）。

诚实纪律：可以**承认**（"I share the concern with market"）、可以**认输**（"It's a consensus long."——承认无 edge 也是合法答案）；让 concession 转化为 timing（锁定期抛压 = 建仓窗口）。

## 6. 文风纪律（硬性）

1. **第一人称单数负责制**："I believe / my base case / I have done the math"。不用无主语的"市场认为"逃避判断（"we" 仅指基金团队）。
2. **每句带数字**；对标必须锚定参照系（"cars per 1000: India 55 vs China 226"）。区间优先于伪精度（"RMB8-10k"、"20-30%"、"c." 和 "~" 标注约数）。
3. **一份 write-up 一个大类比**：CATL=Samsung、PDD=Costco、Brunello Cucinelli=Hermès。类比要逐因素检验，不能只贴标签。再造一个**论点把手**（thesis handle）：如 "King of Cashmere"、"a publicly traded private equity business"。
4. **篇幅不对称是设计**：辩论所在的 1–2 节给 500–1,600 词，无争议的问题 1–3 句带过。深度跟着分歧走。
5. **每节先结论后论据**；关键论点句加粗；bullet 用加粗引导语 + 破折号展开。
6. **自问自答**推进论证："Do I worry new competitors? No."
7. **对报表保持怀疑**：自己重算分部利润、调整口径，并说明为什么公司口径失真。
8. 不确定性词汇校准：高确信 = "for sure / very doable"；真未知 = "remains debatable / we need more evidence"；期权性 = "the X factor / worth an option, not in base case"。主动交代论点弱处与自己的 miss。
9. 图表就近，标 "Figure: ..."；表格自制（运营矩阵、成本 build-up、comps、情景表），不贴截图凑数。
10. 中文 8Q 用等价结构：问题标题可译可保留英文，数字规范按 `output-format.md`，判断标注"我的判断/我的估算"。

## 7. 8Q ↔ 七章深度报告映射

| 8Q | 深度报告章节（report-template.md） |
|---|---|
| Company overview | 1. Business description |
| Q1 增长 | 2. Growth potential |
| Q2 护城河 / Q4 客户 | 3. Competitive dynamics |
| Q3 文化 / Q6 资本配置 | 4. Management, governance, and capital allocation |
| Q5 利润率 | 1/2 章的分部经济与驱动分析 |
| Q7 估值 | 5. Valuation（深度版按 valuation-methods.md 至少两法 + dcf.py） |
| Q8 变异认知 | 6. Sell-side views 的"共识 vs 我的分歧点" |
| Conclusion | 7. 监控清单 + 结论框 |
