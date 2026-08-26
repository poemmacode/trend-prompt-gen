"""Main Trend-Hunter coordinator: orchestrates scrapers and deduplicates trends."""

from src.trend_hunter.models import Trend, TrendReport
from src.trend_hunter.scrapers.google_trends import scrape_google_trends


def run_trend_hunt(niche: str) -> TrendReport:
    """Execute a complete trend hunt for the given niche.

    Collects trends from all available sources, deduplicates, and ranks by relevance.

    Args:
        niche: The market niche to analyze.

    Returns:
        A TrendReport containing discovered trends.
    """
    all_trends: list[Trend] = []

    # Google Trends
    try:
        google_trends = scrape_google_trends(niche)
        all_trends.extend(google_trends)
    except Exception:
        pass

    # Deduplicate by title
    seen_titles: set[str] = set()
    unique_trends: list[Trend] = []
    for trend in all_trends:
        if trend.title not in seen_titles:
            seen_titles.add(trend.title)
            unique_trends.append(trend)

    # Sort by niche relevance (descending)
    unique_trends.sort(key=lambda t: t.niche_relevance, reverse=True)

    return TrendReport(
        niche=niche,
        trends=unique_trends,
    )
