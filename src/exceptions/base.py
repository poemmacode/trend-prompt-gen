"""Base exceptions for TrendPrompt Engine."""


class TrendPromptError(Exception):
    """Base exception for all TrendPrompt Engine errors."""

    def __init__(self, message: str = "An unexpected error occurred") -> None:
        self.message = message
        super().__init__(self.message)
