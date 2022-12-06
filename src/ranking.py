import logging
from random import shuffle
from copy import copy


class RankedSet:

	# Set of driver IDs (IN ORDER)
	_data: list[int]
	_relations: list[list[int]]
	score: int

	def __init__(self, data: list[int], relations: list[list[int]]):
		logging.debug(f'RankedSet created with {len(data)} IDs: {data}')

		self._data = data
		self._total_participants = len(self._data)
		self._relations = relations

		self.score = 0
		self.calculate_score()

	def calculate_score(self):
		tmp_score = 0
		for i, driver in enumerate(self._data):
			#print(i, driver)
			for j in range(i, self._total_participants):
				#print(i, j, driver, self._data[j])
				score = 0
				# TODO: Improve this horribly inefficient search
				for k in self._relations:
					if (i == k[0] and j == k[1]) or (j == k[0] and i == k[1]):
						score = k[2]
				if score > 0:
					tmp_score += abs(score)

		self.score = tmp_score

	def get_neighbour(self):
		c = copy(self._data)
		shuffle(c)
		return RankedSet(c, self._relations)


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(asctime)s - %(message)s')
	rs = RankedSet(list(range(1, 45)))
