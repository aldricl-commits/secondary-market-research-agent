# 免责声明 / Disclaimer

## 中文

**本仓库是研究方法论工具，不是投资建议。**

1. 本仓库**不包含**任何针对具体上市公司的成稿研究报告或估值模型。研究产出（`reports/`）与估值 case 文件（`workspace/`）内嵌具体标的的情景假设、概率与公允价值，等同于机器可读的投资结论，一律留在本地、不进版本库（见 `.gitignore`）。
2. 文档（`README.md`、`docs/`）中出现的所有数字均来自 `scripts/dcf.py --example` 的**合成案例**（Example Corp / EXMP）或明确标注的虚构示意，**不涉及任何真实公司**。任何人都可以自己运行 `python3 scripts/dcf.py --example` 复现这些数字。
3. 本仓库不提供个性化投资建议，作者不是持牌投资顾问。任何人依据本仓库内容做出的投资决策，风险自负。
4. 本框架产出的估值结论是**基于明示假设的条件性结论**，且只在其标注的数据截止日成立。假设列在每份报告的附录里——先读假设，再读结论。框架本身不保证输出正确，它保证的是输出可被审计和证伪。
5. 本仓库不含任何第三方研究机构的研报正文。

## English

**This repository is a research-methodology toolkit, not investment advice.**

It contains **no** finished research reports or valuation models for any specific listed company. Research output (`reports/`) and valuation case files (`workspace/`) embed scenario assumptions, probabilities and fair values for specific tickers — effectively machine-readable investment conclusions — and are kept local, outside version control (see `.gitignore`).

Every figure appearing in the documentation comes from the **synthetic** `scripts/dcf.py --example` case (Example Corp / EXMP) or from explicitly labelled illustrative placeholders. No real company is involved. Reproduce them yourself with `python3 scripts/dcf.py --example`.

No personalized investment advice is provided. The author is not a licensed investment adviser. Valuation outputs produced by this framework are **conditional on stated assumptions** and hold only as of the stated data cut-off date. The framework does not guarantee that its output is correct; what it guarantees is that the output can be audited and falsified. This repository contains no third-party research firm's proprietary reports.
