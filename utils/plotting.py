import pandas as pd
import matplotlib.pyplot as plt


def plot_price_with_indicators(df: pd.DataFrame, ticker: str):
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['close'], label='Close')
    if 'sma' in df:
        plt.plot(df.index, df['sma'], label='SMA')
    if 'ema' in df:
        plt.plot(df.index, df['ema'], label='EMA')
    plt.title(f"{ticker} Price with Indicators")
    plt.legend()
    plt.tight_layout()
    plt.show()
