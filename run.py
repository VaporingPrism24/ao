import pandas as pd
from utils.data_loader import download_ohlcv
from analysis.indicators import add_indicators
from analysis.peaks import find_peaks
from models.random_forest import prepare_dataset, train_random_forest, evaluate_model
from utils.exporter import save_to_csv, save_report
from utils.plotting import plot_price_with_indicators


def main():
    ticker = 'BTC-USD'
    data = download_ohlcv(ticker, start='2020-01-01', end='2021-01-01')
    data = add_indicators(data)
    data = find_peaks(data)
    X_train, X_test, y_train, y_test = prepare_dataset(data)
    model = train_random_forest(X_train, y_train)
    report = evaluate_model(model, X_test, y_test)
    print(report)
    save_report(report, 'reports/random_forest_report.txt')
    save_to_csv(data, 'reports/processed_data.csv')
    plot_price_with_indicators(data, ticker)


if __name__ == '__main__':
    main()
