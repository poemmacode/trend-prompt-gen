# Plan: 003 — Authentication System (Supabase)

## Architecture

```
Frontend (浏览器)                    Backend (FastAPI)
┌─────────────────┐                ┌──────────────────────┐
│ Login/Signup     │───POST auth──▶│ Supabase Auth        │
│ (Supabase JS)    │◀──JWT token──│ (email + password)   │
│                  │                │                      │
│ Dashboard        │───POST /api──▶│ get_current_user()   │
│ (protected)      │   + JWT       │ (verifies JWT)       │
└─────────────────┘                │                      │
                                   │ Fetches user's       │
                                   │ API key from DB      │
                                   │                      │
                                   │ Calls OpenAI with    │
                                   │ user's key           │
                                   └──────────────────────┘
```

## Database Schema (Supabase)

```sql
CREATE TABLE user_api_keys (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  api_key TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(user_id)
);

-- RLS: users can only access their own keys
ALTER TABLE user_api_keys ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read their own API key"
  ON user_api_keys FOR SELECT
  USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own API key"
  ON user_api_keys FOR INSERT
  WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update their own API key"
  ON user_api_keys FOR UPDATE
  USING (auth.uid() = user_id);
```

## Files to Create/Modify

| File | Action | Description |
|------|--------|-------------|
| `src/database.py` | CREATE | Supabase client initialization |
| `src/auth.py` | MODIFY | Add `get_current_user` JWT verification |
| `src/main.py` | MODIFY | Add auth routes + protect report endpoint |
| `requirements.txt` | MODIFY | Add `supabase` package |
| `index.html` | MODIFY | Add login/signup/dashboard pages |
| `js/app.js` | MODIFY | Add auth flow + dashboard logic |
| `css/style.css` | MODIFY | Add auth page styles |

## Execution Order

1. Add `supabase` dependency to pyproject.toml
2. Create `src/database.py` with Supabase client
3. Update `src/auth.py` with JWT verification
4. Create auth API routes (signup, login, api-keys)
5. Protect POST /api/v1/report
6. Update frontend with login/signup/dashboard
7. Test locally
8. Deploy
