#!/usr/bin/env python3
"""dcf.py — 单文件、纯标准库的公司估值 CLI（DCF / 反向 DCF / 三情景加权 / EPV / 敏感性 / 仓位参考）。

用法
====
    python3 dcf.py case.json      # 读取一个公司 case 的 JSON，打印报告并写出 <case>_output.json
    python3 dcf.py --example      # 打印一份带注释("_comment"字段)的完整示例 JSON 后退出

对应参考文件：valuation-methods.md §2(三情景加权)、§4(EV/不对称比/Kelly-lite/P(loss))；
base-rates.md §4(隐含退出 P/FCF 自动输出)；earnings-mode.md §5(敏感性与三情景概率加权)。

输入 JSON 结构（每个公司 case 一个文件；所有以 "_" 开头的键会被忽略，可用作注释）
================================================================================
共享块（顶层字段）:
  company              str   公司名
  ticker               str   代码
  currency             str   报告币种（仅用于展示）
  valuation_date       str   估值基准日 YYYY-MM-DD（仅用于展示）
  current_price        float 当前股价
  diluted_shares_mm    float 稀释后股本（百万股）
  net_debt_mm          float 净债务（百万，负数 = 净现金）
  wacc                 float 折现率（小数，如 0.09 = 9%）
  terminal_growth      float 永续增长率（小数；各情景可覆盖）
  annual_dilution_pct  float 可选。年度稀释率（小数）；每股价值按
                             股本 × (1+稀释率)^年数 计算
  scenario_horizon_years int 可选，默认 5，必须 >= 5。情景法与相对估值法的评估年限
                             （valuation-methods.md §2：5 年 horizon，对齐长期持有）
  method_weights       obj   可选。三种方法的权重，和必须为 1，默认
                             {"scenario":0.45,"relative":0.35,"dcf":0.20}。
                             dcf > 0.30 会告警——永续 DCF 对折现率过度敏感，只作交叉验证。
                             某方法缺输入时，其权重自动按比例分配给其余方法。

"scenarios" 块（必填；必须且只能含 bear / base / bull 三个键）:
  每个情景:
    probability      float  概率（三情景之和必须为 1）
    revenue_mm       float  基年收入（百万）
    revenue_growth   [float] 显性期逐年收入增速（建议 5 年以上）
    fcf_margin       [float] 逐年 FCF 利润率（与 revenue_growth 等长，允许爬坡）
    terminal_growth  float  可选。覆盖顶层永续增长率
    exit_multiple    float  可选。退出 P/FCF 倍数（只影响 [1] 永续 DCF 的并列展示）
    exit             obj    **情景加权法（默认最高权重）的输入**：
                              metric     "revenue"(默认) / "fcf" / "custom"
                              multiple   H 年 EV 倍数（EV/Sales、EV/EBITDA、P/FCF…）
                              metric_mm  可选；metric=custom 时必填。省略时取
                                         H 年收入或 H 年 FCF
                              rationale  可选。合理倍数的归因，会写入输出 JSON
                            计算：EV_H = multiple × metric；净债务_H = 期初净债务 −
                            H 年累计 FCF；每股_H = (EV_H − 净债务_H) ÷ H 年股本；
                            现值 = 每股_H ÷ (1+WACC)^H。**无永续增长项**。

"relative" 块（相对估值；两种口径二选一）:
  A. 三情景口径（可计入权重，推荐）:
     metric_name    str  如 "EV/Sales"
     metric_label   str  可选，如 "FY2031E"
     horizon_years  int  可选，默认 scenario_horizon_years
     scenarios      obj  bear/base/bull 各含 {metric_mm, multiple, rationale?}
                         合理倍数须自行推导，不许直接抄同业中位数
  B. 旧版每股口径（只展示、不计权重）:
     metric_name / metric_per_share / multiple_low / multiple_mid / multiple_high

"epv" 块（可选；无增长盈利能力价值，作为下限锚）:
  normalized_ebit_mm      float 正常化 EBIT（百万）
  tax_rate                float 税率（小数）
  maintenance_capex_adj_mm float 维持性资本开支调整（百万）：从税后 EBIT 中
                                扣减；若折旧高估维持性开支可给负数（即加回）

"relative" 块（可选；相对估值快算）:
  metric_name       str   指标名（如 "EPS" / "FCF per share"）
  metric_per_share  float 每股指标值
  multiple_low      float 低倍数
  multiple_mid      float 中倍数
  multiple_high     float 高倍数

内联示例（`--example` 输出同一份，可直接运行）:
    {
      "company": "Example Corp", "ticker": "EXMP", "currency": "USD",
      "valuation_date": "2026-08-25", "current_price": 150.0,
      "diluted_shares_mm": 1000.0, "net_debt_mm": -5000.0,
      "wacc": 0.09, "terminal_growth": 0.03, "annual_dilution_pct": 0.01,
      "scenario_horizon_years": 5,
      "method_weights": {"scenario": 0.45, "relative": 0.35, "dcf": 0.20},
      "scenarios": {
        "bear": {"probability": 0.25, "revenue_mm": 50000,
                  "revenue_growth": [0.02, 0.02, 0.01, 0.01, 0.0],
                  "fcf_margin":     [0.16, 0.15, 0.15, 0.14, 0.14],
                  "terminal_growth": 0.02},
        "base": {"probability": 0.50, "revenue_mm": 50000,
                  "revenue_growth": [0.08, 0.07, 0.07, 0.06, 0.05],
                  "fcf_margin":     [0.18, 0.18, 0.19, 0.19, 0.20]},
        "bull": {"probability": 0.25, "revenue_mm": 50000,
                  "revenue_growth": [0.14, 0.13, 0.12, 0.10, 0.09],
                  "fcf_margin":     [0.20, 0.21, 0.22, 0.22, 0.23],
                  "exit_multiple": 22}
      },
      "epv": {"normalized_ebit_mm": 9000, "tax_rate": 0.21,
               "maintenance_capex_adj_mm": 500},
      "relative": {"metric_name": "EPS", "metric_per_share": 5.5,
                    "multiple_low": 15, "multiple_mid": 18, "multiple_high": 22}
    }

输出
====
1. 每情景永续 DCF：显性期 PV、终值（Gordon；有 exit_multiple 时两套并列）、股权价值、
   每股价值、自动输出隐含退出 P/FCF（对照 base-rates.md §4：>25x 且稳态增速仅 ~3% 时终值偷偷乐观）
2. **方法加权 × 概率加权公允价值（主口径）**：三方法 × 三情景矩阵 → 每情景方法加权值
   → 概率加权 FV 与标签。下游期望收益/赔率/稳健性检验全部基于这套加权后的每情景值
3. 反向 DCF：诊断用（权重 0），以现价倒解 (a) 固定收入增速；(b) 固定 FCF 利润率
4a. 折现率敏感性：方法加权公允价值 vs WACC ±1.5%（步长 0.5%），并显示标签是否翻转
4b. 敏感性：基准情景每股价值 5x5 表（仅永续 DCF 口径），WACC ±1% × 永续增长 ±1%
5. 期望收益 EV = Σ p_i × (V_i/P − 1)；不对称比 = 牛市涨幅 ÷ |熊市跌幅|；
   P(loss) = 每股价值 < 现价 的情景概率之和；Kelly-lite = 0.25 × Kelly(两点近似：
   win = 牛市涨幅 @ p_bull，loss = 熊市跌幅 @ p_bear)，上限 15%、下限 0；
   仓位标签：<2% 小、2–5% 中、>5% 标准（量级参考，不构成配置建议）
6. EPV（若提供）：正常化 EBIT × (1−税率) − 维持性 capex 调整，除以 WACC，减净债务 → 每股
7. 稳健性检验：在 ±15pp 内把概率推到对当前标签最不利的组合（默认向 bear 移动；
   若当前标签为高估类则向 bull 移动），报告标签是否翻转
   标签规则：加权 FV 相对现价的空间 > +20% 低估；−10%~+20% 合理；< −10% 高估；< −30% 显著高估

同时把全部结构化结果写入与输入同目录的 <case>_output.json。
"""

