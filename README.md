# Secondary Market Research Agent

一个买方视角的**二级市场个股研究 agent**。你给它一个公司名或代码，它按固定管线跑完研究并产出一份可审计的投资研究报告。

它不是"让 AI 写一篇看起来专业的研报"。它解决的是 AI 写研报的三个真实失效模式：

| 失效模式 | 这个 agent 怎么处理 |
|---|---|
| **编数字**——模型凭记忆补上看似合理的财务数据 | 来源分五层（Tier 1 监管申报 → Tier 5 媒体），关键财务数字**必须**有 Tier 1 原文支持；拿不到就写"未获取到"，不许留空表头、不许用倒推值冒充事实 |
| **事实与观点混在一起**——读者分不清哪句是披露、哪句是模型的猜测 | 五类信息强制分离：历史事实 / 管理层观点 / 共识预期 / 我的估算 / 推断。分析性判断一律署名"我的判断" |
| **估值是数字游戏**——DCF 折现率动 1% 结论就反转，但报告不说 | 三种方法显式加权（情景 45% / 相对 35% / 永续 DCF 20%），必附折现率敏感性；标签随折现率翻转就降级为"对折现率敏感" |

配合 [Claude Code](https://claude.com/claude-code) 使用：把这个仓库作为工作目录打开，`CLAUDE.md` 会自动加载成 agent 的调度指令。

> **先看这个** → **[docs/OUTPUT-GUIDE.md](docs/OUTPUT-GUIDE.md)**：输出长什么样、每一章有什么、怎么读。这是分享给同事时应该先读的文件。
>
> 空白结构 + 字段标注 → **[docs/report-skeleton.md](docs/report-skeleton.md)**
>
> 注：**成稿报告与估值 case 不进版本库**——它们内嵌具体标的的投资结论，一律留在本地（见 [`.gitignore`](.gitignore)）。文档里的示例数字全部来自 `scripts/dcf.py --example` 的合成案例，可自行复现。

---

## 四种输出模式

agent 按你的提问方式自动判定模式，不需要你指定。

| 模式 | 你会怎么问 | 产出 | 量级 |
|---|---|---|---|
| **深度研究报告**（默认） | "研究一下台积电"、"写一篇 ASML 的报告" | 七章 + 附录，完整证据链 | 8,000–15,000 字 |
| **财报深度分析** | "分析英伟达这季财报"、"TSM 3Q25"、"腾讯业绩怎么样" | 九章，以财报为重检论点的事件 | 5,000–10,000 字 |
| **8Q write-up** | "给我一份 ASML 的 8Q"、"写个短版 memo" | 8 个固定问题的判断浓缩 | 2,500–5,000 词 |
| **AI role play** | "hedge fund 视角看 NVDA"、"跑一遍投委会" | 四个独立人设 memo + 委员会合成（**英文输出**） | 单视角 1–2 页 / 全委员会 6–10 页 |

语言默认跟随你的提问语言（role play 例外，一律英文）。

## 执行管线（九步，不跳步）

```
1. 解析请求      公司 / 代码 / 上市地 / 财年年结 / 模式 / 语言；歧义代码先确认主挂牌
2. 行业路由      references/industry-routing.md → 选 1 个主行业附录 + 最多 2 个分部附录
3. 读取规范      data-sources.md（采集纪律）+ financial-definitions.md（计算口径）+ 行业附录
                 A股/港股标的加读 markets-cn-hk.md
4. 数据采集      四条线并行：披露线 / 预期线 / 沟通线 / 市场线
                 每个数字记来源 + 时间戳；关键财务数字 ≥1 份 Tier 1 原文
5. 财报质量核查  forensic-accounting.md 最小核查集 → 产出可信度等级 A/B/C/D
                 C 级 → 禁用"低估"买入标签；D 级 → 只允许回避/卖出
6. 分析          按模板章节 + 行业附录的价值驱动树与 KPI 字典展开
7. 估值          scripts/dcf.py：三情景 × 三方法加权，5 年 horizon
                 关键假设旁标注 base-rates.md 历史分位；>80 分位必须给结构性理由
8. 写作          output-format.md：结论前置、结论框 / Tearsheet、段落 ≤5 行、精度匹配不确定性
9. 质量门        过模板末尾的检查清单；附数据来源时间戳清单 + 估值假设摘要
```

## 仓库结构

```
CLAUDE.md                       agent 主调度文件（模式判定、管线、硬纪律、文件地图）
│
references/                     11 个规范文件——agent 的"工作手册"
├── report-template.md          深度报告七章结构与各章要求
├── earnings-mode.md            财报模式九章结构与对账协议
├── 8q-framework.md             8Q 骨架 + 全局文风纪律
├── output-format.md            排版、数字规范、置信度自评、预测登记
├── data-sources.md             来源分层、降级路径、对账、防注入
├── financial-definitions.md    收入/增长/利润率/回报率/每股口径定义
├── valuation-methods.md        估值方法、5 年三情景、方法权重、仓位思维
├── base-rates.md               增速/利润率/ROIC 历史分布锚（外部视角）
├── forensic-accounting.md      财报质量核查与可信度评级
├── industry-routing.md         行业 → industries/*.md 路由表
└── markets-cn-hk.md            A股/港股披露、准则、对照系差异
│
industries/                     20 个行业附录：KPI 字典、价值驱动树、估值方法、财报重点
                                （行业附录的 KPI/估值口径优先于通用模板中冲突的部分）
│
scripts/dcf.py                  估值计算 CLI（纯标准库，JSON 输入）
│
AI role play/                   四视角投委会：4 个人设 + 调度规则 + 支撑文件
.claude/skills/analyze-earnings/ 财报分析 skill（调度 earnings-mode + 行业路由 + 前瞻分支）
│
docs/
├── OUTPUT-GUIDE.md             ★ 输出说明——先读这个
└── report-skeleton.md          七章空白模板 + 每个字段的填写要求
│
workspace/                      本地工作目录（估值 case 与中间数据，不进版本库）
reports/                        成稿输出目录（不进版本库）
```

## 快速开始

**跑一份报告**

在 Claude Code 里把这个仓库作为工作目录，然后直接说：

```
研究一下 ASML
```

成稿会写到 `reports/<YYYYMMDD> <公司名> <模式>.md`，估值 JSON 写到 `workspace/<ticker>/`。这两个目录都在 `.gitignore` 里——研究产出留在本地，不随仓库分发。

**单独跑估值计算**

`scripts/dcf.py` 是独立的，不依赖 agent，纯 Python 标准库：

```bash
python3 scripts/dcf.py --example > case.json   # 生成带注释的输入模板
python3 scripts/dcf.py case.json               # 打印报告 + 写出 case_output.json
```

它输出：三情景 × 三方法的加权公允价值、反向 DCF（现价隐含什么）、折现率敏感性、期望收益 / 不对称比 / P(loss) / Kelly-lite 仓位参考、以及概率稳健性检验（把概率推到对结论最不利的组合，看标签是否翻转）。

## 估值方法权重（为什么 DCF 只占 20%）

| 方法 | 权重 | 理由 |
|---|---:|---|
| 情景加权（5 年退出倍数） | **45%** | 假设全部落在可观察的经营变量上；只折现 5 年、不含永续项，对折现率最不敏感 |
| 相对估值（合理倍数） | **35%** | 直接对标市场为同类资产实际支付的价格；与情景法共用经营假设，分歧必然来自倍数判断 |
| 永续 DCF（Gordon） | **20%**（上限 30%） | WACC ±1% 就能让估值变动 30–50%，终值常占价值 70%+。**降权不是因为它错，是因为它的错误无法被验证** |
| 反向 DCF | **0**（诊断） | 回答"现价隐含什么"，不产出公允价值，永远单列 |

情景 horizon 固定 **5 年**——覆盖一个完整的产品/资本/监管周期。3 年窗口会把周期底部误判为结构性衰退。

## 已知缺口

- **`industries/` 目录待补齐**：20 个行业附录在原始工作目录里，因 Google Drive 文件系统权限问题未能打包进首次提交。缺了它们，管线第 2 步（行业路由）会退化为通用模板——报告仍能产出，但会丢掉行业特定的 KPI 与估值锚。补齐方法见 [`industries/README.md`](industries/README.md)。
- 一致预期依赖公开聚合站（FactSet / LSEG / Bloomberg 无权限）；聚合站的预测数字**经常有量级错误**（见过把 $181mm 收入预测写成 $9bn 的），`references/data-sources.md` 要求交叉核对两处以上。

## 免责

见 [DISCLAIMER.md](DISCLAIMER.md)。本仓库是研究方法论工具，不提供投资建议；作者不是持牌投资顾问。文档中的示例数字均为合成案例，不涉及任何真实公司。
