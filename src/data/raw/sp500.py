import requests

datahub_host = 'https://datahub.io'


def store_sp500_data(**kwargs) -> None:
	"""The .csv request is from https://datahub.io/core/s-and-p-500"""

	response = requests.get(datahub_host + '/core/s-and-p-500/r/data.csv', params=kwargs)
	response.raise_for_status()
	with open('../data/raw/sp500.csv', 'w') as f:
		f.write(response.text)
