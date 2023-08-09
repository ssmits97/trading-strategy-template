import numpy as np
import pandas as pd


def get_sp500_basics() -> None:
	df = pd.read_csv('../data/clean/sp500.csv', index_col=0)
	df['returns'] = df['SP500'].pct_change()
	df['logs'] = np.log(df['SP500'])
	df = df[['returns', 'logs', 'Consumer Price Index', 'Long Interest Rate']]
	df.to_csv('../data/features/sp500_basics.csv')
