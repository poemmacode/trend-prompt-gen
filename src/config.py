"""Centralized configuration using pydantic-settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # OpenAI
    openai_api_key: str = ""

    # Supabase (supports both naming conventions)
    supabase_url: str = ""
    supabase_anon_key: str = ""
    supabase_service_key: str = ""
    supabase_jwt_secret: str = ""

    @property
    def supabase_key(self) -> str:
        """Get the Supabase service key (for admin operations)."""
        return self.supabase_service_key

    # Scraping (future)
    etsy_api_key: str = ""
    twitter_bearer_token: str = ""
    amazon_access_key: str = ""
    amazon_secret_key: str = ""
    amazon_partner_tag: str = ""


settings = Settings()
