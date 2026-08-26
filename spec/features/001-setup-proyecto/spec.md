# Spec: 001 — Project Setup

## Status: [PLANNING]

## Objective

Initialize the base infrastructure of the TrendPrompt Engine project so the development team can begin implementing features with a solid, consistent, and verifiable foundation.

## Scope

This feature includes ONLY the development environment configuration. It does not include business logic, scrapers, or external API integrations.

## Acceptance Criteria

### AC-1: Virtual Environment
- [ ] A `.venv/` directory exists with Python 3.11+ virtualenv activated.
- [ ] `python --version` returns 3.11 or higher inside the venv.
- [ ] The venv is in `.gitignore`.

### AC-2: Folder Structure
- [ ] The complete directory structure defined in `AGENTS.md` exists:
  ```
  api/
  src/
  src/exceptions/
  src/trend_hunter/
  src/trend_hunter/scrapers/
  src/prompt_writer/
  src/utils/
  tests/
  tests/unit/
  tests/integration/
  tests/e2e/
  scripts/
  ```
- [ ] All directories contain `__init__.py` where applicable.
- [ ] No `__init__.py` is empty without reason (minimum a docstring or import).

### AC-3: Configuration Files
- [ ] `pyproject.toml` configured with:
  - Project metadata (name, version, description).
  - Core dependencies installed (fastapi, pydantic, pydantic-settings, httpx, openai).
  - Dev dependencies installed (pytest, pytest-asyncio, pytest-cov, ruff, mypy, respx).
  - Ruff configuration (target-version py311, selected rules).
  - MyPy configuration (strict mode).
  - Pytest configuration (testpaths, markers).
- [ ] `.env.example` created with all required environment variables (placeholder values).
- [ ] `.gitignore` configured for Python + Vercel (venv, __pycache__, .env, .vercel/, *.egg-info, .mypy_cache, .pytest_cache, .ruff_cache).

### AC-3b: Vercel Configuration
- [ ] `vercel.json` created with Python runtime config (`@vercel/python`), builds, routes, and maxDuration.
- [ ] `api/index.py` created as entrypoint importing `app` from `src.main`.
- [ ] `.gitignore` includes `.vercel/` (local Vercel CLI directory).

### AC-4: Functional Linters
- [ ] `ruff check .` runs without errors on existing code.
- [ ] `ruff format --check .` passes with no changes needed.
- [ ] `mypy src/` runs without type errors.

### AC-5: Base Tests
- [ ] `pytest` runs without errors (even with 0 tests, it must pass cleanly).
- [ ] At least one trivial unit test exists verifying the setup works (e.g., imports `src.config` without errors).
- [ ] `pytest --cov=src` shows a coverage report (can be 0% if no code, but must generate the report).

### AC-6: Git
- [ ] Git repository initialized with `git init`.
- [ ] First commit with base structure: "feat: initial project setup with SDD harness".
- [ ] `.gitignore` excludes all generated artifacts.

### AC-7: README
- [ ] `README.md` created with:
  - Project name and description.
  - Setup instructions (create venv, install dependencies, configure .env).
  - Development commands (tests, linting, type checking).
  - Vercel deploy instructions (`vercel deploy`, environment variables in Dashboard).
  - Reference to `AGENTS.md` for understanding the project.

## Source of Truth

This spec is the source of truth for feature 001. Any deviation from the plan must be documented here first before implementation.

## Dependencies

None. This is the root feature of the project.

## Risks

- **R1:** Dependency version incompatibility. **Mitigation:** Pin minimum versions in pyproject.toml and test on clean venv.
- **R2:** Ruff/MyPy configuration too strict for initial code. **Mitigation:** Start with moderate config, adjust as code is written.
