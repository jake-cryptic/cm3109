#!/usr/bin/python3
from sa import SimulatedAnnealing
from ranking import RankedSet
from wmg import WMG
import logging


def print_rankings(ranked_set: RankedSet, parser: WMG) -> None:
	ids = ranked_set.get_rankings()

	text_out = 'Rank\t|\tDriver Name\n'
	for i, driver_id in enumerate(ids):
		text_out += f'\t{i+1}\t|\t{parser.participants[driver_id]}\n'

	print(text_out)


def main() -> None:
	parser = WMG()
	parser.read_file('../data/1994_Formula_One.wmg')
	parser.parse_file()

	sa = SimulatedAnnealing(
		initial_t=100,
		t_length=100,
		max_iterations=50,
		cooling_ratio=0.95
	)
	sa.set_wmg(parser)
	sa.initialise_rankings()
	sa.run_outer()
	sa.get_execution_time(f'End of testing, best score was: {sa.get_best_ranking().score}')

	print_rankings(sa.get_best_ranking(), parser)


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(asctime)s - %(message)s')
	main()
