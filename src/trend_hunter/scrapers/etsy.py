"""Etsy scraper: identifies trending searches and popular items."""

from src.trend_hunter.models import Trend


async def scrape_etsy(niche: str) -> list[Trend]:
    """Scrape Etsy trending data for a given niche.

    Args:
        niche: The market niche to search for.

    Returns:
        List of Trend items from Etsy.
    """
    raise NotImplementedError("Etsy scraper not yet implemented")
