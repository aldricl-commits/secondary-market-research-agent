# 行业路由表

用途：研究开始前，把目标公司映射到 `industries/*.md` 行业附录。行业附录提供该行业的 KPI 字典、价值驱动树、财务模型结构、估值方法与财报模式重点，**优先级高于通用模板中与之冲突的部分**。

## 0. 路由规则（硬性）

1. **先判定主业**：按最新财年收入/利润构成判定主业，不按公司自我标签（"AI 公司"、"平台"是营销词，不是路由依据）。
2. **多业务公司拆分部路由**：每个重要分部（收入或利润占比 ≥20%）分别匹配行业附录，各自用对应框架分析与估值，最后 SOTP。禁止用单一行业框架打包混合体。
3. 匹配到 1 个主附录 + 最多 2 个分部附录即可，不要贪多。
4. 报告附录必须记录本次使用了哪些行业附录（来源清单的一部分）。
5. 未覆盖行业见第 3 节：用最近替代框架 + 显式声明"该行业无专用附录，借用 X 框架，以下差异需注意"。

## 1. 主路由表

| 行业附录 | 适用范围 | 触发关键词（中/英） | 主估值锚 |
|---|---|---|---|
| `industries/saas.md` | 订阅制/云原生/垂直 SaaS、消费订阅软件 | SaaS、订阅软件、企业软件、云软件、开发者工具、网络安全软件、subscription/cloud/vertical SaaS | EV/ARR、EV/FCF + Rule of 40 校正；高估值必做反向 DCF |
| `industries/internet-platform.md` | 搜索、电商、社交、广告、本地生活、流媒体平台、共享经济 | 互联网平台、电商、社交、广告平台、外卖、网约车、e-commerce、marketplace、streaming platform | SOTP 为主；SBC 后 FCF 倍数；新业务用单位经济/期权定价 |
| `industries/semiconductors.md` | 芯片设计、代工、IDM、存储、设备、材料、EDA/IP、封测 | 半导体、芯片、GPU、AI 芯片、fabless、foundry、DRAM/NAND/HBM、光刻、封装测试 | 三情景 P/E + 跨周期正常化盈利；禁止峰值利润 × 中枢倍数 |
| `industries/hardware.md` | 消费电子、计算设备、网络设备、服务器、存储系统 | 硬件、消费电子、手机、PC、服务器、AI server、ODM、networking | 跨周期 EV/EBITDA、P/E；硬件/服务/融资 SOTP |
| `industries/banks.md` | 商业/零售/区域/数字银行、银行控股公司 | 银行、存贷、deposit franchise、neobank、universal bank | P/TBV × 可持续 ROTCE；禁用工业企业 FCF/EV-EBITDA |
| `industries/payments-fintech.md` | 卡组织、收单、钱包、跨境汇款、BNPL、经纪/交易平台、银行科技（不含持牌银行主体） | 支付、卡组织、收单、数字钱包、超级App、BNPL、消费信贷平台、crypto 交易平台 | EV/EBITDA、P/E；信贷型用拨备后 ROE × P/B 并引用 banks.md 资产质量框架 |
| `industries/capital-markets.md` | 资管、交易所与清算、券商/投行、评级机构、市场数据 | 资产管理、AUM、交易所、清算所、券商、投行、评级、market data | 资管 DCF/P/E；交易所 EV/EBITDA 区分经常/周期收入；券商 P/TBV-ROTCE |
| `industries/insurance.md` | 财产险、寿险、健康险、再保险、保险经纪、综合保险集团 | 保险、产险、寿险、年金、健康险、再保险、combined ratio、经纪 | P&C 用 P/B × 正常化 ROE；寿险 P/EV + VNB；集团 SOTP |
| `industries/consumer.md` | 品牌消费品、零售、餐饮、服饰、美妆、食品饮料、家居、耐用品、消费服务（含奢侈品、酒店门店模型） | 消费、品牌、零售、餐饮、服饰、美妆、白酒、食品饮料、奢侈品、luxury | 正常化 P/E / EV-EBITDA；门店公司必做单店经济 × 开店 NPV |
| `industries/media-gaming.md` | 游戏、影视、音乐、出版、流媒体内容、体育赛事、IP 授权 | 游戏、手游、影视、音乐、唱片、出版、IP、streaming content | 成熟订阅/游戏 DCF、EV/EBITDA；内容集团按 IP/平台 SOTP |
| `industries/healthcare-services.md` | 医院诊所、医疗服务、医疗器械、IVD、CRO/CDMO | 医院、医疗服务、器械、诊断、IVD、CRO、CDMO、医药外包 | 服务/器械 DCF + EV/EBITDA；装机 cohort；医院分支付方 SOTP |
| `industries/pharma.md` | 创新药、生物技术、成熟制药、仿制药、疫苗 | 制药、医药、biotech、创新药、仿制药、管线、临床阶段 | 逐资产 rNPV（必做）+ 在售产品 DCF（含 LOE 侵蚀）+ SOTP |
| `industries/autos-ev.md` | 整车 OEM、EV 新势力、零部件、经销商 | 汽车、整车、EV、新能源车、造车新势力、零部件、Tier 1、智能驾驶、经销商 | 传统 OEM 中周期 EPS × 中枢 P/E；EV 成长期反向 DCF；金融子公司拆开 |
| `industries/industrials.md` | 通用机械、自动化、电气设备、航空航天与国防、多元工业集团、工程建筑 | 工业、机械、自动化、机器人、电气设备、军工、国防、多元集团、E&C | 中周期盈利 × 中枢 EV/EBITDA；多元集团一律 SOTP；国防看 backlog |
| `industries/energy.md` | 油气上游、综合能源、炼化、油服、中游管道/LNG、煤炭 | 油气、E&P、炼化、油服、管道、LNG、煤炭 | 逐资产 NAV 为主；中周期 EV/DACF；禁止现货价永续化 |
| `industries/metals-mining.md` | 基本/贵金属、电池金属、铁矿、煤矿、冶炼加工 | 矿业、铜、铝、金矿、锂矿、铁矿、冶炼 | 逐矿山 NAV / P/NAV；AISC 成本曲线分位；价格 ±20% 敏感性必做 |
| `industries/utilities.md` | 受监管电力/燃气/水务、公用事业控股、IPP、可再生发电运营 | 公用事业、电力、燃气、水务、IPP、风电场、光伏电站运营、rate base | DDM/DCF（rate base × earned ROE 驱动）；P/B × ROE 交叉；集团 SOTP |
| `industries/telecom.md` | 移动/固网运营商、铁塔、卫星通信 | 电信、运营商、宽带、5G、FTTH、铁塔、卫星通信 | EV/EBITDA(aL) + FCF yield；DCF 覆盖完整 capex 周期；铁塔单独估值 |
| `industries/transport.md` | 航空、机场、铁路、航运、快递物流、货代 | 航空公司、机场、铁路、集运、干散货、油轮、快递、物流、货代 | 航空/航运中周期盈利 × 低倍数 + 船队/机队 NAV 下限；机场铁路 EV/EBITDA + 监管回报 |
| `industries/reits.md` | 权益型 REIT（各物业类型）、mREIT、开发商 | REIT、房地产、物流地产、数据中心 REIT、开发商、中资地产 | NAV（NOI ÷ cap rate）+ P/AFFO；mREIT 用 P/B + 息差久期，绝不混用 |

