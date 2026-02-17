# Perplexity Research Skill (联网研究技能)

这是一个基于 Perplexity AI (Sonar Pro 模型) 的自动化研究与资讯聚合工具。它既可以作为独立的 Python 脚本运行，也支持作为 [OpenClaw](https://github.com/openclaw/openclaw) 助手的插件，实现**自然语言对话式调研**。

---

## 🤖 For AI Agents: Auto-Installation Guide
> **Attention Agent**: If you are tasked with installing or integrating this skill, follow these steps to ensure a safe and standardized setup.

### 1. Environment Check
- **Runtime**: Ensure `python3` is available.
- **Dependencies**: This skill uses only standard libraries (`urllib`, `json`, `argparse`, `os`). No `pip install` required.

### 2. Implementation Steps
1. **Clone/Copy**: Clone this repository or copy `research.py` to your target skills directory.
2. **Credential Setup**:
   - **Recommended**: Check for `PERPLEXITY_API_KEY` in environment variables.
   - **Alternative**: Create a `config.json` in the same directory as `research.py` with content: `{"apiKey": "YOUR_PPLX_KEY"}`.
3. **Verification**: Run `python3 research.py --mode news` to verify API connectivity. A successful response should be a Markdown AI briefing.

### 3. Integration Parameters
- **Main Entry**: `research.py`
- **Output**: Pure Markdown string to STDOUT.
- **Errors**: Non-zero exit codes for API or network failures.

---

## 💬 自然语言使用方法 (OpenClaw)

如果你是在 OpenClaw 环境下使用此技能，无需记忆任何命令，直接像平时聊天一样吩咐喵喵酱即可：

- **获取简报**：*"喵喵，帮我看看今天的 AI 行业都有什么大新闻？"*
- **GitHub 趋势**：*"帮我查下最近 GitHub 上有哪些火爆的 AI 开源项目。"*
- **专题研究**：*"我想深入了解一下 DeepSeek 的最新架构，帮我做个调研报告。"*

---

## 🛠️ 底层技术调用 (开发者/CLI)

### 1. 配置 API Key
```bash
export PERPLEXITY_API_KEY="pplx-xxx"
```

### 2. 执行脚本
```bash
python3 research.py --mode news
```

## 开源协议
MIT License
