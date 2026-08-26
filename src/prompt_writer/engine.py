"""Prompt generation engine: converts trends into AI image prompts using OpenAI."""

from openai import AsyncOpenAI

from src.prompt_writer.models import Prompt
from src.prompt_writer.templates import SYSTEM_PROMPT
from src.trend_hunter.models import Trend

PROMPTS_PER_TREND = 8


async def generate_prompts(trend: Trend, api_key: str) -> list[Prompt]:
    """Generate image prompts for a given trend using OpenAI GPT-4o-mini.

    Args:
        trend: The trend to generate prompts for.
        api_key: User's OpenAI API key.

    Returns:
        List of Prompt items ready for AI image generation.
    """
    client = AsyncOpenAI(api_key=api_key)

    user_message = f"""Generate {PROMPTS_PER_TREND} original, creative image prompts for this trend:

Title: {trend.title}
Description: {trend.description}
Source: {trend.source}

For each prompt, provide:
1. A suggested product based on the trend
2. The complete prompt text optimized for Midjourney/DALL-E/Stable Diffusion

Return as JSON array with fields: suggested_product, prompt_text"""

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.8,
        max_tokens=4000,
    )

    content = response.choices[0].message.content or "[]"

    prompts = _parse_prompts(content, trend)
    return prompts


def _parse_prompts(content: str, trend: Trend) -> list[Prompt]:
    """Parse OpenAI response into Prompt objects.

    Args:
        content: Raw response content from OpenAI.
        trend: The trend these prompts are based on.

    Returns:
        List of parsed Prompt objects.
    """
    import json

    # Extract JSON from the response (handle markdown code blocks)
    text = content.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        text = "\n".join(lines[1:-1])

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        # If JSON parsing fails, return a single prompt with raw content
        return [
            Prompt(
                trend_title=trend.title,
                suggested_product=trend.description or "AI-generated image",
                prompt_text=text[:2000],
                sources=[trend.source_url] if trend.source_url else [],
            )
        ]

    prompts = []
    for item in data[:PROMPTS_PER_TREND]:
        prompts.append(
            Prompt(
                trend_title=trend.title,
                suggested_product=item.get("suggested_product", "AI-generated image"),
                prompt_text=item.get("prompt_text", ""),
                sources=[trend.source_url] if trend.source_url else [],
            )
        )

    return prompts
