import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Hello from anime-recommendation-ai!")
    
    token = os.getenv("OPENAI_API_KEY")
    endpoint = "https://models.github.ai/inference"
    model = "openai/gpt-4.1"
    client = OpenAI(
        base_url=endpoint,
        api_key=token,
    )
    
    user_message = input("You: ")

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message
            },
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
