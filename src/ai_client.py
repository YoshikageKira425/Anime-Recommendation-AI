import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("OPENAI_API_KEY")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def send_to_ai(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                },
            ],
            temperature=1.0,
            model=model
        )

        return response.choices[0].message.content
    except Exception as e:
        return "Sorry, I couldn't get a recommendation right now."
