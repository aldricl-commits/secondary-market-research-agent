# 财务口径定义手册

目的：统一全报告的计算口径。任何分部占比、增长率、利润率、每股与回报率指标，先按本文件定义计算，再进正文；口径不一致的比较是最常见的隐性错误源。

## 1. 收入口径

| 指标 | 定义 | 典型场景 | 常见陷阱 |
|---|---|---|---|
| Revenue | 按会计准则确认的收入（GAAP/IFRS） | 一切默认口径 | 唯一可与利润表对账的口径 |
| Bookings | 期内签约合同总额（TCV 或 ACV） | 软件/服务销售动能 | 含未来多年金额，远大于当期 revenue |
| Billings | 期内开票额 ≈ revenue + Δ deferred revenue | SaaS 需求前瞻 | 受开票周期（年付/月付）扭曲 |
| ARR | 期末经常性收入 × 12（点时值） | 订阅业务规模 | 是快照不是流量，不可与全年 revenue 直比 |
| GMV | 平台交易总额 | 电商/市场平台 | 不是公司收入；take rate = revenue/GMV 才是 |
| NRR | 存量客户收入留存率（同店口径） | 订阅质量 | 各公司 cohort 定义不同，横比先核定义 |

**硬性规则**：以上口径**不得互换**——计算增速、利润率、估值倍数时，分子分母必须同口径同期间；引用公司自报 ARR/bookings 时标注公司定义。为什么：混用口径是 SaaS 报告中最常见的估值虚高来源。

## 2. 分部收入份额

- 公式：`分部份额 = 分部 external revenue ÷ consolidated external revenue`。
- **external revenue 优先**：分部附注同时给 total segment revenue 与 intersegment revenue 时，必须剔除 intersegment 后再算份额。为什么：含内部抵消的份额加总会超过 100%，横向失真。
- 分母一律用合并报表对外收入，不用各分部收入简单加总。为什么：加总里可能残留未抵消项与"其他/公司层"科目。
- 各分部份额 + 其他/抵消项必须加总 ≈ 100%（±0.5%），否则回查是否漏了 corporate/eliminations 行。
- 公司重划分部（resegmentation）时，用重述后可比数据；无重述则只比重叠期间并标注不连续。

## 3. 增长率

- **3-year CAGR 必须用 4 个财年端点**（FY0 与 FY3）：`CAGR = (end/begin)^(1/3) − 1`。为什么：3 年增长跨 3 个复利期，用 3 个端点会算成 2 年。
- 通用公式：n 年 CAGR 需要 n+1 个数据点，指数为 1/n。

| 口径 | 定义 | 使用纪律 |
|---|---|---|
| Reported | 报表原值增速 | 默认口径，其他口径与它并列呈现 |
| Organic | 剔除并购/剥离贡献 | 公司自算无统一标准，须注明公司定义 |
| Constant-currency | 按固定汇率重算 | 判断真实需求用；估值现金流仍用报告币种 |
| Pro-forma | 假设并购期初完成的重算 | 只作可比参考，不得直接进 CAGR 序列 |

- **53-week year 调整**：零售/餐饮 4-4-5 日历约每 5–6 年出现 53 周财年，同比虚增约 +1.9%（1/52）；比较时按 52 周口径调整或明确标注。为什么：多出的一周会把平庸增长伪装成加速。
- 基数含一次性项目（会计变更、大额退款、政府补助）时，先剔除再算增速并注明。

## 4. 利润率层级

| 层级 | 公式 | 注意 |
|---|---|---|
| Gross margin | 毛利 ÷ revenue | COGS 是否含 D&A、物流因公司而异 |
| Operating margin | 经营利润 ÷ revenue | GAAP 与公司调整口径分开报 |
| EBITDA margin | EBITDA ÷ revenue | Adjusted EBITDA 的加回项逐项列出 |
| EBIT margin | EBIT ÷ revenue | 与 operating 差异在非经营损益归类 |
| Net margin | 净利润 ÷ revenue | 归母口径；少数股东损益要剔除 |
| FCF margin | FCF ÷ revenue | FCF 定义见第 7 节 |

- **Segment margin 口径**：先读分部附注确定公司口径是 segment operating、segment gross 还是自定义 "segment profit/adjusted EBITDA"，并确认 SBC、D&A、总部费用是否已分摊。为什么：未分摊总部成本的分部利润率天然虚高。
- **不可直接横比的情形**：不同准则（GAAP vs IFRS 的租赁/研发资本化）、不同 SBC 处理、经销 vs 代理（gross vs net）收入确认、分部分摊政策不同——横比前先做口径桥接或改比同一公司的趋势。

## 5. 每股口径

| 股数口径 | 定义 | 用途 |
|---|---|---|
| Basic weighted average | 期内加权平均普通股 | Basic EPS |
| Diluted weighted average | 加权平均 + 稀释性工具 | Diluted EPS（默认引用口径） |
| 期末股数 | 报表日在外流通股 | 市值、每股账面价值 |
| 完全摊薄期末 | 期末 + 期权/RSU/可转债潜在稀释 | 估值每股价值（见 data-sources.md 2.2） |

- **Treasury stock method 简述**：假设 in-the-money 期权行权，行权款回购股票，净增股数 = 行权股数 −（行权款 ÷ 期内均价）；只有价内工具产生稀释。
- **SBC 稀释纪律**：加回 SBC 算 adjusted EPS 的同时必须用摊薄股数并考虑未来发行，否则同一成本被两头忽略。为什么：SBC 不走利润表就走股本，不可能两边都不算。
- 亏损公司稀释工具反稀释，diluted = basic，估值时仍应用完全摊薄股数。

