import pandas as pd
import ta


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Add common technical indicators to the dataframe."""
    df = df.copy()
    df['sma'] = ta.trend.sma_indicator(df['close'])
    df['ema'] = ta.trend.ema_indicator(df['close'])
    df['rsi'] = ta.momentum.rsi(df['close'])
    macd = ta.trend.MACD(df['close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    df['macd_diff'] = macd.macd_diff()
    boll = ta.volatility.BollingerBands(df['close'])
    df['bb_high'] = boll.bollinger_hband()
    df['bb_low'] = boll.bollinger_lband()
    return df
