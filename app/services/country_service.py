from openai import OpenAI
from app.core.config import settings

class CountryService:
    def __init__(self):
        self.client = OpenAI(
            base_url=settings.OPENROUTER_BASE_URL,
            api_key=settings.OPENROUTER_API_KEY
        )

    def get_capital(self, country: str) -> str:
        """
        Fetches the capital of a given country using the recommendation engine (LLM).
        """
        try:
            response = self.client.chat.completions.create(
                model=settings.MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": f"What is the capital of {country}? Give only the capital name."
                    }
                ]
            )
            capital = response.choices[0].message.content
            return capital.strip()
        except Exception as e:
            raise Exception(f"Error fetching capital: {str(e)}")

# Singleton instance for easy reuse
country_service = CountryService()
