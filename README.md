
# 🚀 TrendPrompt Engine

**Trend-Hunter + Prompt-Writer:** Generates AI image prompts based on real market trends.

TrendPrompt Engine is a dual-engine tool designed for content creators, designers, and Print-on-Demand sellers:

1. **🦅 Trend-Hunter** — Searches Google Trends, Amazon, Etsy, and social media (X/TikTok/Pinterest) for what's trending in a specific niche.
2. **✍️ Prompt-Writer** — Converts those trends into 8-10 original prompts ready to paste into Midjourney, DALL-E, or Stable Diffusion.

### 📦 Unique Output Format
Instead of just giving raw data, the engine structures the output so you can act immediately. For every trend, it generates:
*   **Trend Title:** e.g., *Vintage Retro Mushroom Lamp*
*   **Suggested Product:** e.g., *3D Desk Lamp / Laptop Sticker*
*   **Ready-to-use Prompt:** Inside a code block to copy to your clipboard with a single click.
*   **Verified Sources:** Direct references of where the trend was found so you can validate the market yourself.

---

## ⚡ Quick Start

### Prerequisites
- Python 3.11+
- An OpenAI API key

### Setup

```bash
# Clone the repository
git clone <repository-url>
cd trend-prompt-gen

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

# Configure environment variables
cp .env.example .env
# Edit .env with your API keys
```

## 🛠️ Development Commands

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=src --cov-report=term-missing

# Linting
ruff check .

# Formatting
ruff format .

# Type checking
mypy src/
```

## 🌐 Deploy to Vercel

```bash
# Install Vercel CLI (if not installed)
npm i -g vercel

# Deploy to preview
vercel deploy

# Deploy to production
vercel --prod
```
*(Remember to set your environment variables in the Vercel Dashboard: Settings → Environment Variables).*

---

## 📂 Project Structure

See `AGENTS.md` for the complete directory structure, code conventions, and development workflow.

## 🛠️ Tech Stack

- **Python 3.11+** with FastAPI
- **OpenAI SDK** for prompt generation (gpt-4o-mini)
- **BeautifulSoup4 + Selenium** for web scraping (off-chain)
- **Pydantic v2** for data validation
- **Vercel** for serverless deploy
- **ruff** for linting/formatting, **mypy** for type checking

## 📚 Documentation

- `AGENTS.md` — System prompt and development rules
- `spec/constitution/` — Project mission, tech stack, and roadmap
- `spec/features/` — Per-feature specifications (SDD)
