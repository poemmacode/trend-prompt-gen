"""HTTP client with retry/backoff for external API calls."""

import httpx


async def get_client() -> httpx.AsyncClient:
    """Create an async HTTP client with default configuration.

    Returns:
        Configured httpx.AsyncClient instance.
    """
    raise NotImplementedError("HTTP client not yet implemented")
