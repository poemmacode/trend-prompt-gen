"""Off-chain scraper worker: runs scrapers outside Vercel and stores results in cache."""

from src.trend_hunter.models import TrendReport


async def run_worker(niche: str) -> TrendReport:
    """Execute all scrapers off-chain and store results in cache.

    Args:
        niche: The market niche to analyze.

    Returns:
        A TrendReport with all scraped trends.
    """
    raise NotImplementedError("Scraper worker not yet implemented")
