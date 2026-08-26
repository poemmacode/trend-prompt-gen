"""Pydantic models for Prompt-Writer output."""

from pydantic import BaseModel, Field


class Prompt(BaseModel):
    """A generated image prompt based on a trend."""

    trend_title: str = Field(description="Title of the trend this prompt is based on")
    suggested_product: str = Field(description="Product suggestion based on the trend")
    prompt_text: str = Field(description="The complete prompt for AI image generation")
    sources: list[str] = Field(default_factory=list, description="Source URLs for the trend")
