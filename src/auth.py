"""API key authentication dependency for FastAPI."""

from fastapi import Header, HTTPException


async def get_api_key(authorization: str | None = Header(default=None)) -> str:
    """Extract and validate API key from Authorization header.

    Args:
        authorization: The Authorization header value.

    Returns:
        The validated API key.

    Raises:
        HTTPException: If no key provided or format is invalid.
    """
    if not authorization:
        raise HTTPException(
            status_code=401, detail="API key required. Provide it in the Authorization header."
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid Authorization format. Use: Bearer <your-openai-api-key>",
        )

    api_key = authorization.removeprefix("Bearer ").strip()

    if not api_key:
        raise HTTPException(status_code=401, detail="API key cannot be empty.")

    if not api_key.startswith("sk-"):
        raise HTTPException(
            status_code=401,
            detail="Invalid API key format. OpenAI keys start with 'sk-'.",
        )

    return api_key
