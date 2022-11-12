class WMG:

	total_participants: int
	participants: dict
	participant_relations: dict
	data_line: str

	file_lines: list

	def __init__(self):
		self.file_lines = []

	def read_file(self, file_name):
		with open(file_name) as f:
			l = f.readline()
			while l != '':
				self.file_lines.append(l.strip())
				l = f.readline()

	def parse_file(self):
		self.total_participants = int(self.file_lines[0])
		self.data_line = str(self.file_lines[self.total_participants + 1])

		# Parse participant list
		for i in range(1, self.total_participants + 1):
			print(f'Participant: {self.file_lines[i]}')

		# Parse participant relations
		for i in range(self.total_participants, len(self.file_lines)):
			print(f'Relation: {self.file_lines[i]}')



if __name__ == '__main__':
	w = WMG()
	w.read_file('1994_Formula_One.wmg')
	w.parse_file()
