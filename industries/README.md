# industries/ — 行业附录（20 个，待补齐）

## 这个目录是什么

每个文件是一个行业的研究附录，提供该行业的：**KPI 字典、价值驱动树、财务模型结构、估值方法、财报模式重点、护城河判断清单**。

管线第 2 步（行业路由）按 `references/industry-routing.md` 把目标公司映射到 1 个主行业附录 + 最多 2 个分部附录。**行业附录里的 KPI 与估值口径优先于通用模板中与之冲突的部分。**

## 当前状态：待补齐

首次提交时，这 20 个文件因原始工作目录的 Google Drive 同步权限问题（目录返回 `EPERM`）未能打包进来。**缺了它们，管线第 2 步会退化为通用模板**——报告仍能产出，但会丢掉行业特定的 KPI 与估值锚。

应有的 20 个文件（文件名即路由表中的引用名）：

```
autos-ev.md            banks.md               capital-markets.md     consumer.md
energy.md              hardware.md            healthcare-services.md industrials.md
insurance.md           internet-platform.md   media-gaming.md        metals-mining.md
payments-fintech.md    pharma.md              reits.md               saas.md
semiconductors.md      telecom.md             transport.md           utilities.md
```

## 补齐方法

在原始工作目录能被正常读取后（在 Finder 里打开该文件夹、或右键设为"可离线使用"，让 Google Drive 把文件物化到本地），运行：

```bash
SRC="/path/to/Secondary market research agent"
cp "$SRC"/industries/*.md industries/
git add industries/ && git commit -m "Add 20 industry appendices"
```

补齐后请删除本文件。
