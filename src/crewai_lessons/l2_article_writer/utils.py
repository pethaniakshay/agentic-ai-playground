import os
from dotenv import load_dotenv, dotenv_values

def get_openai_api_key():
    import os
from dotenv import load_dotenv, dotenv_values

def get_openai_api_key():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get API key from environment variables (either system or .env)
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        # Fallback to .env values if not set as system environment variable
        config = dotenv_values()
        api_key = config.get("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file or as an environment variable.")
        
    return api_key