import json
import math
import os
import sys
import unicodedata

# ---------------------------------------------------------------------------
# 常量与标签
# ---------------------------------------------------------------------------

SCENARIO_ORDER = ["bear", "base", "bull"]
SCENARIO_CN = {"bear": "熊市", "base": "基准", "bull": "牛市"}

# valuation-methods.md §2：情景 horizon 固定 5 年（长期持有口径）
DEFAULT_SCENARIO_HORIZON = 5
# valuation-methods.md §4：方法权重默认值。永续 DCF 对折现率/终值 g 过度敏感，故降权。
DEFAULT_METHOD_WEIGHTS = {"scenario": 0.45, "relative": 0.35, "dcf": 0.20}
METHOD_ORDER = ["scenario", "relative", "dcf"]
METHOD_CN = {
    "scenario": "情景法(H年退出倍数)",
    "relative": "相对估值(合理倍数)",
    "dcf": "永续DCF(Gordon)",
}
MAX_DCF_WEIGHT = 0.30

LABEL_UNDER = "低估"
LABEL_FAIR = "合理"
LABEL_OVER = "高估"
LABEL_VERY_OVER = "显著高估"


class CaseError(Exception):
    """输入数据问题：报错信息面向使用者，不打印裸 traceback。"""


# ---------------------------------------------------------------------------
# 格式化助手
# ---------------------------------------------------------------------------

def fmt_num(x, decimals=2):
    """千分位 + 固定小数位。"""
    if x is None or (isinstance(x, float) and not math.isfinite(x)):
        return "n/a"
    return f"{x:,.{decimals}f}"


def fmt_pct(x, decimals=1):
    """小数 → 百分比字符串（1 位小数）。"""
    if x is None or (isinstance(x, float) and not math.isfinite(x)):
        return "n/a"
    return f"{x * 100:.{decimals}f}%"


def disp_w(text):
    """显示宽度：CJK / 全角字符按 2 列计。"""
    w = 0
    for ch in str(text):
        w += 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1
    return w


def padl(text, width):
    """按显示宽度左对齐。"""
    text = str(text)
    return text + " " * max(0, width - disp_w(text))


def padr(text, width):
    """按显示宽度右对齐。"""
    text = str(text)
    return " " * max(0, width - disp_w(text)) + text


def hr(char="-", width=78):
    return char * width


# ---------------------------------------------------------------------------
# 输入校验
# ---------------------------------------------------------------------------

def require(d, key, types, where):
    if key not in d:
        raise CaseError(f"{where} 缺少必填字段 '{key}'")
    v = d[key]
    if types is float:
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise CaseError(f"{where}.{key} 必须是数字，实际为 {type(v).__name__}: {v!r}")
        return float(v)
    if types is str:
        if not isinstance(v, str):
            raise CaseError(f"{where}.{key} 必须是字符串，实际为 {type(v).__name__}")
        return v
    if types is list:
        if not isinstance(v, list) or not v:
            raise CaseError(f"{where}.{key} 必须是非空数组")
        out = []
        for i, item in enumerate(v):
            if isinstance(item, bool) or not isinstance(item, (int, float)):
                raise CaseError(f"{where}.{key}[{i}] 必须是数字，实际为 {item!r}")
            out.append(float(item))
        return out
    raise CaseError(f"内部错误：未知类型校验 {types}")


