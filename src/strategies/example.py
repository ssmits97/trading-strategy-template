import dataclasses
from collections import Callable

from sklearn.model_selection import GridSearchCV


@dataclasses.dataclass
class Strategy:
	"""Some example strategy you can use for backtesting"""
	param_1: int
	param_2: float
	param_3: str

	model: Callable

	def score(self) -> float:
		return self.model(self.param_1, self.param_2, self.param_3)


if __name__ == '__main__':
	param_1_opts = [1, 2, 3]
	param_2_opts = [0.01, 0.05, 0.1]
	param_3_opts = ['gini', 'entropy']

	param_grid = {'param_1': param_1_opts, 'param_2': param_2_opts, 'param_3': param_3_opts}
	grid_search = GridSearchCV(Strategy, param_grid)
