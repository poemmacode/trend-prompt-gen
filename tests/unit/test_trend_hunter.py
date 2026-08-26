"""Unit tests for Trend-Hunter models and orchestrator."""

from src.trend_hunter.models import Trend, TrendReport
from src.trend_hunter.orchestrator import run_trend_hunt


def test_trend_creation_with_all_fields() -> None:
    """Verify Trend model with all fields."""
    trend = Trend(
        title="Test Trend",
        description="A test trend",
        source="Google Trends",
        source_url="https://example.com",
        niche_relevance=0.85,
    )
    assert trend.title == "Test Trend"
    assert trend.niche_relevance == 0.85
    assert trend.source_url == "https://example.com"


def test_trend_report_creation() -> None:
    """Verify TrendReport model."""
    trends = [
        Trend(title="Trend 1", source="Source A"),
        Trend(title="Trend 2", source="Source B"),
    ]
    report = TrendReport(niche="test niche", trends=trends)
    assert report.niche == "test niche"
    assert len(report.trends) == 2


def test_orchestrator_returns_report() -> None:
    """Verify orchestrator returns a TrendReport."""
    report = run_trend_hunt("plant moms")
    assert isinstance(report, TrendReport)
    assert report.niche == "plant moms"
    assert isinstance(report.trends, list)
    assert len(report.trends) > 0


def test_orchestrator_trends_have_sources() -> None:
    """Verify that trends from orchestrator have source information."""
    report = run_trend_hunt("vintage clothing")
    for trend in report.trends:
        assert trend.title
        assert trend.source
