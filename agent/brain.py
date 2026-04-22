import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Cargamos .env si existe
load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def ask_ai(prompt, model="claude-3-sonnet-20240229"):
    try:
        response = client.messages.create(
            model=model,
            max_tokens=1200,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        return f"Error connecting to AI: {str(e)}"
