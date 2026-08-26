# workspace/ — 本地工作目录（不进版本库）

管线运行时的中间产物放这里，按标的分子目录：

```
workspace/<ticker>/<ticker>-dcf-<YYYYMMDD>.json          估值输入
workspace/<ticker>/<ticker>-dcf-<YYYYMMDD>_output.json    dcf.py 输出（脚本自动生成）
workspace/<ticker>/*.txt                                  一手申报节选、电话会转录等
```

命名带日期，便于下次覆盖更新时做"原值 → 新值"桥（见 `references/output-format.md` 第 5 节
预测可追踪性：更新报告要保留旧预测原值，只追加实际结果与误差归因）。

**本目录内容不提交到版本库**（见 `.gitignore`）。原因：估值 case 文件内嵌具体标的的情景假设、
概率与公允价值，等同于机器可读的投资结论；报告成稿同理，一律留在本地。

想看输入文件长什么样：

```bash
python3 scripts/dcf.py --example      # 带注释的完整输入模板
```
