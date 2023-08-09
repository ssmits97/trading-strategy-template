import dataclasses
import datetime
import json


@dataclasses.dataclass
class Config:
	"""Simple static config."""

	start_date: datetime.datetime | str
	end_date: datetime.datetime | str

	datetime_format: str

	def __post_init__(self):
		self.start_date = self.start_date if isinstance(self.start_date, datetime.datetime) \
							else datetime.datetime.strptime(self.start_date, self.datetime_format)

		self.end_date = self.end_date if isinstance(self.end_date, datetime.datetime) \
							else datetime.datetime.strptime(self.end_date, self.datetime_format)

	@classmethod
	def load_default(cls, path: str = '../data/static/settings.json'):
		with open(path, 'r') as f:
			config = json.load(f)
		return cls(**config)


default_config = Config.load_default()
