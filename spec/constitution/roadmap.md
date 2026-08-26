# Roadmap — TrendPrompt Engine

## Feature Backlog

Each feature follows the SDD cycle: `spec → plan → tasks → implement → verify`.

| ID    | Feature                                | Status       | Priority | Dependencies |
| ----- | -------------------------------------- | ------------ | -------- | ------------ |
| 001   | Project Setup                          | [PLANNING]   | High     | —            |
| 002   | Vercel Configuration + vercel.json     | [PLANNING]   | High     | 001          |
| 003   | Google Trends Scraper                  | [PLANNING]   | High     | 001          |
| 004   | Amazon Best Sellers Scraper            | [PLANNING]   | High     | 001          |
| 005   | Etsy Trending Scraper                  | [PLANNING]   | Medium   | 001          |
| 006   | Social Media Scraper (X/TikTok/Pinterest) | [PLANNING] | Medium | 001          |
| 007   | Scraper Worker (off-chain runner)      | [PLANNING]   | High     | 003,004,005,006 |
| 008   | LLM Integration for Prompt-Writer      | [PLANNING]   | High     | 001          |
| 009   | Output Format (Markdown Report)        | [PLANNING]   | High     | 008          |
| 010   | Trend-Hunter Orchestrator              | [PLANNING]   | High     | 007,008      |
| 011   | REST API (FastAPI on Vercel)           | [PLANNING]   | High     | 010,009,002  |
| 012   | E2E Tests and Validation               | [PLANNING]   | High     | 011          |

## Feature Details

### 001 — Project Setup
- **Objective:** Functional dev environment with folder structure, dependencies, linters, and base tests.
- **Expected outcome:** `pytest` passes, `ruff check` clean, `mypy` no errors.
- **Current status:** [PLANNING]

### 002 — Vercel Configuration + vercel.json
- **Objective:** Configure the project for Vercel deploy as serverless functions.
- **Dependencies:** 001
- **Expected outcome:**
  - `vercel.json` file with Python runtime config, maxDuration, and routes.
  - `api/index.py` entrypoint exposing the FastAPI app.
  - Environment variables configured in Vercel Dashboard (not .env for production).
  - Deploy script: `vercel deploy` / `vercel --prod`.
- **Note:** Frontend (React/Next.js) is optional. The API can be consumed directly.
- **Current status:** [PLANNING]

### 003 — Google Trends Scraper
- **Objective:** Fetch rising terms, related queries, and interest by region for a given niche.
- **Dependencies:** 001
- **Expected outcome:** Function that takes a string (niche) and returns a Pydantic model with Google Trends data.
- **Current status:** [PLANNING]

### 004 — Amazon Best Sellers Scraper
- **Objective:** Extract best sellers and movers & shakers from an Amazon category.
- **Dependencies:** 001
- **Expected outcome:** Function returning a list of trending products with title, price, rating, and URL.
- **Current status:** [PLANNING]

### 005 — Etsy Trending Scraper
- **Objective:** Identify trends on Etsy (trending searches, popular items) for a niche.
- **Dependencies:** 001
- **Expected outcome:** Function with normalized Etsy trend output.
- **Current status:** [PLANNING]

### 006 — Social Media Scraper (X/TikTok/Pinterest)
- **Objective:** Detect viral hashtags and trending content on social media for the niche.
- **Dependencies:** 001
- **Expected outcome:** Function consolidating data from all three platforms.
- **Current status:** [PLANNING]

### 007 — Scraper Worker (off-chain runner)
- **Objective:** Run scrapers off-chain (outside Vercel) and store results in cache/DB.
- **Dependencies:** 003, 004, 005, 006
- **Expected outcome:**
  - Executable script: `python -m src.scrapers.worker --niche "plant moms"`.
  - Stores results in local SQLite (dev) or Upstash Redis (production).
  - Can run as: Vercel Cron Job (every N hours), system cron, or external service (Inngest, Trigger.dev).
  - The API queries the cache instead of scraping in real-time.
- **Reason:** Selenium/Playwright require browser binaries that Vercel doesn't support. Heavy scraping must run off-chain.
- **Current status:** [PLANNING]

### 008 — LLM Integration for Prompt-Writer
- **Objective:** Convert trends into original image prompts using OpenAI GPT-4o-mini.
- **Dependencies:** 001
- **Expected outcome:** Function that receives trends and returns structured prompts.
- **Current status:** [PLANNING]

### 009 — Output Format (Markdown Report)
- **Objective:** Generate markdown report with trends, copyable prompts, and verifiable sources.
- **Dependencies:** 008
- **Expected outcome:** Markdown string generator with exact format specified in mission.md.
- **Current status:** [PLANNING]

### 010 — Trend-Hunter Orchestrator
- **Objective:** Coordinate scraper cache reads, deduplicate trends, and send them to the Prompt-Writer.
- **Dependencies:** 007, 008
- **Expected outcome:** Function `run_trend_hunt(niche: str) -> Report` that:
  1. Reads trends from cache (populated by the off-chain worker).
  2. Deduplicates and ranks by relevance.
  3. Sends to Prompt-Writer.
  4. Returns complete report.
- **Current status:** [PLANNING]

### 011 — REST API (FastAPI on Vercel)
- **Objective:** Expose HTTP endpoints on Vercel serverless to generate reports and query history.
- **Dependencies:** 010, 009, 002
- **Expected endpoints:**
  - `POST /api/v1/report` — Generate complete report for a niche (reads from cache + LLM).
  - `GET /api/v1/report/{id}` — Retrieve generated report.
  - `GET /api/v1/trends/{niche}` — Query cached trends for a niche.
- **Vercel config:**
  - Entrypoint: `api/index.py` with `app = FastAPI()`.
  - `maxDuration`: 60s (hobby) or 300s (pro) — enough for OpenAI calls.
  - Environment variables in Vercel Dashboard (OPENAI_API_KEY, etc.).
- **Current status:** [PLANNING]

### 012 — E2E Tests and Validation
- **Objective:** Validate the full niche → report flow with real prompts.
- **Dependencies:** 011
- **Expected outcome:** E2E suite that runs the full flow and validates output structure.
- **Current status:** [PLANNING]

## Progress

```
Completed:  0/12 features
In progress: 0/12 features
Pending:    12/12 features
```

## Update Rules

1. A feature only moves to `[IN_PROGRESS]` when implementation begins.
2. A feature moves to `[DONE]` only when: code written + tests pass + ruff/mypy clean + spec updated.
3. If a feature requires design changes, update its `spec.md` first, then continue.
4. The roadmap is updated after each feature completion.