def load_case(path):
    """读取并校验 case JSON，返回规范化后的 dict。所有错误以 CaseError 抛出。"""
    if not os.path.isfile(path):
        raise CaseError(f"找不到输入文件: {path}")
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except json.JSONDecodeError as e:
        raise CaseError(f"JSON 解析失败（{path} 第 {e.lineno} 行第 {e.colno} 列）: {e.msg}")
    if not isinstance(raw, dict):
        raise CaseError("输入 JSON 顶层必须是对象 {…}")

    case = {}
    case["company"] = require(raw, "company", str, "顶层")
    case["ticker"] = require(raw, "ticker", str, "顶层")
    case["currency"] = require(raw, "currency", str, "顶层")
    case["valuation_date"] = require(raw, "valuation_date", str, "顶层")
    case["current_price"] = require(raw, "current_price", float, "顶层")
    case["diluted_shares_mm"] = require(raw, "diluted_shares_mm", float, "顶层")
    case["net_debt_mm"] = require(raw, "net_debt_mm", float, "顶层")
    case["wacc"] = require(raw, "wacc", float, "顶层")
    case["terminal_growth"] = require(raw, "terminal_growth", float, "顶层")
    case["annual_dilution_pct"] = float(raw.get("annual_dilution_pct", 0.0) or 0.0)

    warnings = []

    h = raw.get("scenario_horizon_years", DEFAULT_SCENARIO_HORIZON)
    if isinstance(h, bool) or not isinstance(h, int) or h < 5:
        raise CaseError(
            f"scenario_horizon_years 必须是 >= 5 的整数（收到 {h!r}）。"
            "valuation-methods.md §2：三情景 horizon 为 5 年，与长期持有的评估周期对齐。")
    case["scenario_horizon_years"] = h

    mw_raw = raw.get("method_weights")
    if mw_raw is None:
        case["method_weights"] = dict(DEFAULT_METHOD_WEIGHTS)
    else:
        if not isinstance(mw_raw, dict):
            raise CaseError("'method_weights' 必须是对象，键为 scenario/relative/dcf")
        unknown = [k for k in mw_raw if not k.startswith("_") and k not in METHOD_ORDER]
        if unknown:
            raise CaseError(
                f"method_weights 含未知方法: {', '.join(unknown)}；只允许 {', '.join(METHOD_ORDER)}")
        mw = {}
        for m in METHOD_ORDER:
            v = mw_raw.get(m, 0.0)
            if isinstance(v, bool) or not isinstance(v, (int, float)) or v < 0:
                raise CaseError(f"method_weights.{m} 必须是非负数字")
            mw[m] = float(v)
        tot = sum(mw.values())
        if abs(tot - 1.0) > 1e-6:
            raise CaseError(f"method_weights 之和必须为 1，实际为 {tot:.4f}")
        if mw["dcf"] > MAX_DCF_WEIGHT:
            warnings.append(
                f"method_weights.dcf = {fmt_pct(mw['dcf'])} 超过建议上限 "
                f"{fmt_pct(MAX_DCF_WEIGHT)}（valuation-methods.md §4：永续 DCF 对折现率过度敏感，"
                "只作交叉验证）；若确有理由须在报告中显式说明")
        case["method_weights"] = mw

    if case["current_price"] <= 0:
        raise CaseError("current_price 必须为正数")
    if case["diluted_shares_mm"] <= 0:
        raise CaseError("diluted_shares_mm 必须为正数")
    if not (0.0 < case["wacc"] < 0.5):
        raise CaseError(f"wacc={case['wacc']} 超出合理范围 (0, 0.5)；请用小数表示（如 0.09）")
    if case["wacc"] <= case["terminal_growth"]:
        raise CaseError(
            f"wacc ({fmt_pct(case['wacc'])}) 必须大于 terminal_growth "
            f"({fmt_pct(case['terminal_growth'])})，否则 Gordon 终值无定义")

    scen_raw = raw.get("scenarios")
    if not isinstance(scen_raw, dict):
        raise CaseError("缺少 'scenarios' 块（必须包含 bear/base/bull）")
    missing = [k for k in SCENARIO_ORDER if k not in scen_raw]
    if missing:
        raise CaseError(f"'scenarios' 缺少情景: {', '.join(missing)}（必须是 bear/base/bull）")

    scenarios = {}
    horizon = None
    for name in SCENARIO_ORDER:
        s_raw = scen_raw[name]
        if not isinstance(s_raw, dict):
            raise CaseError(f"scenarios.{name} 必须是对象")
        where = f"scenarios.{name}"
        sc = {
            "probability": require(s_raw, "probability", float, where),
            "revenue_mm": require(s_raw, "revenue_mm", float, where),
            "revenue_growth": require(s_raw, "revenue_growth", list, where),
            "fcf_margin": require(s_raw, "fcf_margin", list, where),
        }
        if not (0.0 <= sc["probability"] <= 1.0):
            raise CaseError(f"{where}.probability 必须在 [0,1] 内")
        if sc["revenue_mm"] <= 0:
            raise CaseError(f"{where}.revenue_mm 必须为正数")
        if len(sc["fcf_margin"]) != len(sc["revenue_growth"]):
            raise CaseError(
                f"{where}: fcf_margin 长度 ({len(sc['fcf_margin'])}) 必须与 "
                f"revenue_growth 长度 ({len(sc['revenue_growth'])}) 相同")
        if len(sc["revenue_growth"]) < case["scenario_horizon_years"]:
            raise CaseError(
                f"{where}: 显性期只有 {len(sc['revenue_growth'])} 年，短于 "
                f"scenario_horizon_years={case['scenario_horizon_years']}；"
                "情景法需要至少覆盖到 horizon 年")
        if horizon is None:
            horizon = len(sc["revenue_growth"])
        sc["terminal_growth"] = float(s_raw.get("terminal_growth", case["terminal_growth"]))
        if case["wacc"] <= sc["terminal_growth"]:
            raise CaseError(
                f"{where}.terminal_growth ({fmt_pct(sc['terminal_growth'])}) 必须小于 "
                f"wacc ({fmt_pct(case['wacc'])})")
        em = s_raw.get("exit_multiple")
        if em is not None:
            if isinstance(em, bool) or not isinstance(em, (int, float)) or em <= 0:
                raise CaseError(f"{where}.exit_multiple 必须是正数")
            sc["exit_multiple"] = float(em)
        else:
            sc["exit_multiple"] = None

        ex_raw = s_raw.get("exit")
        if ex_raw is not None:
            if not isinstance(ex_raw, dict):
                raise CaseError(f"{where}.exit 必须是对象")
            metric = str(ex_raw.get("metric", "revenue"))
            if metric not in ("revenue", "fcf", "custom"):
                raise CaseError(f"{where}.exit.metric 只能是 revenue / fcf / custom")
            mult = require(ex_raw, "multiple", float, f"{where}.exit")
            if mult <= 0:
                raise CaseError(f"{where}.exit.multiple 必须是正数")
            metric_mm = None
            if "metric_mm" in ex_raw:
                metric_mm = require(ex_raw, "metric_mm", float, f"{where}.exit")
            elif metric == "custom":
                raise CaseError(f"{where}.exit: metric=custom 时必须提供 metric_mm")
            sc["exit"] = {"metric": metric, "multiple": mult, "metric_mm": metric_mm,
                          "rationale": str(ex_raw.get("rationale", ""))}
        else:
            sc["exit"] = None
            warnings.append(
                f"{where} 缺少 exit 块（H 年退出倍数），情景加权法无法计算；"
                "权重会被重新归一化到其余方法")
        scenarios[name] = sc

    prob_sum = sum(scenarios[n]["probability"] for n in SCENARIO_ORDER)
    if abs(prob_sum - 1.0) > 1e-6:
        raise CaseError(
            f"三情景概率之和必须为 1，实际为 {prob_sum:.6f} "
            f"(bear={scenarios['bear']['probability']}, base={scenarios['base']['probability']}, "
            f"bull={scenarios['bull']['probability']})")
    case["scenarios"] = scenarios

    epv_raw = raw.get("epv")
    if epv_raw is not None:
        if not isinstance(epv_raw, dict):
            raise CaseError("'epv' 块必须是对象")
        case["epv"] = {
            "normalized_ebit_mm": require(epv_raw, "normalized_ebit_mm", float, "epv"),
            "tax_rate": require(epv_raw, "tax_rate", float, "epv"),
            "maintenance_capex_adj_mm": float(epv_raw.get("maintenance_capex_adj_mm", 0.0) or 0.0),
        }
        if not (0.0 <= case["epv"]["tax_rate"] < 1.0):
            raise CaseError("epv.tax_rate 必须在 [0,1) 内")
    else:
        case["epv"] = None

    rel_raw = raw.get("relative")
    if rel_raw is not None:
        if not isinstance(rel_raw, dict):
            raise CaseError("'relative' 块必须是对象")
        if isinstance(rel_raw.get("scenarios"), dict):
            rs_raw = rel_raw["scenarios"]
            miss = [k for k in SCENARIO_ORDER if k not in rs_raw]
            if miss:
                raise CaseError(f"relative.scenarios 缺少情景: {', '.join(miss)}")
            rh = rel_raw.get("horizon_years", case["scenario_horizon_years"])
            if isinstance(rh, bool) or not isinstance(rh, int) or rh < 1:
                raise CaseError("relative.horizon_years 必须是正整数")
            rs = {}
            for name in SCENARIO_ORDER:
                w2 = f"relative.scenarios.{name}"
                d2 = rs_raw[name]
                if not isinstance(d2, dict):
                    raise CaseError(f"{w2} 必须是对象")
                mult = require(d2, "multiple", float, w2)
                if mult <= 0:
                    raise CaseError(f"{w2}.multiple 必须是正数")
                rs[name] = {
                    "metric_mm": require(d2, "metric_mm", float, w2),
                    "multiple": mult,
                    "rationale": str(d2.get("rationale", "")),
                }
            case["relative"] = {
                "mode": "scenario",
                "metric_name": str(rel_raw.get("metric_name", "EV/metric")),
                "metric_label": str(rel_raw.get("metric_label", "")),
                "horizon_years": rh,
                "scenarios": rs,
            }
        else:
            case["relative"] = {
                "mode": "legacy",
                "metric_name": str(rel_raw.get("metric_name", "metric")),
                "metric_per_share": require(rel_raw, "metric_per_share", float, "relative"),
                "multiple_low": require(rel_raw, "multiple_low", float, "relative"),
                "multiple_mid": require(rel_raw, "multiple_mid", float, "relative"),
                "multiple_high": require(rel_raw, "multiple_high", float, "relative"),
            }
            warnings.append(
                "relative 使用旧版「每股指标 × 倍数」口径：只展示、不参与方法加权。"
                "改用 relative.scenarios（三情景合理倍数 + H 年指标）才能计入权重")
    else:
        case["relative"] = None
        warnings.append("未提供 relative 块，相对估值权重将被重新归一化到其余方法")

    case["_warnings"] = warnings
    return case


# ---------------------------------------------------------------------------
# 核心计算（纯函数）
# ---------------------------------------------------------------------------

def effective_shares_mm(case, n_years):
    """显性期末的有效股本：稀释后股本 × (1+年度稀释率)^n。"""
    return case["diluted_shares_mm"] * (1.0 + case["annual_dilution_pct"]) ** n_years


def dcf_cashflows(revenue_mm, growth_path, margin_path):
    """逐年收入与 FCF（百万）。"""
    revenues, fcfs = [], []
    rev = revenue_mm
    for g, m in zip(growth_path, margin_path):
        rev = rev * (1.0 + g)
        revenues.append(rev)
        fcfs.append(rev * m)
    return revenues, fcfs


