"""FastAPI application entrypoint."""

from pathlib import Path

from fastapi import Depends, FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from src.auth import User, get_current_user
from src.database import get_supabase
from src.prompt_writer.engine import generate_prompts
from src.prompt_writer.formatter import format_report
from src.trend_hunter.models import Trend

ROOT_DIR = Path(__file__).parent.parent

app = FastAPI(
    title="TrendPrompt Engine",
    description="Trend-Hunter + Prompt-Writer: generates AI prompts based on real market trends",
    version="0.1.0",
)

# Mount static assets for local development (Vercel serves these automatically)
app.mount("/css", StaticFiles(directory=ROOT_DIR / "css"), name="css")
app.mount("/js", StaticFiles(directory=ROOT_DIR / "js"), name="js")


# --- Static Pages ---


@app.get("/")
def root() -> FileResponse:
    """Serve the landing page."""
    return FileResponse(ROOT_DIR / "index.html")


@app.get("/login")
def login_page() -> FileResponse:
    """Serve the login page."""
    return FileResponse(ROOT_DIR / "login.html")


@app.get("/signup")
def signup_page() -> FileResponse:
    """Serve the signup page."""
    return FileResponse(ROOT_DIR / "signup.html")


@app.get("/dashboard")
def dashboard_page() -> FileResponse:
    """Serve the dashboard page."""
    return FileResponse(ROOT_DIR / "dashboard.html")


@app.get("/health")
def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}


# --- Auth Routes ---


class SignupRequest(BaseModel):
    """Signup request body."""

    email: str
    password: str


class LoginRequest(BaseModel):
    """Login request body."""

    email: str
    password: str


class ApiKeyRequest(BaseModel):
    """API key save request body."""

    api_key: str


@app.post("/api/v1/auth/signup")
async def signup(body: SignupRequest) -> dict[str, str]:
    """Sign up a new user with Supabase Auth.

    Args:
        body: Email and password.

    Returns:
        User ID and access token.
    """
    supabase = get_supabase()
    result = supabase.auth.sign_up({"email": body.email, "password": body.password})

    if result.user is None:
        return {"error": "Signup failed. Email may already be in use."}

    return {
        "user_id": result.user.id,
        "access_token": result.session.access_token if result.session else "",
    }


@app.post("/api/v1/auth/login")
async def login(body: LoginRequest) -> dict[str, str]:
    """Log in an existing user with Supabase Auth.

    Args:
        body: Email and password.

    Returns:
        User ID and access token.
    """
    supabase = get_supabase()
    result = supabase.auth.sign_in_with_password({"email": body.email, "password": body.password})

    if result.user is None:
        return {"error": "Invalid email or password."}

    return {
        "user_id": result.user.id,
        "access_token": result.session.access_token if result.session else "",
    }


@app.get("/api/v1/auth/me")
async def get_me(user: User = Depends(get_current_user)) -> dict[str, str]:
    """Get current authenticated user info.

    Args:
        user: Authenticated user from JWT.

    Returns:
        User ID and email.
    """
    return {"user_id": user.id, "email": user.email}


# --- API Key Routes ---


@app.post("/api/v1/api-keys")
async def save_api_key(
    body: ApiKeyRequest, user: User = Depends(get_current_user)
) -> dict[str, str]:
    """Save or update the user's OpenAI API key.

    Args:
        body: The API key to save.
        user: Authenticated user.

    Returns:
        Success message.
    """
    supabase = get_supabase()

    # Upsert: try update first, insert if not exists
    existing = supabase.table("user_api_keys").select("id").eq("user_id", user.id).execute()

    if existing.data:
        supabase.table("user_api_keys").update({"api_key": body.api_key}).eq(
            "user_id", user.id
        ).execute()
    else:
        supabase.table("user_api_keys").insert(
            {"user_id": user.id, "api_key": body.api_key}
        ).execute()

    return {"status": "saved"}


@app.get("/api/v1/api-keys")
async def get_api_key(user: User = Depends(get_current_user)) -> dict[str, str]:
    """Get the user's stored OpenAI API key.

    Args:
        user: Authenticated user.

    Returns:
        The stored API key (or empty string if not set).
    """
    supabase = get_supabase()
    result = supabase.table("user_api_keys").select("api_key").eq("user_id", user.id).execute()

    if result.data:
        return {"api_key": result.data[0]["api_key"]}
    return {"api_key": ""}


# --- Report Route ---


@app.post("/api/v1/report")
async def generate_report(niche: str, user: User = Depends(get_current_user)) -> dict[str, str]:
    """Generate a trend report for the given niche.

    Uses the user's stored OpenAI API key.

    Args:
        niche: The market niche to analyze.
        user: Authenticated user.

    Returns:
        Report with generated prompts in markdown format.
    """
    # Fetch user's stored API key
    supabase = get_supabase()
    result = supabase.table("user_api_keys").select("api_key").eq("user_id", user.id).execute()

    if not result.data or not result.data[0].get("api_key"):
        return {"error": "No API key saved. Please add your OpenAI API key in settings."}

    api_key = result.data[0]["api_key"]

    # Placeholder trends — will be replaced by real scrapers (features 003-006)
    trends = [
        Trend(
            title=f"Rising interest in {niche}",
            description=f"Current trending topics and products in the {niche} market",
            source="Trend Analysis",
        ),
    ]

    all_prompts = []
    for trend in trends:
        prompts = await generate_prompts(trend, api_key)
        all_prompts.extend(prompts)

    report = format_report(niche, all_prompts)

    return {
        "niche": niche,
        "status": "success",
        "report": report,
    }
