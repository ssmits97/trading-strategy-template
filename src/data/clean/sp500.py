import datetime

import pandas as pd


def clean_sp500_data(start_date: datetime.datetime, end_date: datetime.datetime) -> None:
	df = pd.read_csv('../data/raw/sp500.csv', parse_dates=['Date'])
	df = df.set_index('Date')
	df = df[(df.index >= start_date) & (df.index < end_date)]
	df.to_csv('../data/clean/sp500.csv')
