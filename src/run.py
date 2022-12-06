#!/usr/bin/python3
from sa import SimulatedAnnealing
from wmg import WMG
import logging


def main():
	parser = WMG()
	parser.read_file('../data/1994_Formula_One.wmg')
	parser.parse_file()

	sa = SimulatedAnnealing(100, 10, 10, 0.95)
	sa.set_wmg(parser)
	sa.run_outer()


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(asctime)s - %(message)s')
	main()
