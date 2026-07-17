import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

BASE_URL = "https://api.groq.com/openai/v1"

MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct"