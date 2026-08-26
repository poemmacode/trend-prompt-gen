# Tasks: 002 — Landing Page + API Key Auth

## Task Checklist

- [ ] **T1:** Create `src/auth.py` with `get_api_key` FastAPI dependency (extracts from Authorization header, validates format)
- [ ] **T2:** Create `POST /api/v1/report` endpoint in `src/main.py` (accepts niche, requires API key, returns placeholder report)
- [ ] **T3:** Create `static/index.html` with hero, how-it-works, form, results section
- [ ] **T4:** Create `static/css/style.css` with responsive design
- [ ] **T5:** Create `static/js/app.js` with form submission and report display
- [ ] **T6:** Update `vercel.json` to serve static files + API routes
- [ ] **T7:** Test locally with `uvicorn src.main:app --reload`
- [ ] **T8:** Verify ruff check, mypy, pytest all pass
- [ ] **T9:** Commit and push

## Definition of "Done"

This feature is `[DONE]` when:
1. Landing page loads at `/` with no errors
2. Form submits niche + API key to `/api/v1/report`
3. 401 returned if no API key provided
4. Report returned when valid API key provided
5. All linting/type checks pass
