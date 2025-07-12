import pandas as pd
from scipy.signal import argrelextrema


def find_peaks(df: pd.DataFrame, order: int = 5) -> pd.DataFrame:
    """Identify local highs and lows."""
    df = df.copy()
    df['peak'] = 0
    df['trough'] = 0
    idx_max = argrelextrema(df['close'].values, comparator=lambda a, b: a > b, order=order)[0]
    idx_min = argrelextrema(df['close'].values, comparator=lambda a, b: a < b, order=order)[0]
    df.loc[df.index[idx_max], 'peak'] = 1
    df.loc[df.index[idx_min], 'trough'] = 1
    return df
