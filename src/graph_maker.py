#!/usr/bin/python
import matplotlib as plt
from sa import SimulatedAnnealing
from ranking import RankedSet
from wmg import WMG


def run_tests(parser: WMG) -> None:
	pass


def main() -> None:
	parser = WMG()
	parser.read_file('../data/1994_Formula_One.wmg')
	parser.parse_file()

	run_tests(parser)


if __name__ == '__main__':
	main()