def dcf_value(case, revenue_mm, growth_path, margin_path, wacc=None, term_g=None,
              exit_multiple=None):
    """单套假设的完整 DCF。返回结构化 dict；每股价值以 Gordon 终值为主口径。

    wacc/term_g 缺省取 case 顶层值（敏感性分析会覆盖）。
    """
    w = case["wacc"] if wacc is None else wacc
    tg = case["terminal_growth"] if term_g is None else term_g
    if w <= tg:
        return None  # 由调用方决定如何展示（敏感性表打 n/a）

    revenues, fcfs = dcf_cashflows(revenue_mm, growth_path, margin_path)
    n = len(fcfs)
    pv_explicit = sum(f / (1.0 + w) ** (t + 1) for t, f in enumerate(fcfs))

    fcf_n = fcfs[-1]
    tv_gordon = fcf_n * (1.0 + tg) / (w - tg)
    pv_tv_gordon = tv_gordon / (1.0 + w) ** n
    implied_exit_pfcf = tv_gordon / fcf_n if fcf_n > 0 else float("nan")

    shares = effective_shares_mm(case, n)

    def per_share(pv_tv):
        equity = pv_explicit + pv_tv - case["net_debt_mm"]
        return equity, equity / shares

    equity_g, ps_g = per_share(pv_tv_gordon)

    out = {
        "years": n,
        "revenues_mm": revenues,
        "fcfs_mm": fcfs,
        "pv_explicit_mm": pv_explicit,
        "tv_gordon_mm": tv_gordon,
        "pv_tv_gordon_mm": pv_tv_gordon,
        "implied_exit_p_fcf": implied_exit_pfcf,
        "equity_value_mm": equity_g,
        "per_share": ps_g,
        "effective_shares_mm": shares,
        "terminal_growth": tg,
        "wacc": w,
    }
    if exit_multiple is not None:
        tv_exit = fcf_n * exit_multiple
        pv_tv_exit = tv_exit / (1.0 + w) ** n
        equity_e, ps_e = per_share(pv_tv_exit)
        out["exit_multiple"] = exit_multiple
        out["tv_exit_mm"] = tv_exit
        out["pv_tv_exit_mm"] = pv_tv_exit
        out["equity_value_exit_mm"] = equity_e
        out["per_share_exit"] = ps_e
    return out


def scenario_dcf(case, name, wacc=None, term_g=None):
    sc = case["scenarios"][name]
    tg = sc["terminal_growth"] if term_g is None else term_g
    return dcf_value(case, sc["revenue_mm"], sc["revenue_growth"], sc["fcf_margin"],
                     wacc=wacc, term_g=tg, exit_multiple=sc["exit_multiple"])


def horizon_fcf_sum_mm(case, name, years):
    """情景在前 years 年的累计 FCF（负数 = 净烧钱）。"""
    sc = case["scenarios"][name]
    _, fcfs = dcf_cashflows(sc["revenue_mm"], sc["revenue_growth"], sc["fcf_margin"])
    return sum(fcfs[:years]), fcfs


def _horizon_equity(case, name, years, ev_h):
    """H 年末：净债务 = 期初净债务 − 期间累计 FCF；股权 = EV − 净债务；股本按稀释率外推。"""
    cum, _ = horizon_fcf_sum_mm(case, name, years)
    nd_h = case["net_debt_mm"] - cum
    equity_h = ev_h - nd_h
    shares_h = effective_shares_mm(case, years)
    return nd_h, equity_h, shares_h, equity_h / shares_h


def exit_multiple_value(case, name, wacc=None):
    """方法一「情景加权」：H 年末 EV = 退出倍数 x H 年指标，扣 H 年末净债务，折现回今天。

    不含永续增长项，只做 H 年折现，因此对 WACC 与终值 g 的敏感度显著低于 Gordon DCF。
    """
    sc = case["scenarios"][name]
    ex = sc.get("exit")
    if ex is None:
        return None
    w = case["wacc"] if wacc is None else wacc
    h = case["scenario_horizon_years"]
    revenues, fcfs = dcf_cashflows(sc["revenue_mm"], sc["revenue_growth"], sc["fcf_margin"])
    if ex["metric_mm"] is not None:
        metric = ex["metric_mm"]
    elif ex["metric"] == "revenue":
        metric = revenues[h - 1]
    else:
        metric = fcfs[h - 1]
    ev_h = ex["multiple"] * metric
    nd_h, eq_h, sh_h, ps_h = _horizon_equity(case, name, h, ev_h)
    return {"horizon_years": h, "metric": ex["metric"], "metric_mm": metric,
            "multiple": ex["multiple"], "rationale": ex["rationale"],
            "ev_horizon_mm": ev_h, "net_debt_horizon_mm": nd_h,
            "equity_horizon_mm": eq_h, "shares_horizon_mm": sh_h,
            "per_share_horizon": ps_h, "per_share": ps_h / (1.0 + w) ** h, "wacc": w}


def relative_scenario_value(case, name, wacc=None):
    """方法二「相对估值」：合理倍数（peer/自身历史推导）x H 年指标，同样折现回今天。"""
    rel = case["relative"]
    if rel is None or rel.get("mode") != "scenario":
        return None
    w = case["wacc"] if wacc is None else wacc
    h = rel["horizon_years"]
    d = rel["scenarios"][name]
    ev_h = d["multiple"] * d["metric_mm"]
    nd_h, eq_h, sh_h, ps_h = _horizon_equity(case, name, h, ev_h)
    return {"horizon_years": h, "metric_mm": d["metric_mm"], "multiple": d["multiple"],
            "rationale": d["rationale"], "ev_horizon_mm": ev_h,
            "net_debt_horizon_mm": nd_h, "equity_horizon_mm": eq_h,
            "shares_horizon_mm": sh_h, "per_share_horizon": ps_h,
            "per_share": ps_h / (1.0 + w) ** h, "wacc": w}


def method_values(case, wacc=None):
    """返回 {method: {scenario: 每股价值}}；某方法任一情景缺数据则整个方法不出现。"""
    out = {}
    for key, fn in (("scenario", exit_multiple_value),
                    ("relative", relative_scenario_value),
                    ("dcf", None)):
        vals = {}
        ok = True
        for n in SCENARIO_ORDER:
            r = scenario_dcf(case, n, wacc=wacc) if fn is None else fn(case, n, wacc=wacc)
            if r is None:
                ok = False
                break
            vals[n] = r["per_share"]
        if ok:
            out[key] = vals
    return out


def effective_method_weights(case, available):
    """按可用方法重新归一化权重；返回 (weights, note)。"""
    w = {m: case["method_weights"][m] for m in METHOD_ORDER if m in available}
    tot = sum(w.values())
    if tot <= 0:
        raise CaseError("没有任何可用估值方法：检查 scenarios.*.exit 与 relative.scenarios")
    note = None
    if abs(tot - 1.0) > 1e-9:
        missing = [METHOD_CN[m] for m in METHOD_ORDER if m not in available]
        note = (f"缺少方法 [{', '.join(missing) or '-'}]，权重按可用方法归一化"
                f"（原合计 {tot:.2f}）")
        w = {k: v / tot for k, v in w.items()}
    return w, note


def blend(case, wacc=None):
    """方法加权 → 每情景混合每股价值 → 概率加权公允价值（本脚本的主口径）。"""
    mv = method_values(case, wacc=wacc)
    w, note = effective_method_weights(case, mv)
    blended = {n: sum(w[m] * mv[m][n] for m in w) for n in SCENARIO_ORDER}
    probs = {n: case["scenarios"][n]["probability"] for n in SCENARIO_ORDER}
    per_method_fv = {m: sum(probs[n] * mv[m][n] for n in SCENARIO_ORDER) for m in mv}
    return {"method_values": mv, "weights": w, "weight_note": note,
            "blended_scenario_values": blended, "per_method_fv": per_method_fv,
            "fair_value": sum(probs[n] * blended[n] for n in SCENARIO_ORDER)}


