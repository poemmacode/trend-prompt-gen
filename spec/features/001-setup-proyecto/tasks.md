# Tasks: 001 — Project Setup

## Task Checklist

- [ ] **T1:** Create complete directory structure (`api/`, `src/`, `tests/`, `scripts/` and subdirectories).
- [ ] **T2:** Create all `__init__.py` files with descriptive docstrings.
- [ ] **T3:** Create `.gitignore` with Python + Vercel rules (venv, __pycache__, .env, .vercel/, dist/, build/).
- [ ] **T4:** Create `.env.example` with all required environment variables (OPENAI_API_KEY, ETSY_API_KEY, TWITTER_BEARER_TOKEN, AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_PARTNER_TAG) and placeholder values `[INSERT_HERE]`.
- [ ] **T5:** Create `pyproject.toml` with metadata, dependencies (core + dev), ruff, mypy, and pytest config per plan.md.
- [ ] **T6:** Create `vercel.json` with Python runtime config, builds, routes, and maxDuration.
- [ ] **T7:** Create `api/index.py` as Vercel entrypoint (imports `app` from `src.main`).
- [ ] **T8:** Create `src/config.py` with `Settings` class using pydantic-settings (reads from .env, validates required API keys).
- [ ] **T9:** Create `src/exceptions/base.py` with base exception `TrendPromptError`.
- [ ] **T10:** Create `src/trend_hunter/models.py` with base Pydantic models (at least: `Trend`, `TrendReport`, `Prompt`).
- [ ] **T11:** Create placeholders for all `src/` modules (orchestrator, scrapers, prompt_writer, utils, worker) with descriptive docstrings — no `pass`, no `# TODO`.
- [ ] **T12:** Create `tests/conftest.py` with base fixture (e.g. `mock_settings`).
- [ ] **T13:** Create `tests/unit/test_setup.py` with test verifying `src.config` can be imported and `Settings` works.
- [ ] **T14:** Create `README.md` with: project description, setup instructions (venv, install, .env), development commands, Vercel deploy instructions, reference to AGENTS.md.
- [ ] **T15:** Initialize git repository (`git init`).
- [ ] **T16:** Install dependencies in virtualenv (`pip install -e ".[dev]"`).
- [ ] **T17:** Run `ruff check .` and fix any errors.
- [ ] **T18:** Run `ruff format .` and verify with `ruff format --check .`.
- [ ] **T19:** Run `mypy src/` and fix any errors.
- [ ] **T20:** Run `pytest -v` and verify it passes.
- [ ] **T21:** Run `pytest --cov=src` and verify it generates a coverage report.
- [ ] **T22:** Make first commit: `"feat: initial project setup with SDD harness"`.

## Recommended Order

```
T1 → T2 → T3 → T4 → T5 → T6-T7 → T8-T11 (parallel) → T12-T13 → T14 → T15 → T16 → T17-T21 → T22
```

## Definition of "Done"

This feature is `[DONE]` when:
1. All tasks T1-T22 are marked with `[x]`.
2. `ruff check .` passes without errors.
3. `ruff format --check .` passes with no changes.
4. `mypy src/` passes without errors.
5. `pytest -v` passes with 0 failures.
6. The first commit exists in the git history.
