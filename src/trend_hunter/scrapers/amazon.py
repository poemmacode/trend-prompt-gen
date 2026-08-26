"""Amazon scraper: extracts best sellers and movers & shakers."""

from src.trend_hunter.models import Trend


async def scrape_amazon(niche: str) -> list[Trend]:
    """Scrape Amazon Best Sellers for a given niche.

    Args:
        niche: The market niche to search for.

    Returns:
        List of Trend items from Amazon.
    """
    raise NotImplementedError("Amazon scraper not yet implemented")
