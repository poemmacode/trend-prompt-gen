"""Google Trends scraper: fetches rising terms, related queries, and interest by region."""

from pytrends.request import TrendReq

from src.trend_hunter.models import Trend


def scrape_google_trends(niche: str, timeframe: str = "today 1-m") -> list[Trend]:
    """Scrape Google Trends data for a given niche.

    Args:
        niche: The market niche to search for.
        timeframe: Time range for trends (default: last month).

    Returns:
        List of Trend items from Google Trends.
    """
    pytrends = TrendReq(hl="en-US", tz=360)
    trends: list[Trend] = []

    try:
        pytrends.build_payload([niche], cat=0, timeframe=timeframe, geo="")
        interest = pytrends.interest_over_time()

        if not interest.empty and niche in interest.columns:
            avg_interest = float(interest[niche].mean())
            trend = Trend(
                title=f"Google Trends: {niche}",
                description=f"Average interest score: {avg_interest:.0f}/100 over the selected period",
                source="Google Trends",
                source_url=f"https://trends.google.com/trends/explore?q={niche.replace(' ', '+')}",
                niche_relevance=min(avg_interest / 100, 1.0),
            )
            trends.append(trend)

        # Related queries
        related = pytrends.related_queries()
        if niche in related and related[niche].get("rising") is not None:
            rising = related[niche]["rising"].head(5)
            for _, row in rising.iterrows():
                query = row.get("query", "")
                value = row.get("value", 0)
                if query:
                    trends.append(
                        Trend(
                            title=f"Rising: {query}",
                            description=f"Search volume increase: {value}%",
                            source="Google Trends",
                            source_url=f"https://trends.google.com/trends/explore?q={query.replace(' ', '+')}",
                            niche_relevance=min(value / 1000, 1.0) if value else 0.5,
                        )
                    )

    except Exception:
        # Return at least the base trend if scraping fails
        pass

    if not trends:
        trends.append(
            Trend(
                title=f"Trend data for {niche}",
                description="Google Trends data could not be retrieved",
                source="Google Trends",
                source_url=f"https://trends.google.com/trends/explore?q={niche.replace(' ', '+')}",
            )
        )

    return trends
