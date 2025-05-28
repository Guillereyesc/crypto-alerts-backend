from fastapi import FastAPI
from binance import get_klines
from indicators import process_klines
from alerts import check_alerts
from gpt import generar_analisis
import os

app = FastAPI()

@app.get("/analisis")
def analizar():
    symbol = os.getenv("SYMBOL", "BTCUSDT")
    klines = get_klines(symbol, "5m")
    df = process_klines(klines)
    alerta = check_alerts(df)

    if alerta["activo"]:
        gpt_response = generar_analisis(alerta["señales"])
        return {
            "symbol": symbol,
            "alerta": alerta,
            "gpt": gpt_response
        }

    return {"alerta": "Sin señales relevantes"}
