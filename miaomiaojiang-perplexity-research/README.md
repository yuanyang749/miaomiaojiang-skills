# Perplexity Research Skill (联网研究技能)

这是一个基于 Perplexity AI (Sonar Pro 模型) 的自动化研究与资讯聚合工具。

## 功能特性

- **AI 每日简报 (`--mode news`)**：获取过去 24-48 小时全球最核心的 AI 动态，包含标题、摘要及来源链接。
- **GitHub 趋势分析 (`--mode github`)**：发现过去 24 小时内最热门的开源 AI 项目。
- **深度专题研究 (`--mode research`)**：针对特定主题生成结构化的深度研究报告。
- **纯净依赖**：仅使用 Python 原生库，无需 `pip install`。

## 安装与配置

1. **环境要求**：Python 3.6+
2. **获取 API Key**：从 [Perplexity AI](https://www.perplexity.ai/settings/api) 获取。
3. **配置凭据**：
   - 方式 A (推荐)：设置环境变量 `export PERPLEXITY_API_KEY="pplx-xxx"`。
   - 方式 B：在当前目录下创建 `config.json`，内容如下：
     ```json
     { "apiKey": "pplx-xxx" }
     ```

## 使用方法

### 获取 AI 每日新闻
```bash
python3 research.py --mode news
```

### 获取 GitHub 趋势
```bash
python3 research.py --mode github
```

### 指定主题研究
```bash
python3 research.py --mode research --topic "大模型长文本技术的现状"
```

## 开源协议
MIT License
