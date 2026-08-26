"""Unit tests verifying project setup and basic imports."""

import importlib


def test_src_package_imports() -> None:
    """Verify that the src package can be imported."""
    import src

    assert src.__doc__ is not None


def test_config_imports() -> None:
    """Verify that src.config module can be imported."""
    module = importlib.import_module("src.config")
    assert module is not None


def test_exceptions_imports() -> None:
    """Verify that src.exceptions.base can be imported."""
    from src.exceptions.base import TrendPromptError

    assert issubclass(TrendPromptError, Exception)


def test_models_imports() -> None:
    """Verify that src.trend_hunter.models can be imported."""
    from src.trend_hunter.models import Trend, TrendReport

    assert Trend is not None
    assert TrendReport is not None


def test_prompt_writer_models_imports() -> None:
    """Verify that src.prompt_writer.models can be imported."""
    from src.prompt_writer.models import Prompt

    assert Prompt is not None


def test_trend_creation() -> None:
    """Verify that a Trend model can be created with required fields."""
    from src.trend_hunter.models import Trend

    trend = Trend(title="Test Trend", source="Google Trends")
    assert trend.title == "Test Trend"
    assert trend.source == "Google Trends"
    assert trend.niche_relevance == 0.0


def test_trend_report_creation() -> None:
    """Verify that a TrendReport model can be created."""
    from src.trend_hunter.models import Trend, TrendReport

    trend = Trend(title="Test Trend", source="Google Trends")
    report = TrendReport(niche="test niche", trends=[trend])
    assert report.niche == "test niche"
    assert len(report.trends) == 1


def test_prompt_creation() -> None:
    """Verify that a Prompt model can be created."""
    from src.prompt_writer.models import Prompt

    prompt = Prompt(
        trend_title="Test Trend",
        suggested_product="Test Product",
        prompt_text="A beautiful image of test",
        sources=["https://example.com"],
    )
    assert prompt.trend_title == "Test Trend"
    assert len(prompt.sources) == 1
