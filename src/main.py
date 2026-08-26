"""FastAPI application entrypoint."""

from pathlib import Path

from fastapi import Depends, FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from src.auth import get_api_key

ROOT_DIR = Path(__file__).parent.parent

app = FastAPI(
    title="TrendPrompt Engine",
    description="Trend-Hunter + Prompt-Writer: generates AI prompts based on real market trends",
    version="0.1.0",
)

# Mount static assets for local development (Vercel serves these automatically)
app.mount("/css", StaticFiles(directory=ROOT_DIR / "css"), name="css")
app.mount("/js", StaticFiles(directory=ROOT_DIR / "js"), name="js")


@app.get("/")
def root() -> FileResponse:
    """Serve the landing page."""
    return FileResponse(ROOT_DIR / "index.html")


@app.get("/health")
def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}


@app.post("/api/v1/report")
async def generate_report(niche: str, api_key: str = Depends(get_api_key)) -> dict[str, str]:
    """Generate a trend report for the given niche.

    Args:
        niche: The market niche to analyze.
        api_key: User's OpenAI API key (from Authorization header).

    Returns:
        Report data with trends and prompts.
    """
    # TODO: Implement actual trend hunting and prompt generation
    # For now, return a placeholder showing the key was accepted
    return {
        "niche": niche,
        "status": "received",
        "message": f"API key accepted. Trend hunting for '{niche}' will be implemented in future features.",
    }
