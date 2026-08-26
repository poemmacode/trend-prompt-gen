# Tech Stack — TrendPrompt Engine

## Development Environment

| Component         | Version / Detail                                              |
| ------------------ | ----------------------------------------------------------- |
| Python             | 3.11+ (recommended: 3.12)                                   |
| Package manager    | pip 23+ with virtualenv (alternative: poetry 1.7+)          |
| Development OS     | macOS / Linux (Windows compatible with WSL2)                 |
| Editor             | VS Code with extensions: Python, Ruff, MyPy, Pylance        |
| Deploy platform    | Vercel (serverless functions)                                |

## Deploy Architecture

```
┌─────────────────┐     ┌─────────────────────────────────┐
│   Frontend      │────▶│  Vercel Serverless Functions     │
│   (React/Next)  │     │  FastAPI (api/index.py)          │
│   [OPTIONAL]    │     │  Prompt-Writer (OpenAI calls)    │
└─────────────────┘     └──────────────┬──────────────────┘
                                       │
                          ┌────────────┴────────────────┐
                          ▼                              ▼
                 ┌─────────────────┐         ┌──────────────────────┐
                 │   OpenAI API    │         │  Scraper Worker       │
                 │   (gpt-4o-mini) │         │  (Off-chain: cron or  │
                 └─────────────────┘         │   separate VPS)       │
                                             └──────────────────────┘
```

### Responsibility Separation

| Component           | Runs on             | Reason                                                |
| ------------------- | ------------------- | ----------------------------------------------------- |
| REST API (FastAPI)  | Vercel serverless   | Lightweight I/O, fast responses                       |
| Prompt-Writer       | Vercel serverless   | Just an HTTP call to OpenAI, no Selenium needed       |
| Scraping (Google Trends, Amazon, etc.) | External worker / Vercel Cron | Requires Selenium/Playwright, heavy binaries, long timeouts |
| Orchestrator        | Vercel serverless   | Coordinates calls, delegates scraping to worker       |

### Vercel Serverless Limitations

- **Max duration:** 60s (hobby), 900s (pro) per request.
- **Max body size:** 4.5 MB.
- **Not supported:** Browser binaries (Selenium/Playwright), persistent processes, files > 50MB.
- **Cold start:** ~200-500ms for Python.
- **Scraping:** Must run off-chain and feed a cache/DB that the API queries.

## Core Dependencies

| Package             | Version | Use                                        |
| ------------------- | ------- | ------------------------------------------ |
| fastapi             | ≥0.110  | REST HTTP Framework                        |
| uvicorn[standard]   | ≥0.29   | ASGI server (dev and production)           |
| pydantic            | ≥2.6    | Data models and validation                 |
| pydantic-settings   | ≥2.2    | Configuration and .env management          |
| httpx               | ≥0.27   | Async HTTP client (for requests)           |
| python-dotenv       | ≥1.0    | Environment variable loading               |

## Scraping Dependencies

| Package          | Version | Use                                          |
| ---------------- | ------- | -------------------------------------------- |
| beautifulsoup4   | ≥4.12   | Static HTML parsing                          |
| lxml             | ≥5.1    | Fast HTML/XML parser (BS4 backend)           |
| selenium         | ≥4.18   | Headless navigation for dynamic content      |
| webdriver-manager| ≥4.0    | Automatic chromedriver management            |

## LLM Integration

| Package   | Version | Use                                            |
| --------- | ------- | ---------------------------------------------- |
| openai    | ≥1.14   | Official SDK for GPT-4o-mini (prompt generation)|

## Testing Dependencies

| Package          | Version | Use                                            |
| ---------------- | ------- | ---------------------------------------------- |
| pytest           | ≥8.1    | Test framework                                 |
| pytest-asyncio   | ≥0.23   | Async tests                                    |
| pytest-cov       | ≥5.0    | Code coverage                                  |
| httpx            | ≥0.27   | FastAPI endpoint testing                       |
| respx            | ≥0.21   | HTTP request mocking in tests                  |

## Linting / Formatting / Type Checking

| Package | Version | Use                                                      |
| ------- | ------- | -------------------------------------------------------- |
| ruff    | ≥0.4    | Linting + formatting (replaces black, isort, flake8)     |
| mypy    | ≥1.9    | Static type checking                                     |

## Development Commands

```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

# Linting
ruff check .

# Formatting
ruff format .

# Type checking
mypy src/

# All tests
pytest

# Tests with coverage
pytest --cov=src --cov-report=term-missing

# Unit tests only
pytest tests/unit/ -v

# Integration tests only
pytest tests/integration/ -v
```

## Ruff Configuration

Configured in `pyproject.toml`:

```toml
[tool.ruff]
target-version = "py311"
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I", "N", "UP", "B", "A", "C4", "SIM", "TCH"]
ignore = ["E501"]  # Handled by formatter

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

## MyPy Configuration

```toml
[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

## External API Management

### General Rules
1. **Never hardcode API keys.** Use pydantic-settings to read from `.env`.
2. **Rate limiting:** All external API calls must go through `src/utils/rate_limiter.py`.
3. **Retry with backoff:** Use exponential backoff (max 3 retries) for errors 429/500/502/503.
4. **Timeout:** Maximum 30-second timeout per HTTP request.
5. **Logging:** Log failed requests at WARNING level, successful ones at DEBUG level.

### Specific APIs
| API                | Auth Method         | Rate Limit (free tier) | Notes                                    |
| ------------------ | ------------------- | ---------------------- | ---------------------------------------- |
| Google Trends      | N/A (scraping)      | ~10 req/min            | Use selenium to avoid blocks             |
| Amazon Product API | API Key (PA-API)    | 1 request/second       | Requires Amazon Associates registration  |
| Etsy Open API      | API Key             | [INSERT_HERE]          | Verify current limits                    |
| OpenAI API         | Bearer token        | Variable by model      | Use gpt-4o-mini for cost/performance     |
| Twitter/X API      | Bearer token        | [INSERT_HERE]          | Free tier: 1500 tweets/month             |

### Required Environment Variables

```env
# .env (NEVER commit this file)
OPENAI_API_KEY=sk-...
ETSY_API_KEY=[INSERT_HERE]
TWITTER_BEARER_TOKEN=[INSERT_HERE]
AMAZON_ACCESS_KEY=[INSERT_HERE]
AMAZON_SECRET_KEY=[INSERT_HERE]
AMAZON_PARTNER_TAG=[INSERT_HERE]
```

## Pytest Configuration

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
markers = [
    "unit: Unit tests (no external calls)",
    "integration: Integration tests (may use external APIs)",
    "e2e: End-to-end tests (full flow)",
    "slow: Tests that take > 5s",
]
```
