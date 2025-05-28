def check_alerts(df):
    last = df.iloc[-1]
    signals = []

    if last['rsi'] < 30:
        signals.append("RSI < 30 (sobreventa)")
    if last['macd'] > 0:
        signals.append("MACD cruce alcista")
    if last['ema20'] > last['ema50']:
        signals.append("Cruce EMA 20 > EMA 50")
    if last['close'] < last['bb_bbm']:
        signals.append("Precio bajo la media de Bollinger")
    if last['adx'] > 25:
        signals.append("ADX fuerte tendencia")

    if len(signals) >= 3:
        return {
            "activo": True,
            "señales": signals,
            "confianza": "Alta",
            "recomendación": "COMPRA",
        }
    
    return {"activo": False}