def wacc_sensitivity_blended(case, steps=(-0.015, -0.01, -0.005, 0.0, 0.005, 0.01, 0.015)):
    """混合公允价值对 WACC 的敏感性——用于展示降权后对折现率的依赖度。"""
    rows = []
    price = case["current_price"]
    for st in steps:
        w = case["wacc"] + st
        if w <= 0.005:
            continue
        try:
            b = blend(case, wacc=w)
        except CaseError:
            continue
        ups = b["fair_value"] / price - 1.0
        rows.append({"wacc": w, "fair_value": b["fair_value"],
                     "upside": ups, "label": label_for_upside(ups)})
    return rows


def weighted_fair_value(case, results):
    """旧口径：仅 Gordon DCF 的概率加权（保留供交叉对照）。"""
    return sum(case["scenarios"][n]["probability"] * results[n]["per_share"]
               for n in SCENARIO_ORDER)


def label_for_upside(upside):
    """标签规则：>+20% 低估；−10%~+20% 合理；<−10% 高估；<−30% 显著高估。"""
    if upside > 0.20:
        return LABEL_UNDER
    if upside >= -0.10:
        return LABEL_FAIR
    if upside < -0.30:
        return LABEL_VERY_OVER
    return LABEL_OVER


def bisect_solve(fn, lo, hi, target, tol=1e-7, max_iter=200):
    """在 [lo, hi] 上二分求 fn(x) = target；fn 需单调递增。无法夹住根时返回 None。"""
    f_lo = fn(lo) - target
    f_hi = fn(hi) - target
    if f_lo is None or f_hi is None or math.isnan(f_lo) or math.isnan(f_hi):
        return None
    if f_lo * f_hi > 0:
        return None
    for _ in range(max_iter):
        mid = (lo + hi) / 2.0
        f_mid = fn(mid) - target
        if abs(f_mid) < tol or (hi - lo) < tol:
            return mid
        if f_lo * f_mid <= 0:
            hi = mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2.0


def reverse_dcf(case):
    """反向 DCF：(a) 倒解固定收入增速（用基准利润率路径）；(b) 倒解固定 FCF 利润率
    （用基准增速路径）。终值增长率与 WACC 用顶层/基准情景口径。"""
    base = case["scenarios"]["base"]
    price = case["current_price"]
    tg = base["terminal_growth"]
    n = len(base["revenue_growth"])

    def ps_for_growth(g):
        r = dcf_value(case, base["revenue_mm"], [g] * n, base["fcf_margin"], term_g=tg)
        return r["per_share"] if r else float("nan")

    def ps_for_margin(m):
        r = dcf_value(case, base["revenue_mm"], base["revenue_growth"], [m] * n, term_g=tg)
        return r["per_share"] if r else float("nan")

    implied_g = bisect_solve(ps_for_growth, -0.60, 1.50, price)
    implied_m = bisect_solve(ps_for_margin, 1e-6, 1.0, price)

    base_avg_g = sum(base["revenue_growth"]) / n
    base_avg_m = sum(base["fcf_margin"]) / n
    return {
        "implied_constant_growth": implied_g,
        "base_avg_growth": base_avg_g,
        "implied_constant_fcf_margin": implied_m,
        "base_avg_fcf_margin": base_avg_m,
        "horizon_years": n,
    }


def sensitivity_grid(case, steps=(-0.01, -0.005, 0.0, 0.005, 0.01)):
    """基准情景每股价值：WACC ±1% × 永续增长 ±1%，步长 0.5%（5×5）。"""
    base_tg = case["scenarios"]["base"]["terminal_growth"]
    waccs = [case["wacc"] + s for s in steps]
    tgs = [base_tg + s for s in steps]
    grid = []
    for w in waccs:
        row = []
        for t in tgs:
            r = scenario_dcf(case, "base", wacc=w, term_g=t) if w > t else None
            row.append(r["per_share"] if r else None)
        grid.append(row)
    return {"waccs": waccs, "terminal_growths": tgs, "per_share": grid}


def position_metrics(case, values):
    """valuation-methods.md §4：EV、不对称比、P(loss)、Kelly-lite、仓位标签。
    values = 每情景「方法加权后」的每股价值。"""
    price = case["current_price"]
    probs = {n: case["scenarios"][n]["probability"] for n in SCENARIO_ORDER}
    rets = {n: values[n] / price - 1.0 for n in SCENARIO_ORDER}

    ev = sum(probs[n] * rets[n] for n in SCENARIO_ORDER)
    bull_up = rets["bull"]
    bear_down = -rets["bear"]  # 正数 = 跌幅
    asymmetry = (bull_up / bear_down) if (bull_up > 0 and bear_down > 0) else None

    p_loss = sum(probs[n] for n in SCENARIO_ORDER if values[n] < price)
    base_below = values["base"] < price

    # Kelly 两点近似：win = 牛市涨幅 @ p_bull；loss = 熊市跌幅 @ p_bear
    kelly_note = None
    if bull_up <= 0:
        kelly_raw = 0.0
        kelly_note = "牛市情景无上行，Kelly 记 0"
    elif bear_down <= 0:
        kelly_raw = float("inf")
        kelly_note = "熊市情景每股价值仍高于现价（无下行），Kelly-lite 触顶"
    else:
        kelly_raw = probs["bull"] / bear_down - probs["bear"] / bull_up
    kelly_lite = 0.25 * kelly_raw if math.isfinite(kelly_raw) else 0.15
    kelly_lite = max(0.0, min(0.15, kelly_lite))

    if kelly_lite < 0.02:
        pos_label = "小"
    elif kelly_lite <= 0.05:
        pos_label = "中"
    else:
        pos_label = "标准"

    return {
        "expected_return": ev,
        "scenario_returns": rets,
        "bull_upside": bull_up,
        "bear_downside": bear_down,
        "asymmetry_ratio": asymmetry,
        "p_loss": p_loss,
        "base_below_price": base_below,
        "kelly_raw": kelly_raw if math.isfinite(kelly_raw) else None,
        "kelly_lite": kelly_lite,
        "position_label": pos_label,
        "kelly_note": kelly_note,
    }


def epv_value(case):
    """EPV = (正常化 EBIT × (1−税率) − 维持性 capex 调整) / WACC − 净债务 → 每股。"""
    e = case["epv"]
    if e is None:
        return None
    nopat = e["normalized_ebit_mm"] * (1.0 - e["tax_rate"]) - e["maintenance_capex_adj_mm"]
    ev = nopat / case["wacc"]
    equity = ev - case["net_debt_mm"]
    per_share = equity / case["diluted_shares_mm"]
    return {"normalized_nopat_mm": nopat, "enterprise_value_mm": ev,
            "equity_value_mm": equity, "per_share": per_share}


def relative_value(case):
    r = case["relative"]
    if r is None or r.get("mode") == "scenario":
        return None
    return {
        "metric_name": r["metric_name"],
        "metric_per_share": r["metric_per_share"],
        "per_share_low": r["metric_per_share"] * r["multiple_low"],
        "per_share_mid": r["metric_per_share"] * r["multiple_mid"],
        "per_share_high": r["metric_per_share"] * r["multiple_high"],
        "multiples": [r["multiple_low"], r["multiple_mid"], r["multiple_high"]],
    }


