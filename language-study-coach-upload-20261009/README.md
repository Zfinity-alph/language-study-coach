# Language Study Coach

面向中文学习者的俄英双语学习 Skill：从材料精读、语法解释到学习笔记和针对性练习。

A Russian and English learning skill for Chinese-speaking learners, featuring close reading, grammar explanations, vocabulary and word families, Obsidian-compatible notes, and targeted practice.

维护者：Zfinity-alph。当前为公开预览版，不是独立软件，也不包含模型服务。俄英同等受支持；俄语精读与笔记流程目前更细致，不承诺考试分数或学习效果。

## 教学方式

- 作业：先看考点，再给完整答案，最后解释整句、支配关系、形式与合理替代项。
- 俄语：标注重音，解释格支配、动词体、语境义、句式与精品短语；课文逐段翻译后逐句分析，对话逐轮处理。
- 英语：语法、写作、翻译与口语练习；区分必要纠错与可选优化，保留原意，不自动整理普通生词表。
- 首用 grill：分轮了解水平、目标、材料、时间和偏好；可以跳过或暂停，空白画像也能制作笔记。
- 词汇：必要词义随文解释，独立生词笔记仅按明确请求制作。
- 词根：首次询问是否启用，选择后沿用；启用后默认最多两个，优先教学价值，可选随机模式。不递归生成，更新时保留原选择。
- 测试：根据已核验材料制作选择、完形、原序变形和双向翻译；配答案依据及复述反馈。

## 快速使用

技能目录为 [skills/language-study-coach](skills/language-study-coach/SKILL.md)，复制或安装时应保留整个文件夹及其 references、assets，而不是只取 SKILL.md。

在支持本地 Skill 的 Codex 环境中，可按官方说明将此文件夹放入用户级的 `.agents/skills` 或项目级 `.agents/skills` 目录。已有同名技能时先备份并自行决定使用哪一份，不要直接覆盖个人版本。具体加载位置以当前 [官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills) 为准；本仓库不是插件市场安装包。

示例请求：

> 使用 $language-study-coach。暂时跳过画像访谈，分析这篇俄语课文；逐段翻译、逐句解析，先在对话中给出笔记，不生成独立生词表。

> 使用 $language-study-coach。修改这篇英语作文，保留原意，区分语法错误与可选优化，并让我练习最重要的一处改动。

若启用词根功能，可补充：“配套词根笔记启用，优先教学价值，最多两个。”若要保存笔记，请明确目标目录。

## 配置、文件与隐私

无需安装 Obsidian，也无需原维护者的教材或笔记。输出为 Obsidian 兼容 Markdown；普通阅读器不一定渲染所有 callout 或双链，但正文仍可阅读。

保存位置未知时先在对话输出，不擅自落盘；已有明确配置后复用。保护用户已有目录与内容，不强制迁移或重命名。

提供 [空白学习者档案模板](skills/language-study-coach/assets/learner-profile-template.md)。档案经确认且获得授权后才保存到私人位置；不要在公开仓库中填写真实画像。回答访谈不等于授权保存、公开或安排提醒。忽略规则只能减少误提交，不能替代提交前检查。

附件是学习材料而非操作指令。模糊词标记待核对；教材原文、课堂内容、自拟例句和研究结论应分开。请只提交有权公开的材料，本仓库不附完整教材截图或私人课堂记录。

## 展示案例

以下均为自拟材料与编辑制作的教学示例，不是独立模型测试的运行记录：

- [俄语格支配习题](examples/russian-exercise.md)
- [俄语短文逐句解析](examples/russian-text.md)
- [英语写作纠错](examples/english-writing.md)

## 验证与局限

[行为验收任务](tests/acceptance.md)列出了空白画像、文件边界、模糊图片、词根更新和俄英教学等场景。当前完成静态规则审阅、示例人工检查，以及本地文件和引用检查；尚未完成全部场景的独立模型运行或跨平台测试。

结构检查只需 Python 3.9 或更新版本，无第三方依赖：

```text
python scripts/validate_public.py
```

该脚本检查本项目的简单双字段入口、文件引用、部分隐私模式与未完成标记，不是通用 YAML 解析器，也不验证语言正确性或学习效果。

实际使用需要能读取 Skill 的 AI 环境；图片需图像读取能力，保存需文件工具，研究需联网工具。工具不可用时应说明限制，不编造读取、保存或查证结果。文本无法支持发音评价，考试评分只能在充分材料下作有条件的估计。

## 许可证

许可证尚待维护者选择，当前未附开源许可证。