## 2. 跨附录路由（常见组合）

| 公司形态 | 路由 |
|---|---|
| 超级 App / 金融科技平台（如 Kaspi） | payments-fintech.md 主 + banks.md（信贷资产质量）+ internet-platform.md（电商分部） |
| 云 + 广告 + 电商巨头 | internet-platform.md 主 + saas.md（云分部单独建模） |
| 芯片 + 系统 + 软件（如苹果、特斯拉供应链） | 按分部拆 semiconductors / hardware / saas |
| 全能银行（含投行/资管） | banks.md 主 + capital-markets.md 分部 |
| 药企 + 器械/消费健康 | pharma.md 主 + healthcare-services.md 分部 |
| 综合能源（上游+炼化+新能源发电） | energy.md 主 + utilities.md（发电运营分部） |
| 内容 + 平台 + 主机（如 Disney、索尼） | media-gaming.md 主 + internet-platform.md / hardware.md 分部 |
| 汽车 OEM 含金融子公司 | autos-ev.md，金融子公司按其规则单独估值 |

## 3. 未覆盖行业与最近替代

以下行业无专用附录。借用替代框架时必须在报告中声明，并注意所列差异：

| 未覆盖行业 | 最近替代 | 借用时注意 |
|---|---|---|
| IT 服务/软件外包/系统集成 | saas.md（部分）+ industrials.md 的项目制逻辑 | 收入是人天/项目制不是订阅；看人员利用率、单价、attrition，不看 NRR/ARR |
| 教育与培训 | consumer.md 门店/订阅模型 | 政策风险主导（尤其中国）；预收款监管；获客成本结构不同 |
| 化工（大宗/特种/工业气体） | metals-mining.md 周期框架 + industrials.md | 看价差（spread）而非商品单价；产能周期与开工率；特种化工可享成长框架 |
| 建材（水泥/玻璃） | metals-mining.md 成本曲线 + industrials.md | 区域性市场，运输半径决定竞争格局 |
| 农业/种业/农化 | metals-mining.md 周期 + consumer.md 品牌部分 | 政策补贴、天气、生物资产会计 |
| 酒店集团/OTA/博彩/邮轮 | consumer.md 单店经济（酒店）、internet-platform.md（OTA）、reits.md（持有物业） | RevPAR 周期；博彩看牌照与 mass/VIP 结构 |
| Crypto 原生（矿企/财库公司） | payments-fintech.md（交易平台部分） | 币价敏感性用矿业式 NAV 思路；财库公司=杠杆化币价敞口 |
| 大宗商品贸易商 | capital-markets.md 交易类收入逻辑 | 看 ROE 稳定性与风控，不看单年利润倍数 |
| 光伏组件/风机制造 | industrials.md + semiconductors.md 产能周期 | 技术迭代快、产能过剩常态；跟踪单 W 盈利 |
| 环保/废物处理 | utilities.md（合同型）+ industrials.md | 特许经营期限与续约；政府支付能力 |
| 人力资源/专业服务（检测认证、咨询） | capital-markets.md 轻资产服务逻辑 | 看人效与网点密度；周期敏感度分层 |
| 物业管理/地产经纪 | consumer.md 服务模型 + reits.md 背景 | 关联开发商依赖度是核心风险 |

## 4. 路由后必做

读取选定附录后，按其"使用原则"确认公司确实适用（每个附录开头都有排除条款）。若发现不适用（例如"SaaS 公司"实为一次性 license），回到本表重新路由，并在报告中说明。
