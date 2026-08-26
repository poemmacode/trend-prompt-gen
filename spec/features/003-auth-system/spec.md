# Spec: 003 — Authentication System (Supabase)

## Status: [IN_PROGRESS]

## Objective

Implement user authentication using Supabase so users can sign up, log in, store their OpenAI API key, and access the prompt generator without re-entering their key every time.

## Flow

```
/                    → Landing page (public)
/login               → Login form
/signup              → Signup form
/dashboard           → Protected: enter niche, see reports
POST /api/v1/report  → Requires valid Supabase JWT + user's stored API key
```

## Acceptance Criteria

### AC-1: Supabase Integration
- [ ] `supabase` Python package installed
- [ ] `src/auth.py` updated with Supabase JWT verification
- [ ] Environment variables: `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_KEY`

### AC-2: Database Schema
- [ ] `user_api_keys` table: `user_id` (UUID, FK to auth.users), `api_key` (text), `created_at` (timestamp)
- [ ] RLS policies: users can only read/write their own API keys

### AC-3: Auth Middleware
- [ ] FastAPI dependency `get_current_user` extracts JWT from `Authorization: Bearer <token>`
- [ ] Returns 401 if token invalid or expired
- [ ] Returns user ID if valid

### AC-4: API Key Storage
- [ ] `POST /api/v1/api-keys` — Save user's OpenAI API key
- [ ] `GET /api/v1/api-keys` — Get user's stored API key
- [ ] API key encrypted at rest (or stored as-is for MVP)

### AC-5: Updated Report Endpoint
- [ ] `POST /api/v1/report` now requires Supabase JWT (not raw API key)
- [ ] Fetches user's stored API key from database
- [ ] Uses stored key for OpenAI calls

### AC-6: Frontend Auth UI
- [ ] Login page (`/login`) with email + password
- [ ] Signup page (`/signup`) with email + password
- [ ] Auth state tracked in localStorage
- [ ] Dashboard redirects to login if not authenticated
- [ ] Logout button clears session

### AC-7: Landing Page Update
- [ ] Hero CTA links to `/signup` instead of `#try`
- [ ] "Try it" form removed from public landing page
- [ ] Dashboard page with the niche input form (protected)

## Source of Truth

This spec is the source of truth for feature 003.

## Dependencies

- 001 (Project Setup)
- 002 (Landing Page)
- 008 (Prompt-Writer) — already implemented

## Risks

- **R1:** Supabase free tier limits. **Mitigation:** 50K monthly active users, 500MB database — sufficient for MVP.
- **R2:** JWT verification adds latency. **Mitigation:** Supabase JWTs are verified locally (no network call), <1ms overhead.
