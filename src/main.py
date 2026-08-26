"""FastAPI application entrypoint."""

from fastapi import FastAPI

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
