"""FastAPI application entrypoint."""

from fastapi import Depends, FastAPI

from src.auth import get_api_key

app = FastAPI(
    title="TrendPrompt Engine",
    description="Trend-Hunter + Prompt-Writer: generates AI prompts based on real market trends",
    version="0.1.0",
)


@app.get("/")
def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "TrendPrompt Engine API", "docs": "/docs"}


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
