## 评估结果的统计显著性

评估集有限，模型输出又有随机性，因此分数差异可能只是抽样噪声。若在 $n$ 个用例上测得成功率 $p$，标准误可粗略估计为：

$$
\mathrm{SE}(p)\approx\sqrt{\frac{p(1-p)}{n}}
$$

例如 100 个用例、成功率 70% 时，95% 置信区间约为 $70\%\pm9$ 个百分点；“新模型 73% 对旧模型 70%”不足以支持切换。

同一批任务比较两个配置时，应优先做**配对分析**：逐题记录谁胜出，用 McNemar 检验或配对 bootstrap 判断差异，而不是直接相减两个独立成功率。由于 Agent 每次运行也可能不同，每个配置最好用多个随机种子（如 3–5 次），报告均值和波动范围；单次运行只能用来筛选方向。若预期收益只有 2–3 个百分点，而评估集只有几十题，应该先扩大样本，标准误会按 $1/\sqrt{n}$ 缩小。

```python
for task in paired_tasks:
    for seed in fixed_seeds:
        a = run(config_a, task, seed)
        b = run(config_b, task, seed)
        record_paired_delta(verifier(a), verifier(b))

return paired_bootstrap_or_mcnemar(all_deltas)
```

配对的含义是让两组共享任务与随机条件，而不是分别抽两批样本再比较平均值。

并行验证多个假设时还要考虑**多重比较**：收紧显著性阈值，或对正向结果做独立复跑。实务上的判断标准很简单：分差要超过噪声、在配对分析中成立，并且能够复现，才值得据此切换模型或发布改动。
