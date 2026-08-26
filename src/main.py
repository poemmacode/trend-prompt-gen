"""FastAPI application entrypoint."""

from pathlib import Path

from fastapi import Depends, FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from src.auth import get_api_key
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

    Uses the user's OpenAI API key to generate prompts via GPT-4o-mini.

    Args:
        niche: The market niche to analyze.
        api_key: User's OpenAI API key (from Authorization header).

    Returns:
        Report with generated prompts in markdown format.
    """
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
