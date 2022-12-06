#!/usr/bin/python3
from sa import SimulatedAnnealing
from wmg import WMG
import logging


def main():
	parser = WMG()
	parser.read_file('../data/1994_Formula_One.wmg')
	parser.parse_file()

	m = parser.create_matrix()
	m.display()


if __name__ == '__main__':
	main()
