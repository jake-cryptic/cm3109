#!/usr/bin/python
import matplotlib.pyplot as plt
from sa import SimulatedAnnealing
from ranking import RankedSet
from wmg import WMG


def plot(x: list, y: list, fig_name: str, plot_title: str):
	plt.figure(fig_name)
	plt.title(plot_title)
	plt.scatter(x, y, s=3)
	plt.ylim(bottom=0)
	plt.xlim(left=0)
	# plt.savefig('figure1.jpg')
	plt.show()
	plt.close()


def run_controlled_simulation(parser: WMG, param_to_change: str, param_value):
	values_dict = {
		'initial_t': 500,
		't_length': 900,
		'max_uphill_moves': 100,
		'cooling_ratio': 0.95
	}

	values_dict[param_to_change] = param_value
	print(f'Running SimulatedAnnealing({values_dict=})')

	sa = SimulatedAnnealing(
		initial_t=values_dict['initial_t'],
		t_length=values_dict['t_length'],
		max_uphill_moves=values_dict['max_uphill_moves'],
		cooling_ratio=values_dict['cooling_ratio']
	)
	sa.set_wmg(parser)
	sa.initialise_rankings()
	sa.run_outer()

	return sa.get_best_ranking().score


def run_tests(parser: WMG) -> None:
	data = {
		'x': [],
		'y': []
	}

	#for test_initial_t in range(100, 3000, 50):
	#	data['x'].append(test_initial_t)
	#	data['y'].append(run_controlled_simulation(parser, 'initial_t', test_initial_t))
	#plot(data['x'], data['y'], 'Kemeny Score', 'Kemeny Score vs Initial Temperature')

	#for test_cooling in range(60, 100):
	#	data['x'].append(test_cooling/100)
	#	data['y'].append(run_controlled_simulation(parser, 'cooling_ratio', test_cooling/100))
	#plot(data['x'], data['y'], 'Kemeny Score', 'Kemeny Score vs Cooling Ratio')

	for test_tl in range(10, 500, 10):
		data['x'].append(test_tl)
		data['y'].append(run_controlled_simulation(parser, 't_length', test_tl))
	plot(data['x'], data['y'], 'Kemeny Score', 'Kemeny Score vs t_length')


def main() -> None:
	parser = WMG()
	parser.read_file('../data/1994_Formula_One.wmg')
	parser.parse_file()

	run_tests(parser)


if __name__ == '__main__':
	main()
