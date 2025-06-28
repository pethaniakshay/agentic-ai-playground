import os
from dotenv import load_dotenv, dotenv_values

def get_gemini_api_key():
    # Load environment variables from .env file
    load_dotenv()

    # Get API key from environment variables (either system or .env)
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        # Fallback to .env values if not set as system environment variable
        config = dotenv_values()
        api_key = config.get("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file or as an environment variable.")

    return api_key