# TrendPrompt Engine — System Prompt

## Project Identity

**TrendPrompt Engine** is a dual-engine tool that combines a Trend-Hunter (trend search engine for specific niches) with a Prompt-Writer (prompt generator for generative AI image tools). The system receives a user niche, analyzes current trends across multiple sources, and generates original prompts for Midjourney/DALL-E/Stable Diffusion.

## Tech Stack (Default)

- **Language:** Python 3.11+
- **HTTP Framework:** FastAPI (REST API)
- **Deploy:** Vercel (serverless functions)
- **Scraping:** BeautifulSoup4 (static HTML), Selenium (dynamic content) — runs off-chain
- **LLM Integration:** OpenAI SDK (gpt-4o-mini for prompt generation)
- **Data Validation:** Pydantic v2
- **Testing:** pytest + pytest-asyncio + httpx
- **Linting/Formatting:** ruff (unified linting + formatting)
- **Type Checking:** mypy
- **Package Management:** pip + virtualenv (alternative: poetry)
- **Config Management:** pydantic-settings + .env (dev) / Vercel Dashboard (production)
- **Cache (production):** Upstash Redis or local SQLite

## Code Conventions

- **Naming:** `snake_case` for variables, functions, modules. `PascalCase` for classes. `UPPER_SNAKE_CASE` for constants.
- **Imports:** Always absolute (`from src.trend_hunter.scrapers import google_trends`).
- **Type Hints:** Mandatory on all public functions and return types. Use `typing.Annotated` for validation.
- **Docstrings:** Google-style for public functions. Do not document obvious code.
- **Strings:** f-strings for interpolation. Do not use `.format()` or `%`.
- **Error Handling:** Custom exceptions inherited from `src.exceptions.base`. Never catch generic `Exception` without reason.
- **Async:** Prefer `async/await` on I/O functions (scraping, LLM calls).

## Directory Structure

```
trend-prompt-gen/
├── AGENTS.md                    # This file — persistent system prompt
├── README.md                    # Usage documentation
├── pyproject.toml               # Project config and dependencies
├── vercel.json                  # Vercel deploy configuration
├── .env.example                 # Environment variable template
├── .gitignore
├── api/
│   └── index.py                 # Vercel entrypoint: exposes FastAPI app (api/index.py)
├── src/
│   ├── __init__.py
│   ├── main.py                  # FastAPI app (imported by api/index.py)
│   ├── config.py                # Centralized settings (pydantic-settings)
│   ├── exceptions/
│   │   ├── __init__.py
│   │   └── base.py              # Custom project exceptions
│   ├── trend_hunter/
│   │   ├── __init__.py
│   │   ├── models.py            # Pydantic I/O models
│   │   ├── orchestrator.py      # Main Trend-Hunter coordinator
│   │   └── scrapers/
│   │       ├── __init__.py
│   │       ├── google_trends.py
│   │       ├── amazon.py
│   │       ├── etsy.py
│   │       ├── social.py
│   │       └── worker.py        # Off-chain runner (cron/VPS, NOT Vercel)
│   ├── prompt_writer/
│   │   ├── __init__.py
│   │   ├── engine.py            # Prompt generation engine
│   │   ├── templates.py         # Output format templates
│   │   └── formatter.py         # Markdown report formatter
│   └── utils/
│       ├── __init__.py
│       ├── http_client.py       # HTTP client with retry/backoff
│       └── rate_limiter.py      # Request rate control
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Shared fixtures
│   ├── unit/
│   │   ├── __init__.py
│   │   └── test_models.py
│   ├── integration/
│   │   ├── __init__.py
│   │   └── test_scrapers.py
│   └── e2e/
│       ├── __init__.py
│       └── test_full_flow.py
├── spec/                        # SDD specifications (DO NOT modify without updating spec)
│   ├── constitution/            # Global project rules
│   │   ├── mission.md
│   │   ├── tech-stack.md
│   │   └── roadmap.md
│   └── features/                # Per-feature specs
│       └── 001-setup-project/
│           ├── spec.md
│           ├── plan.md
│           └── tasks.md
└── scripts/                     # Utility scripts (dev, CI)
```

## Strict Prohibitions

1. **DO NOT use `pass` or `# TODO` as placeholder.** Every piece of code must have a real implementation or a `NotImplementedError` with a descriptive message.
2. **DO NOT install dependencies without explicit permission.** Any new library must be approved first and updated in `spec/constitution/tech-stack.md`.
3. **DO NOT hardcode API keys, tokens, or secrets.** All secrets are read from environment variables via `pydantic-settings`. If one is missing, an error must be raised at startup.
4. **DO NOT modify `spec/` without also updating the affected code.** If the design changes, update the spec first, then the code.
5. **DO NOT write code without first reading the corresponding spec in `/spec`.**
6. **DO NOT use print() for logging.** Use the standard `logging` module with centralized configuration.
7. **DO NOT skip tests.** All new code must include tests. Minimum coverage: 80% on unit tests.

## Workflow

1. **Before coding:** Read the corresponding `spec/features/XXX/spec.md` and `spec/features/XXX/plan.md`.
2. **When implementing:** Follow `plan.md` strictly. If a deviation arises, update the plan before continuing.
3. **When done:** Mark completed tasks in `tasks.md`. Update `spec/constitution/roadmap.md` if the status changed.
4. **If the design changes:** Update `spec/` first, then adjust the code to align.
5. **Before commit:** Run `ruff check . && mypy src/ && pytest` and fix any errors.

## Quality Gates

- [ ] ruff check passes without errors
- [ ] mypy src/ has no type errors
- [ ] pytest with 0 failures
- [ ] Unit test coverage ≥ 80%
- [ ] No `.env` files or hardcoded secrets in the code
