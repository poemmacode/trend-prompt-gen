"""Authentication dependencies and utilities for FastAPI."""

from dataclasses import dataclass

import jwt
from fastapi import Header, HTTPException

from src.config import settings


@dataclass
class User:
    """Authenticated user."""

    id: str
    email: str


async def get_current_user(authorization: str | None = Header(default=None)) -> User:
    """Extract and verify Supabase JWT from Authorization header.

    Args:
        authorization: The Authorization header value.

    Returns:
        Authenticated User object.

    Raises:
        HTTPException: If no token, invalid format, or verification fails.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Authentication required. Please log in.")

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid Authorization format.")

    token = authorization.removeprefix("Bearer ").strip()

    if not token:
        raise HTTPException(status_code=401, detail="Token cannot be empty.")

    try:
        payload = jwt.decode(
            token,
            settings.supabase_jwt_secret,
            algorithms=["HS256"],
            audience="authenticated",
        )
    except jwt.ExpiredSignatureError as err:
        raise HTTPException(status_code=401, detail="Token expired. Please log in again.") from err
    except jwt.InvalidTokenError as err:
        raise HTTPException(status_code=401, detail="Invalid token.") from err

    user_id = payload.get("sub")
    email = payload.get("email", "")

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token payload.")

    return User(id=user_id, email=email)
