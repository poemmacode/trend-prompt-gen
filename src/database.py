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
