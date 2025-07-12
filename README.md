# Crypto Analysis Toolkit

This repository provides a modular Python toolkit for downloading cryptocurrency data, computing technical indicators, and applying machine learning models to forecast price direction.

## Features

- **Data Download**: fetch OHLCV data with `yfinance`.
- **Technical Indicators**: compute SMA, EMA, RSI, MACD and Bollinger Bands.
- **Peak Detection**: identify local highs and lows in the price series.
- **Machine Learning Models**: Random Forest and LSTM examples for forecasting.
- **Reports**: save processed data and model evaluations to the `reports` folder.
- **Visualization**: quick plots of price series with indicators.

## Installation

```bash
pip install -r requirements.txt
```

This project is compatible with local environments and Google Colab.

## Usage

```bash
python run.py
```

The script downloads BTC-USD data from 2020, computes indicators, trains a Random Forest classifier and saves results in the `reports` directory.

## Project Structure

- `data/`: data handling utilities (future expansion).
- `analysis/`: indicator calculations and peak detection.
- `models/`: machine learning models (Random Forest, LSTM).
- `utils/`: helper functions such as plotting and exporting.
- `reports/`: generated CSV files and model reports.

## Future Work

- Sentiment analysis integration from news and social media.
- Automatic daily update task for fresh forecasts.
