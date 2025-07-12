import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam


def prepare_sequences(df: pd.DataFrame, window: int = 10):
    df = df.dropna()
    values = df.values
    X, y = [], []
    for i in range(len(values) - window - 1):
        X.append(values[i:(i + window), :])
        y.append(1 if values[i + window, df.columns.get_loc('close')] > values[i + window - 1, df.columns.get_loc('close')] else 0)
    return np.array(X), np.array(y)


def build_model(input_shape):
    model = Sequential([
        LSTM(64, input_shape=input_shape),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=Adam(0.001), loss='binary_crossentropy', metrics=['accuracy'])
    return model
