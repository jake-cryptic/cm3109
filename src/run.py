#!/usr/bin/python3
from sa import SimulatedAnnealing
from ranking import RankedSet
from wmg import WMG
from sys import argv
import logging


def print_rankings(ranked_set: RankedSet, parser: WMG) -> None:
	ids = ranked_set.get_rankings()

	text_out = 'Rank\t|\tDriver Name\n'
	for i, driver_id in enumerate(ids):
		text_out += f'\t{i+1}\t|\t{parser.participants[driver_id]}\n'

	print(text_out)


def main() -> None:
	file_to_load = '../data/1994_Formula_One.wmg'

	if len(argv) > 1:
		file_to_load = argv[1]
		logging.info(f'Will try to load data from specified file: {file_to_load}')

	parser = WMG()
	parser.read_file(file_to_load)
	parser.parse_file()

	if not parser.file_loaded:
		exit(1)

	sa = SimulatedAnnealing(
		initial_t=8,
		t_length=50,
		num_non_improve=50,
		cooling_ratio=0.99
	)
	sa.set_wmg(parser)
	sa.initialise_rankings()
	sa.run_outer()

	print(sa.get_execution_time(f'End of testing'))
	print_rankings(sa.get_best_ranking(), parser)
	print(f'Best score was: {sa.get_best_ranking().score}')


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(asctime)s - %(message)s')
	main()
