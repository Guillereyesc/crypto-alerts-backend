import requests
import os

BASE_URL = os.getenv("BINANCE_API_BASE", "https://api.binance.com")

def get_klines(symbol: str, interval: str, limit: int = 100):
    url = f"{BASE_URL}/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    response = requests.get(url, params=params)
    return response.json()
