import logging


class RankedSet:

	# Set of driver IDs (IN ORDER)
	_data: set[int]
	_score: int

	def __init__(self, data: set[int]):
		logging.debug(f'RankedSet created with {len(data)} IDs: {data}')

		self._data = data
		self._score = 0

	def calculate_score(self):
		tmp_score = 0
		pass


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(asctime)s - %(message)s')
	rs = RankedSet(set(range(1, 45)))