## 6. 回报率

| 指标 | 分子 | 分母 | 备注 |
|---|---|---|---|
| ROE | 归母净利润 | 平均归母股东权益 | 受杠杆放大，配 DuPont 拆解 |
| ROTCE | 归母净利润（剔除无形摊销影响可选，注明） | 平均有形普通股权益 = 归母权益 − 商誉 − 无形 − 优先股 | 银行常用 |
| ROIC | NOPAT = EBIT × (1 − 有效税率) | 平均 invested capital = 净债务 + 股东权益（或经营资产法），商誉是否剔除须注明 | 与 WACC 比较 |
| ROIIC | Δ NOPAT | Δ invested capital | **multi-year window（3–5 年）**，见下 |
| CROIC | FCF（或 OCF − 维护性 capex） | 平均 invested capital | 现金口径的 ROIC |

- **ROIIC = Δ NOPAT ÷ Δ invested capital**，用 3–5 年窗口的期间变化量，不用单年。为什么：单年 Δ 受投产滞后与一次性项目噪声支配。
- 硬性规则：估值增长价值时用 ROIIC，不得拿历史存量 ROIC 冒充（呼应 base-rates.md 第 3 节）。
- 分母一律用期初或平均值，分子分母的商誉/租赁处理必须一致并注明。

## 7. 现金流

| 指标 | 公式 | 用途 |
|---|---|---|
| OCF | 经营活动现金流（报表原值） | 基础口径 |
| FCF | **OCF − capex** | 默认 FCF 定义，全报告统一 |
| FCFE | FCF − 税后利息净额调整 + 净借款 | 股权现金流，配权益成本折现 |
| Unlevered FCF (FCFF) | NOPAT + D&A − Δ NWC − capex | DCF 用，配 WACC 折现 |
| Owner earnings | 净利润 + D&A ± 非现金项 − 维护性 capex − 必需 Δ NWC | Buffett 口径，重在维护性 capex 估计 |

- **维护性 vs 成长性 capex**：公司极少直接披露；估计法 = 管理层披露 > D&A 近似（成熟业务）> 收入增量法（capex 中支持增长部分剔除）。标注"我的估算"并给区间。为什么：把成长 capex 全记为维持成本会系统性低估成熟期 FCF。
- OCF 质量检查：营运资本一次性释放、供应链金融、保理会虚增单期 OCF，多年平均后再下结论。

## 8. 增量利润率（Incremental margin）

- 公式：`incremental margin = Δ operating profit ÷ Δ revenue`（同期间、同口径）。
- 使用场景：验证经营杠杆——增量利润率持续高于存量 operating margin，利润率趋势向上，反之则扩张在摊薄利润。
- 陷阱：
  1. 收入几乎不变时分母趋零，数值爆炸无意义——Δ revenue < 收入 2% 时不计算；
  2. 单年受一次性项目支配，优先用 2–3 年滚动窗口；
  3. 收入下滑期算出的"高增量利润率"是减亏幻觉，须改述为 decremental margin。

## 9. 估值分子分母对齐

| 分子 | 匹配的分母 | 禁止错配 |
|---|---|---|
| EV | EBITDA、EBIT、FCFF、revenue | EV/net income、EV/FCFE ✗ |
| 市值（equity value） | net income、FCFE、book value | P/EBITDA、市值/FCFF ✗ |

- 原则：分子含债权人价值（EV）配未扣利息的利润流；分子只含股东价值（市值）配已扣利息的利润流。为什么：错配等于把债务成本算给股东或反之，倍数系统性失真。
- 少数股东权益：EV 里加了 minority interest，则分母用含少数股东的 EBITDA/EBIT，保持一致。
- 硬性规则：同一张倍数比较表内，所有公司的 EV 构成（租赁、养老金、少数股东）与利润口径必须一致（呼应 data-sources.md 8.2）。

## 10. 单位与币种纪律

- 单位统一：million 简写 mm，billion 简写 bn（呼应 output-format.md）；同一张表不得混用 mm 与 bn，换算 1 bn = 1,000 mm；中文材料的"亿"换算为 100 mm 时显式标注。
- **报告币种 vs 申报币种**：公司报表币种（presentation currency）可能不同于经营币种（functional currency）与上市地交易币种；估值现金流用报表币种，最终每股价值换算到股价币种时注明汇率与日期。
- 汇率使用场景：
  | 项目 | 用哪种汇率 | 为什么 |
  |---|---|---|
  | 利润表、现金流量表 | 期间平均汇率 | 流量在全期间发生 |
  | 资产负债表 | 期末汇率 | 存量按时点计价 |
  | 市值/EV 与财务指标对接 | 同一时点汇率 | 分子分母时点错位产生伪折价 |
- 硬性规则：跨币种倍数比较（如港股 vs 美股同业）先全部换算到同一币种同一时点，并在表注写明汇率来源与日期。

## 11. 自检清单（计算前必过）

1. 分部份额分母是否为 consolidated external revenue？
2. CAGR 端点数 = 年数 + 1？有无 53 周/并购/重述污染？
3. 利润率的分子口径（GAAP/调整）与同业是否一致？
4. 每股指标用的是哪种股数？估值是否用完全摊薄？
5. EV 与利润流是否对齐？少数股东处理是否一致？
6. 币种、单位、汇率时点是否统一并注明？