def shift_probs(probs, direction, pp=0.15):
    """把最多 pp 的概率移向 direction（'bear' 或 'bull'）。
    向 bear 移：先从 bull 抽，不够再从 base 抽；向 bull 移对称。返回新概率 dict。"""
    p = dict(probs)
    if direction == "bear":
        donors, receiver = ["bull", "base"], "bear"
    else:
        donors, receiver = ["bear", "base"], "bull"
    remaining = pp
    for d in donors:
        take = min(remaining, p[d])
        p[d] -= take
        p[receiver] += take
        remaining -= take
        if remaining <= 1e-12:
            break
    return p


def robustness_check(case, values):
    """±15pp 内找对当前标签最不利的概率组合：低估/合理 → 向 bear 移；
    高估/显著高估 → 向 bull 移。报告标签是否翻转。"""
    price = case["current_price"]
    probs = {n: case["scenarios"][n]["probability"] for n in SCENARIO_ORDER}

    fv0 = sum(probs[n] * values[n] for n in SCENARIO_ORDER)
    label0 = label_for_upside(fv0 / price - 1.0)

    direction = "bear" if label0 in (LABEL_UNDER, LABEL_FAIR) else "bull"
    adverse = shift_probs(probs, direction)
    fv1 = sum(adverse[n] * values[n] for n in SCENARIO_ORDER)
    label1 = label_for_upside(fv1 / price - 1.0)

    return {
        "original_probs": probs,
        "original_fv": fv0,
        "original_label": label0,
        "adverse_direction": direction,
        "adverse_probs": adverse,
        "adverse_fv": fv1,
        "adverse_label": label1,
        "label_flipped": label1 != label0,
    }


# ---------------------------------------------------------------------------
# 报告输出
# ---------------------------------------------------------------------------

