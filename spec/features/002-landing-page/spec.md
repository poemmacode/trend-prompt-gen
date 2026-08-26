# Spec: 002 — Landing Page + API Key Auth

## Status: [IN_PROGRESS]

## Objective

Build a static landing page that explains TrendPrompt Engine and lets users try the tool by entering their own OpenAI API key. No user accounts or database needed — the user's API key is passed directly to the backend.

## Scope

- Static landing page (HTML/CSS/JS) served by Vercel
- API key input form on the landing page
- Backend middleware that validates the API key is present before calling OpenAI
- No user authentication, no database, no sessions

## Flow

```
User visits / → Landing page (static, no auth)
User fills form (niche + OpenAI API key) → POST /api/v1/report
Backend validates key is present → Calls OpenAI with user's key → Returns report
```

## Acceptance Criteria

### AC-1: Static Landing Page
- [ ] `static/index.html` with responsive design (mobile-first)
- [ ] Hero section: title, tagline, brief description
- [ ] How it works section (3 steps)
- [ ] Input form: niche text field + OpenAI API key input (password field)
- [ ] Submit button → calls POST /api/v1/report
- [ ] Results section: displays the markdown report
- [ ] No external CSS frameworks (vanilla CSS or minimal utility)
- [ ] Works without JavaScript for layout (JS only for form submission)

### AC-2: API Key Handling
- [ ] API key input is a password field (masked)
- [ ] API key is sent in the request header `Authorization: Bearer <key>`
- [ ] API key is never stored server-side or logged
- [ ] API key is never sent to any service other than OpenAI

### AC-3: Backend Auth Middleware
- [ ] FastAPI dependency that extracts API key from `Authorization` header
- [ ] Returns 401 if no API key provided
- [ ] Returns 401 if API key format is invalid (doesn't start with `sk-`)
- [ ] Passes the user's API key to the OpenAI client

### AC-4: Vercel Config
- [ ] `vercel.json` serves `static/` for root path `/`
- [ ] API routes still go to `api/index.py`
- [ ] No breaking changes to existing API endpoints

## Source of Truth

This spec is the source of truth for feature 002.

## Dependencies

- 001 (Project Setup)
- 011 (REST API) — partially, for the report endpoint

## Risks

- **R1:** User enters an invalid/expired API key. **Mitigation:** Return clear error message from OpenAI.
- **R2:** User's API key is exposed in browser network tab. **Mitigation:** Use HTTPS (Vercel default), never log the key.
