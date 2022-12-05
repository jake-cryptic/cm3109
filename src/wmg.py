import logging
from os.path import isfile
from matrix import Matrix


class WMG:

	total_participants: int
	participants: dict
	participant_relations: list
	data_line: str

	file_lines: list
	file_loaded: bool

	def __init__(self):
		self.file_loaded = False
		self.file_lines = []
		self.participants = {}
		self.participant_relations = []

	def read_file(self, file_name: str) -> None:
		if not isfile(file_name):
			logging.error(f'Could not find file: {file_name}')
			return

		with open(file_name) as f:
			line = f.readline()
			while line != '':
				self.file_lines.append(line.strip())
				line = f.readline()

			self.file_loaded = True

	def parse_file(self) -> None:
		if not self.file_loaded:
			logging.error(f'Attempted to call parse_file() before file loaded!')
			return

		self.total_participants = int(self.file_lines[0])
		self.data_line = str(self.file_lines[self.total_participants + 1])

		# Parse participant list
		for i in range(1, self.total_participants + 1):
			logging.debug(f'Participant: {self.file_lines[i]}')
			participant = self.file_lines[i].split(',')
			self.participants[participant[0]] = participant[1]

		# Parse participant relations
		for i in range(self.total_participants + 2, len(self.file_lines)):
			logging.debug(f'Relation: {self.file_lines[i]}')
			relation = self.file_lines[i].split(',')
			self.participant_relations.append(relation)

		logging.debug(self.participants)
		logging.debug(self.participant_relations)

	def create_matrix(self) -> Matrix:
		m = Matrix(self.total_participants, self.total_participants)

		for relation in self.participant_relations:
			m.write(int(relation[0])-1, int(relation[1])-1, int(relation[2]))

		return m


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(asctime)s - %(message)s')

	# To test the class
	w = WMG()
	w.read_file('data/1994_Formula_One.wmg')
	w.parse_file()
