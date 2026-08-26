"""Request rate control for external API calls."""


class RateLimiter:
    """Rate limiter to control request frequency."""

    def __init__(self, max_requests: int = 10, window_seconds: int = 60) -> None:
        self.max_requests = max_requests
        self.window_seconds = window_seconds

    async def acquire(self) -> None:
        """Acquire a rate limit slot. Blocks if limit exceeded."""
        raise NotImplementedError("Rate limiter not yet implemented")
