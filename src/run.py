#!/usr/bin/python3
from sa import SimulatedAnnealing
from wmg import WMG
import logging


def main():
	parser = WMG()
	parser.read_file('../data/1994_Formula_One.wmg')
	parser.parse_file()

	sa = SimulatedAnnealing(
		initial_t=100,
		t_length=100,
		max_iterations=100,
		cooling_ratio=0.98
	)
	sa.set_wmg(parser)
	sa.run_outer()
	sa.get_execution_time(f'End of testing, best score was: {sa.get_best_ranking().score}')


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(asctime)s - %(message)s')
	main()
