import pandas as pd


def save_to_csv(df: pd.DataFrame, path: str):
    df.to_csv(path)


def save_report(text: str, path: str):
    with open(path, 'w') as f:
        f.write(text)
