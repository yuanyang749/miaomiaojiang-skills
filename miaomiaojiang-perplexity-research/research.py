#!/usr/bin/env python3
import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# Configuration
# For open source: Prefer environment variables or a local config.json
DEFAULT_CONFIG_PATH = Path("config.json")
API_URL = "https://api.perplexity.ai/chat/completions"

def load_key() -> str:
    """Load API key from env or local config file."""
    # 1. Check environment variable
    env_key = os.getenv("PERPLEXITY_API_KEY", "").strip()
    if env_key:
        return env_key
    
    # 2. Check local config.json in current directory
    if DEFAULT_CONFIG_PATH.exists():
        try:
            cfg = json.loads(DEFAULT_CONFIG_PATH.read_text(encoding="utf-8"))
            return cfg.get("apiKey", "").strip()
        except Exception:
            pass
            
    # 3. Fallback check for OpenClaw specific path (Optional/Internal)
    oc_config = Path("/root/.openclaw/workspace/config/perplexity-key.json")
    if oc_config.exists():
        try:
            cfg = json.loads(oc_config.read_text(encoding="utf-8"))
            return cfg.get("apiKey", "").strip()
        except Exception:
            pass
            
    return ""

def generate_report(api_key: str, topic: str, mode: str, model: str = "sonar-pro", recency: str = "month") -> str:
    """
    Generate a report using Perplexity API based on mode.
    Modes: 'news', 'github', 'research'
    """
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    system_prompt = (
        "You are an expert AI analyst and researcher. "
        "Your goal is to provide high-quality, dense, and actionable information. "
        "Always cite sources. "
        "Output strictly in Markdown."
    )

    if mode == "news":
        user_prompt = (
            f"Generate a daily AI news briefing for {today} (Asia/Shanghai time). \n"
            "Requirements:\n"
            "1. Identify the top 5-7 most important AI news stories from the last 24-48 hours.\n"
            "2. For each story, provide:\n"
            "   - A clear, engaging title.\n"
            "   - A 1-sentence summary of the key point.\n"
            "   - The source name and URL.\n"
            "3. Add a 'Brief Comment' section at the end (2 sentences max) analyzing the trend.\n"
            "4. Output strictly in Markdown format:\n\n"
            "**# AI Daily Brief｜{today}（CST）**\n\n"
            "**## Core Dynamics**\n"
            "1. **[Title]**\n"
            "   - Key Point: [Summary]\n"
            "   - Source: [URL]\n\n"
            "**## Brief Comment**\n"
            "[Analysis]\n\n"
            "Language: Simplified Chinese (简体中文). CRITICAL: Do NOT output English summaries."
        )
    elif mode == "github":
        user_prompt = (
            f"Find the top 3-5 trending AI/LLM open-source projects on GitHub, Hacker News, or Reddit in the last 24 hours (Date: {today}).\n"
            "Focus on practical tools, agents, frameworks, or significant model releases.\n"
            "Ignore simple wrappers, curations, or tutorials unless they are groundbreaking.\n\n"
            "Output Format (Markdown, Simplified Chinese):\n"
            "**# GitHub AI Trends ｜ {today}**\n\n"
            "**1. [Project Name]**\n"
            "   - **One-Liner**: [What it does]\n"
            "   - **Why Trending**: [Reason/Features]\n"
            "   - **Tech Stack**: [Languages/Frameworks]\n"
            "   - **Link**: [URL]\n\n"
            "**## Trend Analysis**\n"
            "[Brief insight on what developers are focusing on today]\n"
            "Language: Simplified Chinese (简体中文). CRITICAL: Do NOT output English summaries."
        )
    elif mode == "research":
        user_prompt = (
            f"Conduct a deep research report on: '{topic}'.\n"
            "Requirements:\n"
            "1. **Definition**: What is it? (Clear, concise)\n"
            "2. **Key Features/Mechanism**: How does it work?\n"
            "3. **Pros & Cons**: Critical analysis.\n"
            "4. **Use Cases/Examples**: Real-world application.\n"
            "5. **Competitors/Alternatives**: Brief comparison.\n"
            "6. **Conclusion**: Your verdict.\n\n"
            "Language: Simplified Chinese (简体中文).\n"
            "Style: Professional, structured, objective."
        )
    else:
        # Generic query fallback
        user_prompt = topic

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        # Some API versions accept search_recency_filter at top level
        # If it fails, it might just ignore it, which is fine for generic research
        "search_recency_filter": recency 
    }

    req = Request(API_URL, method="POST")
    req.add_header("Authorization", f"Bearer {api_key}")
    req.add_header("Content-Type", "application/json")
    
    data = json.dumps(payload).encode("utf-8")
    
    try:
        with urlopen(req, data=data, timeout=90) as resp:
            raw_response = json.loads(resp.read().decode("utf-8"))
            return raw_response["choices"][0]["message"]["content"]
    except HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"API Error {e.code}: {error_body}")
    except Exception as e:
        raise RuntimeError(f"Request Failed: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Miao Perplexity Research Tool")
    parser.add_argument("--mode", choices=["news", "github", "research"], required=True, help="Operation mode")
    parser.add_argument("--topic", help="Topic for research mode (ignored for news/github)")
    parser.add_argument("--out", help="Output file path (optional)")
    parser.add_argument("--model", default="sonar-pro", help="Perplexity model")
    parser.add_argument("--recency", default="month", help="Search recency (day, week, month)")
    
    args = parser.parse_args()
    
    key = load_key()
    if not key:
        print("Error: No API key found in config/perplexity-key.json or env PERPLEXITY_API_KEY.")
        sys.exit(1)
        
    try:
        # Default recency for news/github should be stricter if not specified
        if args.mode in ["news", "github"] and args.recency == "month":
            real_recency = "day" # Default to day for daily tasks
        else:
            real_recency = args.recency

        print(f"Running mode='{args.mode}' topic='{args.topic}' recency='{real_recency}'...")
        content = generate_report(key, args.topic, args.mode, args.model, real_recency)
        
        if args.out:
            out_path = Path(args.out)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content, encoding="utf-8")
            print(f"Saved report to {args.out}")
        else:
            print(content)
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(2)

if __name__ == "__main__":
    main()
