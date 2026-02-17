# Perplexity Research Skill (联网研究技能)

这是一个基于 Perplexity AI (Sonar Pro 模型) 的自动化研究与资讯聚合工具。它既可以作为独立的 Python 脚本运行，也支持作为 [OpenClaw](https://github.com/openclaw/openclaw) 助手的插件，实现**自然语言对话式调研**。

## 💬 自然语言使用方法 (OpenClaw)

如果你是在 OpenClaw 环境下使用此技能，无需记忆任何命令，直接像平时聊天一样吩咐喵喵酱即可：

- **获取简报**：*"喵喵，帮我看看今天的 AI 行业都有什么大新闻？"*
- **GitHub 趋势**：*"帮我查下最近 GitHub 上有哪些火爆的 AI 开源项目。"*
- **专题研究**：*"我想深入了解一下 DeepSeek 的最新架构，帮我做个调研报告。"*
- **特定日期/范围**：*"帮我搜下上周关于 Sora 视频生成的技术动态。"*

---

## 🛠️ 底层技术调用 (开发者/CLI)

如果你想在命令行或自己的脚本中直接调用：

### 1. 配置 API Key
设置环境变量：
```bash
export PERPLEXITY_API_KEY="pplx-xxx"
```

### 2. 执行脚本
```bash
# 获取 AI 每日新闻
python3 research.py --mode news

# 获取 GitHub 趋势
python3 research.py --mode github

# 指定主题研究
python3 research.py --mode research --topic "大模型长文本技术的现状"
```

## 📂 技能集成说明 (OpenClaw Integrators)

如果你是 OpenClaw 的开发者，可以参考目录下的 `SKILL.md` 进行集成。本技能通过 `research.py` 提供稳定的 Markdown 输出，非常适合作为 Agent 的研究工具。

## 开源协议
MIT License
