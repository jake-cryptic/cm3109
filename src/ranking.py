import logging
from random import shuffle
from copy import copy


class RankedSet:

	# Set of driver IDs (IN ORDER)
	_data: list[int]
	score: int

	def __init__(self, data: list[int]):
		logging.debug(f'RankedSet created with {len(data)} IDs: {data}')

		self._data = data
		self.score = 0

	def calculate_score(self):
		tmp_score = 0
		pass

	def get_neighbour(self):
		c = copy(self._data)
		shuffle(c)
		return RankedSet(c)


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(asctime)s - %(message)s')
	rs = RankedSet(list(range(1, 45)))
