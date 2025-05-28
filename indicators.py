import pandas as pd
import pandas_ta as ta

def process_klines(klines):
    df = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'trades',
        'taker_base_volume', 'taker_quote_volume', 'ignore'
    ])
    df['close'] = df['close'].astype(float)
    df['open'] = df['open'].astype(float)
    df['high'] = df['high'].astype(float)
    df['low'] = df['low'].astype(float)
    df['volume'] = df['volume'].astype(float)

    df['rsi'] = ta.rsi(df['close'])
    df['macd'] = ta.macd(df['close'])['MACD_12_26_9']
    df['ema20'] = ta.ema(df['close'], length=20)
    df['ema50'] = ta.ema(df['close'], length=50)
    df['adx'] = ta.adx(df['high'], df['low'], df['close'])['ADX_14']
    df['bb_bbm'] = ta.bbands(df['close'])['BBM_20_2.0']
    
    return df

