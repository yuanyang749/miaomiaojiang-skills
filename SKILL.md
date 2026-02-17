---
name: miaomiaojiang-perplexity-research
description: Use the Perplexity API (Sonar Pro) to conduct deep research, find GitHub trends, or generate news briefs.
---

# miaomiaojiang-perplexity-research Skill

Use the Perplexity API (Sonar Pro) to conduct deep research, find GitHub trends, or generate news briefs.

## Usage

### CLI
```bash
python3 /root/.openclaw/workspace/skills/miaomiaojiang-perplexity-research/research.py --mode <news|github|research> [--topic "your topic"] [--out path/to/file.md] [--recency day|week|month]
```

### Modes
- **news**: Generates "AI Daily Brief". Ignores `--topic`.
- **github**: Generates "GitHub AI Trends". Ignores `--topic`.
- **research**: Generates a deep research report on `--topic`.

### Examples
1. **Research a topic**:
   `python3 .../research.py --mode research --topic "DeepSeek architecture analysis" --recency month`

2. **Daily GitHub Trends**:
   `python3 .../research.py --mode github --recency day`
