"""Supabase client initialization."""

from supabase import Client, create_client

from src.config import settings

_supabase_client: Client | None = None


def get_supabase() -> Client:
    """Get or create Supabase client singleton (service role).

    Returns:
        Configured Supabase client with service role key.

    Raises:
        ValueError: If SUPABASE_URL or SUPABASE_SERVICE_KEY are not set.
    """
    if not settings.supabase_url:
        raise ValueError(
            "SUPABASE_URL is not set. Add it to your .env file or Vercel environment variables."
        )
    if not settings.supabase_service_key:
        raise ValueError(
            "SUPABASE_SERVICE_KEY is not set. Add it to your .env file or Vercel environment variables."
        )

    global _supabase_client
    if _supabase_client is None:
        _supabase_client = create_client(settings.supabase_url, settings.supabase_service_key)
    return _supabase_client


def get_supabase_for_user(access_token: str) -> Client:
    """Create a Supabase client with user's access token (for RLS).

    Args:
        access_token: The user's Supabase access token.

    Returns:
        Supabase client authenticated as the user.
    """
    client = create_client(settings.supabase_url, settings.supabase_anon_key)
    client.auth.set_session(access_token=access_token)
    return client
