import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.groq.com/openai/v1"

MODEL_NAME = "llama-3.3-70b-versatile"


def get_api_key() -> str | None:
    load_dotenv()
    value = os.getenv("GROQ_API_KEY")
    return value.strip() if value else None