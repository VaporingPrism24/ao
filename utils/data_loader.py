import yfinance as yf
import pandas as pd


def download_ohlcv(ticker: str, start: str, end: str, interval: str = "1d") -> pd.DataFrame:
    """Download OHLCV data for a given ticker."""
    data = yf.download(ticker, start=start, end=end, interval=interval)
    data = data.rename(columns=str.lower)
    data.index = pd.to_datetime(data.index)
    return data
