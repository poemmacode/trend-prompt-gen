"""Prompt generation engine: converts trends into AI image prompts using OpenAI."""

from src.prompt_writer.models import Prompt
from src.trend_hunter.models import Trend


async def generate_prompts(trend: Trend) -> list[Prompt]:
    """Generate image prompts for a given trend using OpenAI GPT-4o-mini.

    Args:
        trend: The trend to generate prompts for.

    Returns:
        List of Prompt items ready for AI image generation.
    """
    raise NotImplementedError("Prompt engine not yet implemented")
