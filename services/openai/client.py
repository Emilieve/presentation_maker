from typing import Any

from config.settings import settings


def create_openai_client() -> Any:
    """Create and return an OpenAI client instance.

    Returns a client from the official openai package if available.
    Raises at runtime if the API key is missing. Kept as Any to avoid
    importing the heavy package when unused in placeholder mode.
    """
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    # Lazy import to keep startup fast when not calling OpenAI
    from openai import OpenAI  # type: ignore

    return OpenAI(api_key=settings.openai_api_key)

