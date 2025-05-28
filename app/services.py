import os
import openai
from dotenv import load_dotenv
import requests

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_market():
    # Ejemplo simple que devuelve texto de GPT
    prompt = "Haz un análisis técnico de BTCUSDT con RSI, MACD y volumen."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"analysis": response['choices'][0]['message']['content']}
