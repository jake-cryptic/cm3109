class RankedSet:

	# Set of driver IDs (IN ORDER)
	_data: set[int]

	def __init__(self, data: set[int]):
		self._data = data
		print(data)

	def get_score(self):
		pass
