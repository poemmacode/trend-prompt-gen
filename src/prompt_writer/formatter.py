"""Markdown report formatter: generates the final report with trends, prompts, and sources."""

from typing import Any


def format_report(niche: str, trends: list[Any], prompts: list[Any]) -> str:
    """Format trends and prompts into a markdown report.

    Args:
        niche: The niche analyzed.
        trends: List of Trend objects.
        prompts: List of Prompt objects.

    Returns:
        Formatted markdown string.
    """
    raise NotImplementedError("Report formatter not yet implemented")
