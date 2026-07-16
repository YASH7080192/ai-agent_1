from openai import OpenAI
from config import API_KEY, BASE_URL, MODEL_NAME

client = OpenAI(
    api_key = API_KEY,
    base_url = BASE_URL,
)

def chat(messages: list) -> str:
    response = client.chat.completions.create(
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