def render_report(case, results, bl, rev, grid, wgrid, pos, epv, rel, robust):
    L = []
    price = case["current_price"]
    ccy = case["currency"]

    L.append(hr("="))
    L.append(f"{case['company']} ({case['ticker']})  估值报告   "
             f"基准日 {case['valuation_date']}   币种 {ccy}")
    L.append(f"现价 {fmt_num(price)}   股本 {fmt_num(case['diluted_shares_mm'], 1)}mm   "
             f"净债务 {fmt_num(case['net_debt_mm'], 0)}mm"
             f"{'（净现金）' if case['net_debt_mm'] < 0 else ''}   "
             f"WACC {fmt_pct(case['wacc'])}   永续 g {fmt_pct(case['terminal_growth'])}   "
             f"年稀释 {fmt_pct(case['annual_dilution_pct'])}   "
             f"情景 horizon {case['scenario_horizon_years']}Y")
    L.append(hr("="))
    for w in case["_warnings"]:
        L.append(f"[提示] {w}")

    # 1. 每情景 DCF
    L.append("")
    L.append(f"[1] 永续 DCF 明细（Gordon 终值；方法权重 "
             f"{fmt_pct(bl['weights'].get('dcf', 0.0))}）")
    header = (f"  {'情景':<6}{'概率':>7}{'显性PV(mm)':>14}{'终值PV(mm)':>14}"
              f"{'股权价值(mm)':>15}{'每股价值':>12}{'vs现价':>9}{'隐含退出P/FCF':>15}")
    L.append(header)
    L.append("  " + hr("-", len(header) - 2))
    for n in SCENARIO_ORDER:
        r = results[n]
        p = case["scenarios"][n]["probability"]
        ups = r["per_share"] / price - 1.0
        pfcf = r["implied_exit_p_fcf"]
        pfcf_str = fmt_num(pfcf, 1) + "x" if math.isfinite(pfcf) else "n/a"
        L.append(f"  {SCENARIO_CN[n]:<5}{fmt_pct(p):>8}{fmt_num(r['pv_explicit_mm'], 0):>15}"
                 f"{fmt_num(r['pv_tv_gordon_mm'], 0):>15}{fmt_num(r['equity_value_mm'], 0):>16}"
                 f"{fmt_num(r['per_share']):>12}{fmt_pct(ups):>9}"
                 f"{pfcf_str:>14}")
        if r.get("exit_multiple") is not None:
            ups_e = r["per_share_exit"] / price - 1.0
            L.append(f"    └ 退出倍数口径 {fmt_num(r['exit_multiple'], 1)}x P/FCF: "
                     f"终值PV {fmt_num(r['pv_tv_exit_mm'], 0)}mm, "
                     f"每股 {fmt_num(r['per_share_exit'])} ({fmt_pct(ups_e)} vs 现价)")
        if r["implied_exit_p_fcf"] > 25 and r["terminal_growth"] <= 0.035:
            L.append(f"    [base-rates §4] 隐含退出 P/FCF {fmt_num(r['implied_exit_p_fcf'], 1)}x "
                     f"> 25x 而稳态增速仅 {fmt_pct(r['terminal_growth'])} —— 终值假设偏乐观，需复核")

    # 2. 方法加权汇总（主口径）
    wfv = bl["fair_value"]
    upside_w = wfv / price - 1.0
    label = label_for_upside(upside_w)
    L.append("")
    L.append(f"[2] 方法加权 x 概率加权公允价值（主口径，horizon {case['scenario_horizon_years']}Y）")
    if bl["weight_note"]:
        L.append(f"  [注] {bl['weight_note']}")
    mv = bl["method_values"]
    cols = (22, 8, 11, 11, 11, 13, 9)
    L.append("  " + padl("方法", cols[0]) + padr("权重", cols[1])
             + padr("熊市", cols[2]) + padr("基准", cols[3]) + padr("牛市", cols[4])
             + padr("概率加权FV", cols[5]) + padr("vs现价", cols[6]))
    L.append("  " + hr("-", sum(cols)))
    for m in METHOD_ORDER:
        if m not in mv:
            continue
        v = mv[m]
        L.append("  " + padl(METHOD_CN[m], cols[0])
                 + padr(fmt_pct(bl["weights"][m]), cols[1])
                 + padr(fmt_num(v["bear"]), cols[2]) + padr(fmt_num(v["base"]), cols[3])
                 + padr(fmt_num(v["bull"]), cols[4])
                 + padr(fmt_num(bl["per_method_fv"][m]), cols[5])
                 + padr(fmt_pct(bl["per_method_fv"][m] / price - 1.0), cols[6]))
    b = bl["blended_scenario_values"]
    L.append("  " + hr("-", sum(cols)))
    L.append("  " + padl("→ 方法加权后", cols[0]) + padr(fmt_pct(1.0), cols[1])
             + padr(fmt_num(b["bear"]), cols[2]) + padr(fmt_num(b["base"]), cols[3])
             + padr(fmt_num(b["bull"]), cols[4]) + padr(fmt_num(wfv), cols[5])
             + padr(fmt_pct(upside_w), cols[6]))
    L.append("")
    L.append(f"  公允价值 = {fmt_num(wfv)} {ccy}/股   vs 现价 {fmt_num(price)} → "
             f"空间 {fmt_pct(upside_w)}   标签: {label}")
    L.append("  （标签规则: >+20% 低估 / −10%~+20% 合理 / <−10% 高估 / <−30% 显著高估）")
    L.append("  （下游的期望收益/赔率/稳健性检验全部基于「方法加权后」的每情景价值）")

    # 3. 反向 DCF
    L.append("")
    L.append("[3] 反向 DCF（诊断用，权重 0：只说明现价隐含什么，不参与公允价值）")
    ig, im = rev["implied_constant_growth"], rev["implied_constant_fcf_margin"]
    if ig is not None:
        cmp_g = "高于" if ig > rev["base_avg_growth"] else "低于"
        L.append(f"  a) 隐含固定收入增速（持基准利润率路径）: {fmt_pct(ig)} /年 × {rev['horizon_years']} 年")
        L.append(f"     解读: 市场定价隐含增速 {fmt_pct(ig)}，{cmp_g}基准假设均值 "
                 f"{fmt_pct(rev['base_avg_growth'])} —— 现价对增长的要求"
                 f"{'更苛刻' if ig > rev['base_avg_growth'] else '并不苛刻'}。")
    else:
        L.append("  a) 隐含收入增速: 在 [-60%, +150%] 区间内无解（现价与假设结构差距过大）")
    if im is not None:
        cmp_m = "高于" if im > rev["base_avg_fcf_margin"] else "低于"
        L.append(f"  b) 隐含固定 FCF 利润率（持基准增速路径）: {fmt_pct(im)}")
        L.append(f"     解读: 市场定价隐含利润率 {fmt_pct(im)}，{cmp_m}基准假设均值 "
                 f"{fmt_pct(rev['base_avg_fcf_margin'])} —— 利润率端的预期"
                 f"{'偏高' if im > rev['base_avg_fcf_margin'] else '留有余地'}。")
    else:
        L.append("  b) 隐含 FCF 利润率: 在 (0, 100%] 区间内无解（现价与假设结构差距过大）")

    # 4. 敏感性
    L.append("")
    L.append("[4a] 折现率敏感性: 方法加权公允价值 vs WACC（±1.5%，步长 0.5%）")
    lab_w = 10
    L.append("  " + padr("WACC", lab_w) + "".join(padr(fmt_pct(r["wacc"]), 11) for r in wgrid))
    L.append("  " + padr("公允价值", lab_w) + "".join(padr(fmt_num(r["fair_value"]), 11) for r in wgrid))
    L.append("  " + padr("vs 现价", lab_w) + "".join(padr(fmt_pct(r["upside"]), 11) for r in wgrid))
    L.append("  " + padr("标签", lab_w) + "".join(padr(r["label"], 11) for r in wgrid))
    if wgrid:
        span = max(r["fair_value"] for r in wgrid) - min(r["fair_value"] for r in wgrid)
        mid = wgrid[len(wgrid) // 2]["fair_value"]
        L.append(f"  解读: WACC ±1.5% 使公允价值波动 {fmt_num(span)} "
                 f"({fmt_pct(span / mid if mid else float('nan'))} of 中值)；"
                 f"标签是否随折现率翻转见上行。")
    L.append("")
    L.append("[4b] 敏感性: 基准情景每股价值（仅永续 DCF 口径）— WACC ±1% × 永续增长 ±1%（步长 0.5%）")
    tgs = grid["terminal_growths"]
    corner = "WACC \\ g"
    head = "  " + f"{corner:>9} |" + "".join(f"{fmt_pct(t):>11}" for t in tgs)
    L.append(head)
    L.append("  " + hr("-", len(head) - 2))
    for w, row in zip(grid["waccs"], grid["per_share"]):
        cells = "".join(f"{fmt_num(v):>11}" if v is not None else f"{'n/a':>11}" for v in row)
        L.append("  " + f"{fmt_pct(w):>9} |" + cells)

    # 5. 期望收益与仓位思维
    L.append("")
    L.append("[5] 期望收益与赔率结构 (valuation-methods.md §4)")
    L.append(f"  期望收益 EV = Σ p_i×(V_i/P−1) = {fmt_pct(pos['expected_return'])}")
    L.append(f"  牛市上行 {fmt_pct(pos['bull_upside'])}   熊市下行 {fmt_pct(-pos['bear_downside'])}   "
             f"不对称比 = {fmt_num(pos['asymmetry_ratio']) if pos['asymmetry_ratio'] else 'n/a'}"
             f"{'   [<1.5 的低估多半不值得建仓]' if pos['asymmetry_ratio'] is not None and pos['asymmetry_ratio'] < 1.5 else ''}")
    base_note = "（注意: 基准情景每股价值低于现价）" if pos["base_below_price"] else ""
    L.append(f"  P(loss) = {fmt_pct(pos['p_loss'])} {base_note}")
    kn = f"   [{pos['kelly_note']}]" if pos["kelly_note"] else ""
    L.append(f"  Kelly-lite = ¼×Kelly(两点近似) = {fmt_pct(pos['kelly_lite'])} "
             f"(上限 15%, 下限 0){kn}")
    L.append(f"  该赔率结构支持 「{pos['position_label']}」 仓位 "
             f"(<2% 小 / 2–5% 中 / >5% 标准) —— 仅量级参考，不构成配置建议。")

    # 6. EPV
    if epv is not None:
        L.append("")
        L.append("[6] EPV 无增长锚 (正常化 EBIT×(1−t) − 维持性capex调整) / WACC − 净债务")
        L.append(f"  正常化 NOPAT {fmt_num(epv['normalized_nopat_mm'], 0)}mm → EV "
                 f"{fmt_num(epv['enterprise_value_mm'], 0)}mm → 股权 "
                 f"{fmt_num(epv['equity_value_mm'], 0)}mm → 每股 {fmt_num(epv['per_share'])} "
                 f"({fmt_pct(epv['per_share'] / price - 1.0)} vs 现价)")
        L.append("  解读: EPV 是零增长下的盈利能力价值；现价高出 EPV 的部分即市场为增长支付的溢价。")

    # 6b. 相对估值
    if rel is not None:
        L.append("")
        L.append(f"[6b] 相对估值快算 ({rel['metric_name']} = {fmt_num(rel['metric_per_share'])}/股)")
        L.append(f"  倍数 {fmt_num(rel['multiples'][0], 1)}x / {fmt_num(rel['multiples'][1], 1)}x / "
                 f"{fmt_num(rel['multiples'][2], 1)}x → 每股 "
                 f"{fmt_num(rel['per_share_low'])} / {fmt_num(rel['per_share_mid'])} / "
                 f"{fmt_num(rel['per_share_high'])}")

    # 7. 稳健性检验
    L.append("")
    L.append("[7] 稳健性检验（基于方法加权后价值；±15pp 内对标签最不利的概率组合，向 "
             f"{SCENARIO_CN[robust['adverse_direction']]}移动）")
    op, ap = robust["original_probs"], robust["adverse_probs"]
    L.append(f"  原概率  bear/base/bull = {fmt_pct(op['bear'])}/{fmt_pct(op['base'])}/{fmt_pct(op['bull'])}"
             f" → FV {fmt_num(robust['original_fv'])} ({robust['original_label']})")
    L.append(f"  不利组合 bear/base/bull = {fmt_pct(ap['bear'])}/{fmt_pct(ap['base'])}/{fmt_pct(ap['bull'])}"
             f" → FV {fmt_num(robust['adverse_fv'])} ({robust['adverse_label']})")
    if robust["label_flipped"]:
        L.append(f"  结论: 标签翻转（{robust['original_label']} → {robust['adverse_label']}）"
                 f"—— 结论对概率敏感，报告中须如实说明。")
    else:
        L.append(f"  结论: 标签未翻转，仍为「{robust['original_label']}」—— 结论对 ±15pp 概率扰动稳健。")

    L.append("")
    L.append(hr("="))
    return "\n".join(L)


# ---------------------------------------------------------------------------
# 示例 JSON
# ---------------------------------------------------------------------------

EXAMPLE_CASE = {
    "_comment": "dcf.py 示例 case。所有 _ 开头的键都是注释，会被忽略；可直接运行: python3 dcf.py example.json",
    "company": "Example Corp",
    "ticker": "EXMP",
    "currency": "USD",
    "valuation_date": "2026-08-25",
    "_comment_price": "current_price = 当前股价; diluted_shares_mm = 稀释股本(百万); net_debt_mm 负数表示净现金",
    "current_price": 150.0,
    "diluted_shares_mm": 1000.0,
    "net_debt_mm": -5000.0,
    "_comment_rates": "wacc/terminal_growth 用小数; annual_dilution_pct 为可选的年度股本稀释率",
    "wacc": 0.09,
    "terminal_growth": 0.03,
    "annual_dilution_pct": 0.01,
    "_comment_horizon": "情景 horizon 固定 5 年(>=5)；方法权重和必须为 1，dcf 建议 <= 0.30",
    "scenario_horizon_years": 5,
    "method_weights": {"scenario": 0.45, "relative": 0.35, "dcf": 0.20},
    "scenarios": {
        "_comment": "三情景必须齐备且概率和为 1; revenue_growth 与 fcf_margin 等长(允许利润率爬坡)",
        "bear": {
            "probability": 0.25,
            "revenue_mm": 50000,
            "revenue_growth": [0.02, 0.02, 0.01, 0.01, 0.0],
            "fcf_margin": [0.16, 0.15, 0.15, 0.14, 0.14],
            "_comment": "terminal_growth 可按情景覆盖顶层值",
            "terminal_growth": 0.02,
            "_comment_exit": "exit = 情景加权法输入：H(=5) 年 EV 倍数 x H 年指标",
            "exit": {"metric": "fcf", "multiple": 12,
                     "rationale": "增长停滞的成熟公司，退出 P/FCF 给同业低分位"}
        },
        "base": {
            "probability": 0.50,
            "revenue_mm": 50000,
            "revenue_growth": [0.08, 0.07, 0.07, 0.06, 0.05],
            "fcf_margin": [0.18, 0.18, 0.19, 0.19, 0.20],
            "exit": {"metric": "fcf", "multiple": 17,
                     "rationale": "中个位数增长 + 稳定 ROIC，给同业中位"}
        },
        "bull": {
            "probability": 0.25,
            "revenue_mm": 50000,
            "revenue_growth": [0.14, 0.13, 0.12, 0.10, 0.09],
            "fcf_margin": [0.20, 0.21, 0.22, 0.22, 0.23],
            "_comment": "exit_multiple(P/FCF) 只影响 [1] 永续 DCF 的并列展示",
            "exit_multiple": 22,
            "exit": {"metric": "fcf", "multiple": 22,
                     "rationale": "份额与利润率同升，给同业上分位"}
        }
    },
    "epv": {
        "_comment": "可选。EPV = (EBIT×(1−t) − maintenance_capex_adj) / WACC − 净债务",
        "normalized_ebit_mm": 9000,
        "tax_rate": 0.21,
        "maintenance_capex_adj_mm": 500
    },
    "relative": {
        "_comment": "三情景口径(计入权重)。合理倍数须自行推导，不许直接抄同业中位数",
        "metric_name": "EV/EBITDA",
        "metric_label": "FY2031E",
        "horizon_years": 5,
        "scenarios": {
            "bear": {"metric_mm": 9500, "multiple": 7.0,
                     "rationale": "增长停滞，较同业中位 10x 折价 30%"},
            "base": {"metric_mm": 12500, "multiple": 10.0,
                     "rationale": "与同业中位持平，ROIC 相当"},
            "bull": {"metric_mm": 16500, "multiple": 13.0,
                     "rationale": "增速高于同业 5pct，给 30% 溢价"}
        }
    }
}


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def build_output_json(case, results, bl, rev, grid, wgrid, pos, epv, rel, robust):
    price = case["current_price"]
    scen_out = {}
    for n in SCENARIO_ORDER:
        r = results[n]
        scen_out[n] = {
            "probability": case["scenarios"][n]["probability"],
            "pv_explicit_mm": r["pv_explicit_mm"],
            "tv_gordon_mm": r["tv_gordon_mm"],
            "pv_tv_gordon_mm": r["pv_tv_gordon_mm"],
            "equity_value_mm": r["equity_value_mm"],
            "per_share": r["per_share"],
            "upside_vs_price": r["per_share"] / price - 1.0,
            "implied_exit_p_fcf": r["implied_exit_p_fcf"],
            "terminal_growth": r["terminal_growth"],
            "effective_shares_mm": r["effective_shares_mm"],
        }
        if r.get("exit_multiple") is not None:
            scen_out[n].update({
                "exit_multiple": r["exit_multiple"],
                "tv_exit_mm": r["tv_exit_mm"],
                "per_share_exit": r["per_share_exit"],
            })
        ex = exit_multiple_value(case, n)
        if ex is not None:
            scen_out[n]["scenario_exit_method"] = ex
        rs = relative_scenario_value(case, n)
        if rs is not None:
            scen_out[n]["relative_method"] = rs
        scen_out[n]["blended_per_share"] = bl["blended_scenario_values"][n]
    wfv = bl["fair_value"]
    upside_w = wfv / price - 1.0
    return {
        "meta": {k: case[k] for k in ("company", "ticker", "currency", "valuation_date",
                                       "current_price", "diluted_shares_mm", "net_debt_mm",
                                       "wacc", "terminal_growth", "annual_dilution_pct",
                                       "scenario_horizon_years", "method_weights")},
        "scenarios": scen_out,
        "method_blend": {
            "weights": bl["weights"],
            "weight_note": bl["weight_note"],
            "per_method_fair_value": bl["per_method_fv"],
            "blended_scenario_values": bl["blended_scenario_values"],
        },
        "weighted_fair_value": wfv,
        "weighted_upside": upside_w,
        "label": label_for_upside(upside_w),
        "dcf_only_fair_value": weighted_fair_value(case, results),
        "reverse_dcf": rev,
        "sensitivity": grid,
        "wacc_sensitivity_blended": wgrid,
        "position": pos,
        "epv": epv,
        "relative": rel,
        "robustness": robust,
    }


def sanitize_json(obj):
    """把 NaN/Inf 替换为 None，保证写出的 JSON 严格合法（RFC 8259 不允许 NaN）。"""
    if isinstance(obj, float) and not math.isfinite(obj):
        return None
    if isinstance(obj, dict):
        return {k: sanitize_json(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [sanitize_json(v) for v in obj]
    return obj


def run_case(path):
    case = load_case(path)

    results = {}
    for n in SCENARIO_ORDER:
        r = scenario_dcf(case, n)
        if r is None:
            raise CaseError(f"scenarios.{n}: wacc <= terminal_growth，Gordon 终值无定义")
        results[n] = r

    bl = blend(case)
    blended = bl["blended_scenario_values"]
    rev = reverse_dcf(case)
    grid = sensitivity_grid(case)
    wgrid = wacc_sensitivity_blended(case)
    pos = position_metrics(case, blended)
    epv = epv_value(case)
    rel = relative_value(case)
    robust = robustness_check(case, blended)

    report = render_report(case, results, bl, rev, grid, wgrid, pos, epv, rel, robust)
    print(report)

    out_path = os.path.join(
        os.path.dirname(os.path.abspath(path)),
        os.path.splitext(os.path.basename(path))[0] + "_output.json")
    out = sanitize_json(build_output_json(case, results, bl, rev, grid, wgrid,
                                          pos, epv, rel, robust))
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2, allow_nan=False)
    print(f"结构化结果已写入: {out_path}")


def main(argv):
    if len(argv) != 2 or argv[1] in ("-h", "--help"):
        print(__doc__.split("\n\n")[0])
        print("用法: python3 dcf.py case.json | python3 dcf.py --example")
        return 0 if (len(argv) == 2) else 1
    if argv[1] == "--example":
        print(json.dumps(EXAMPLE_CASE, ensure_ascii=False, indent=2))
        return 0
    try:
        run_case(argv[1])
        return 0
    except CaseError as e:
        print(f"[输入错误] {e}", file=sys.stderr)
        return 1
    except OSError as e:
        print(f"[文件错误] {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
