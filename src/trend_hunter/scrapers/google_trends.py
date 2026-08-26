"""Google Trends scraper: fetches rising terms, related queries, and interest by region."""

from src.trend_hunter.models import Trend


async def scrape_google_trends(niche: str) -> list[Trend]:
    """Scrape Google Trends data for a given niche.

    Args:
        niche: The market niche to search for.

    Returns:
        List of Trend items from Google Trends.
    """
    raise NotImplementedError("Google Trends scraper not yet implemented")
