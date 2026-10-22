from openai import OpenAI
from config import BASE_URL, MODEL_NAME, get_api_key


def _client() -> OpenAI:
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not configured. Add it to ai-agent_1/.env "
            "and restart Streamlit."
        )

    return OpenAI(
        api_key=api_key,
        base_url=BASE_URL,
    )

def chat(messages: list) -> str:
    response = _client().chat.completions.create(
        model = MODEL_NAME,
        messages = messages,
        temperature = 0
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello, My name is Yashvant giri ?"
        }
    ]

    response = chat(messages)
    print(response)