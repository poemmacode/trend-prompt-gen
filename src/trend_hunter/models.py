"""Pydantic models for Trend-Hunter input/output."""

from pydantic import BaseModel, Field


class Trend(BaseModel):
    """A single trend item."""

    title: str = Field(description="Trend title")
    description: str = Field(default="", description="Brief description of the trend")
    source: str = Field(description="Source name (e.g. Google Trends, Amazon)")
    source_url: str = Field(default="", description="URL to the source data")
    niche_relevance: float = Field(default=0.0, ge=0.0, le=1.0, description="Relevance score 0-1")


class TrendReport(BaseModel):
    """Collection of trends for a specific niche."""

    niche: str = Field(description="The niche queried")
    trends: list[Trend] = Field(default_factory=list, description="List of discovered trends")
    generated_at: str = Field(default="", description="ISO timestamp of report generation")
