### Computer Use 的世界模型

上一节的观察接口解决的是 “屏幕中间发生了什么”：通过关键帧、语音转写和持久文字，让 Agent 不再只看到两张相隔很久的截图。但观察接口并不会消除规划延迟，Agent 仍然是串行的“截图—思考—点击”循环，每执行一个动作都重新观察、思考下一步。**OSWorld-Human** 的效率研究显示，即使任务最终成功，Agent 的操作步骤仍明显多于人类，等待时间也更长；准确率达到人类水平，并不等于已经足够实用。

人类操作电脑时并不是点击之后才开始想下一步，而是会先对动作后果作出预测：如果实际变化与预期一致，就沿着原定计划继续执行；只有发现页面状态偏离预期，才停下来重新观察和规划。世界模型让 Agent 能够在行动前预测桌面接下来可能变成什么，从而实现这种类似于人类的 “推测执行” 机制，大大提高效率。

桌面状态不只是一张像素图，还包括窗口、焦点、滚动位置、输入框内容、加载状态、权限和网络返回；动作则包括点击、键盘输入、滚动、拖拽和等待。一个可用于 Computer Use 的世界模型至少要能编码当前状态、预测候选动作造成的状态变化，并把预测交给规划器决定下一步：

```text
桌面状态 + click/type/scroll/wait ──> 下一状态的表示
```

这样，Agent 就能在真正点击之前比较候选动作的后果，在页面加载期间准备下一步，并在弹窗一闪而过时根据状态差异恢复。例如任务是 “在 VS Code 新建 Python 文件并写入 hello world”，模型可以先预测文件树和编辑器在成功后的关键状态，再选择点击、输入和保存动作；如果任务是删除文件，则可以先在隔离的虚拟桌面中预测是否会出现不可逆确认框，必要时请求用户确认。这里的重点不是让模型生成一张逼真的未来截图，而是预测完成任务所需的、可检查的状态差异。

2026 年 7 月，Induction Labs 公布的 **Photon-1** 展示了这条路线的一种实现，仅用 3 万小时的 H200 GPU 时间就完成了 computer use 世界模型的预训练。它把每帧压缩为离散的潜在 token，自回归预测动作之后的下一状态表示，而不是在预训练阶段逐像素生成截图；另外接入的图像生成器只用于把潜在表示可视化，并非推理必需组件。给定一张种子截图和后续动作，模型可以连续“想象”桌面状态，再通过虚拟机上的在线训练学会输出 computer-use 动作。[^ch6-20]

[^ch6-20]: David Li and Jonathan Li, Induction Labs, “Scaling Video Pretraining with Imagination Models,” 2026-07-23. https://www.inductionlabs.com/news/scaling-video-pretraining 。文中 Photon-1 的参数、数据规模、内部 benchmark 和成本比较均为公司披露的结果。
[^ch6-21]: Jack Parker-Holder and Shlomi Fruchter, Google DeepMind, “Genie 3: A new frontier for world models,” 2025-08-05. https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/；Zachary Lin et al. *Cosmos World Foundation Model Platform for Physical AI.* arXiv:2501.03575, 2025. https://arxiv.org/abs/2501.03575 。
