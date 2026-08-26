# Plan: 002 — Landing Page + API Key Auth

## Architecture

```
static/                  → Served by Vercel as static files
├── index.html           → Landing page
├── css/style.css        → Styles
└── js/app.js            → Form handling + API calls

api/index.py             → FastAPI app (unchanged)
src/auth.py              → New: API key extraction dependency
src/main.py              → Updated: add report endpoint
```

## Landing Page Design

Single-page layout:
1. **Hero** — "TrendPrompt Engine" + tagline + CTA
2. **How it works** — 3 steps (enter niche → get trends → copy prompts)
3. **Try it** — Form with niche input + API key input + submit
4. **Results** — Markdown report displayed after submission
5. **Footer** — GitHub link, credits

## API Key Flow

```
Browser                        Server
  │                              │
  │  POST /api/v1/report         │
  │  Header: Authorization: Bearer sk-...  │
  │  Body: {"niche": "plant moms"}  │
  │ ──────────────────────────▶  │
  │                              │  Validate key format
  │                              │  Create OpenAI client with key
  │                              │  Call OpenAI API
  │  ◀────────────────────────── │
  │  Response: {report: "..."}   │
```

## Files to Create/Modify

| File | Action | Description |
|------|--------|-------------|
| `static/index.html` | CREATE | Landing page |
| `static/css/style.css` | CREATE | Styles |
| `static/js/app.js` | CREATE | Form + API logic |
| `src/auth.py` | CREATE | API key dependency |
| `src/main.py` | MODIFY | Add POST /api/v1/report endpoint |
| `vercel.json` | MODIFY | Add static file serving |
| `api/index.py` | NO CHANGE | Already imports app |

## Execution Order

1. Create `src/auth.py` with API key dependency
2. Create `POST /api/v1/report` endpoint in `src/main.py`
3. Create `static/index.html` landing page
4. Create `static/css/style.css`
5. Create `static/js/app.js`
6. Update `vercel.json` for static + API
7. Test locally with `uvicorn src.main:app --reload`
8. Deploy and verify
