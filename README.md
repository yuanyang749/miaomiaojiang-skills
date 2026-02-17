# Miaomiaojiang Perplexity Research Skill

An AI-powered research and news aggregation tool using Perplexity AI's Sonar models. Originally designed as a skill for [OpenClaw](https://github.com/openclaw/openclaw), now available as a standalone CLI tool.

## Features

- **Daily AI News**: Generates high-quality AI news briefings with sources.
- **GitHub Trends**: Identifies trending AI/LLM open-source projects.
- **Deep Research**: Conducts structured deep-dives on any topic.
- **Markdown Output**: Strictly formatted for readability and integration.

## Installation

```bash
# Clone the repository
git clone https://github.com/yuanyang749/miaomiaojiang-skills.git
cd miaomiaojiang-skills

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate
```

This tool uses only Python standard libraries (`urllib`, `json`, `argparse`), so no extra `pip install` is required!

## Configuration

Set your Perplexity API Key in your environment:

```bash
export PERPLEXITY_API_KEY="your-api-key-here"
```

Alternatively, create a `config.json` in the same directory:

```json
{
  "apiKey": "your-api-key-here"
}
```

## Usage

### 1. AI Daily News
```bash
python3 research.py --mode news
```

### 2. GitHub Trends
```bash
python3 research.py --mode github
```

### 3. Deep Research
```bash
python3 research.py --mode research --topic "What are AI Agents?"
```

## License

MIT License
