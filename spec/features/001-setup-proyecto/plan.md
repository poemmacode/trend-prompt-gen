# Plan: 001 — Project Setup

## Strategy

Incremental setup in dependency order: structure → configuration → tools → validation.

## Initial Folder Architecture

```
trend-prompt-gen/
├── .venv/                          # Virtualenv (gitignored)
├── api/
│   └── index.py                    # Vercel entrypoint: imports app from src/main.py
├── src/
│   ├── __init__.py                 # Root package src
│   ├── main.py                     # FastAPI app (imported by api/index.py)
│   ├── config.py                   # Pydantic-settings: Settings class
│   ├── exceptions/
│   │   ├── __init__.py
│   │   └── base.py                 # TrendPromptError base
│   ├── trend_hunter/
│   │   ├── __init__.py
│   │   ├── models.py               # Pydantic models: TrendReport, Trend, etc.
│   │   ├── orchestrator.py         # Placeholder: async def run_trend_hunt()
│   │   └── scrapers/
│   │       ├── __init__.py
│   │       ├── google_trends.py    # Placeholder
│   │       ├── amazon.py           # Placeholder
│   │       ├── etsy.py             # Placeholder
│   │       ├── social.py           # Placeholder
│   │       └── worker.py           # Off-chain runner (cron/VPS)
│   ├── prompt_writer/
│   │   ├── __init__.py
│   │   ├── engine.py               # Placeholder
│   │   ├── templates.py            # Placeholder
│   │   └── formatter.py            # Placeholder
│   └── utils/
│       ├── __init__.py
│       ├── http_client.py          # Placeholder
│       └── rate_limiter.py         # Placeholder
├── tests/
│   ├── __init__.py
│   ├── conftest.py                 # Base fixtures (e.g. mock httpx client)
│   ├── unit/
│   │   ├── __init__.py
│   │   └── test_setup.py           # Test verifying imports and structure
│   ├── integration/
│   │   └── __init__.py
│   └── e2e/
│       └── __init__.py
├── scripts/                        # Empty directory (prepared)
├── spec/                           # Already exists (SDD harness)
├── .env.example
├── .gitignore
├── pyproject.toml
├── vercel.json                     # Vercel deploy configuration
├── README.md
└── AGENTS.md                       # Already exists
```

## pyproject.toml Configuration

```toml
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.backends._legacy:_Backend"

[project]
name = "trend-prompt-engine"
version = "0.1.0"
description = "Trend-Hunter + Prompt-Writer: generates AI prompts based on real market trends"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.110",
    "uvicorn[standard]>=0.29",
    "pydantic>=2.6",
    "pydantic-settings>=2.2",
    "httpx>=0.27",
    "python-dotenv>=1.0",
    "openai>=1.14",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.1",
    "pytest-asyncio>=0.23",
    "pytest-cov>=5.0",
    "respx>=0.21",
    "ruff>=0.4",
    "mypy>=1.9",
    "beautifulsoup4>=4.12",
    "lxml>=5.1",
]

[tool.setuptools.packages.find]
where = ["."]
include = ["src*"]

[tool.ruff]
target-version = "py311"
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I", "N", "UP", "B", "A", "C4", "SIM", "TCH"]
ignore = ["E501"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"

[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

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

## Execution Order

1. **Create folder structure** (all directories and `__init__.py`, including `api/`).
2. **Create `.gitignore`** (standard Python + Vercel rules).
3. **Create `.env.example`** (all variables with placeholders).
4. **Create `pyproject.toml`** (full config per template above).
5. **Create `vercel.json`** (Python runtime config for Vercel).
6. **Create `api/index.py`** (Vercel entrypoint importing the FastAPI app).
7. **Create placeholder modules** in `src/` (each with minimum docstring, NO `pass`).
8. **Create `src/main.py`** with FastAPI instance (app = FastAPI()).
9. **Create `tests/conftest.py`** with base fixture.
10. **Create `tests/unit/test_setup.py`** with import test.
11. **Create `README.md`** with setup and deploy instructions.
12. **Initialize git** and make first commit.
13. **Install dependencies** in venv and verify ruff/mypy/pytest pass.

## Placeholders — Implementation Rule

Each placeholder file in `src/` must contain:
```python
"""[Module name]: [Brief description of purpose]."""
```
**DO NOT** use `pass`. **DO NOT** use `# TODO`. If the module has no implementation yet, the docstring is sufficient for setup.

## vercel.json Configuration

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "api/index.py"
    }
  ],
  "functions": {
    "api/index.py": {
      "maxDuration": 60
    }
  }
}
```

## Vercel Entrypoint (api/index.py)

```python
"""Entrypoint for Vercel Serverless Functions."""

from src.main import app  # noqa: F401

# Vercel detects `app` automatically as an ASGI application
```

## Final Validation

```bash
# Create venv
python3 -m venv .venv
source .venv/bin/activate

# Install in dev mode
pip install -e ".[dev]"

# Verify tools
ruff check .
ruff format --check .
mypy src/
pytest -v
```

All must pass without errors to consider this feature complete.
