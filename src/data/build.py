"""You should only run the code in ./raw, ./clean ./features for debug purposes.
Running this file should be enough to build your entire dataset."""

from config import default_config

from data.clean.sp500 import clean_sp500_data
from data.features.sp500 import get_sp500_basics
from data.raw.sp500 import store_sp500_data

if __name__ == '__main__':
	config = default_config

	# Get the raw data
	# store_sp500_data()
	#
	# # clean the data
	# clean_sp500_data(config.start_date, config.end_date)

	# Build Features
	get_sp500_basics()
