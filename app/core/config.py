import os
from pathlib import Path
from dotenv import load_dotenv

# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_path = BASE_DIR / '.env'

# Explicitly load .env from the root
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = "Country Capital API"
    OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"
    MODEL_NAME: str = "openai/gpt-oss-120b:free"

    def validate(self):
        if not self.OPENROUTER_API_KEY:
            print("WARNING: OPENROUTER_API_KEY is not set!")
        elif not self.OPENROUTER_API_KEY.startswith("sk-or-"):
            print("WARNING: OPENROUTER_API_KEY does not start with 'sk-or-'")
        else:
            print(f"API Key loaded successfully (starts with {self.OPENROUTER_API_KEY[:10]}...)")

settings = Settings()
settings.validate()
