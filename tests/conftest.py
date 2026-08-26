"""Shared test fixtures for TrendPrompt Engine."""

import pytest


@pytest.fixture
def mock_settings() -> dict[str, str]:
    """Mock environment variables for testing."""
    return {
        "OPENAI_API_KEY": "sk-test-key",
        "ETSY_API_KEY": "etsy-test-key",
        "TWITTER_BEARER_TOKEN": "twitter-test-token",
        "AMAZON_ACCESS_KEY": "amazon-test-key",
        "AMAZON_SECRET_KEY": "amazon-test-secret",
        "AMAZON_PARTNER_TAG": "test-partner-20",
    }
