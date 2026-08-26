"""Supabase client initialization."""

from supabase import Client, create_client

from src.config import settings

_supabase_client: Client | None = None


def get_supabase() -> Client:
    """Get or create Supabase client singleton.

    Returns:
        Configured Supabase client.
    """
    global _supabase_client
    if _supabase_client is None:
        _supabase_client = create_client(settings.supabase_url, settings.supabase_service_key)
    return _supabase_client


def get_supabase_anon() -> Client:
    """Get Supabase client with anon key (for public operations).

    Returns:
        Supabase client with anon key.
    """
    return create_client(settings.supabase_url, settings.supabase_anon_key)
