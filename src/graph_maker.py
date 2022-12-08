#!/usr/bin/python
import matplotlib.pyplot as plt
from sa import SimulatedAnnealing
from ranking import RankedSet
from wmg import WMG


def plot(x: list, y: list, fig_name: str, plot_title: str, xlab:str, ylab: str):
	plt.figure(fig_name)
	plt.title(plot_title)
	plt.scatter(x, y, s=3)
	plt.ylim(bottom=0)
	plt.xlim(left=0)
	plt.xlabel(xlab)
	plt.ylabel(ylab)
	# plt.savefig('figure1.jpg')
	plt.show()
	plt.close()


def run_controlled_simulation(parser: WMG, param_to_change: str, param_value):
	values_dict = {
		'initial_t': 4,
		't_length': 120,
		'num_non_improve': 125,
		'cooling_ratio': 0.95
	}

	values_dict[param_to_change] = param_value
	print(f'Running SimulatedAnnealing({values_dict=})')

	sa = SimulatedAnnealing(
		initial_t=values_dict['initial_t'],
		t_length=values_dict['t_length'],
		num_non_improve=values_dict['num_non_improve'],
		cooling_ratio=values_dict['cooling_ratio']
	)
	sa.set_wmg(parser)
	sa.initialise_rankings()
	sa.run_outer()

	return sa.get_best_ranking().score, sa.return_exec_time_ms()


def run_tests(parser: WMG) -> None:
	data = {
		'x': [],
		'x1': [],
		'y': [],
		'y1': []
	}

	if False:
		for test_it in range(4, 250, 1):
			data['x'].append(test_it)
			result = run_controlled_simulation(parser, 'initial_t', test_it)
			data['y'].append(result[0])
			data['y1'].append(result[1])
		plot(data['x'], data['y'], 'Kemeny Score', 'Initial Temperature vs Kemeny Score', 'Initial Temperature', 'Kemeny Score')
		plot(data['x'], data['y1'], 'Kemeny Score', 'Initial Temperature vs time (ms)', 'Initial Temperature', 'time (ms)')

	if False:
		for test_cooling in range(50, 100, 1):
			data['x'].append(test_cooling/100)
			result = run_controlled_simulation(parser, 'cooling_ratio', test_cooling/100)
			data['y'].append(result[0])
			data['y1'].append(result[1])
		plot(data['x'], data['y'], 'Kemeny Score', 'Cooling Ratio vs Kemeny Score', 'Cooling Ratio', 'Kemeny Score')
		plot(data['x'], data['y1'], 'Kemeny Score', 'Cooling Ratio vs time (ms)', 'Cooling Ratio', 'time (ms)')

	if False:
		for test_tl in range(1, 125, 5):
			data['x'].append(test_tl)
			result = run_controlled_simulation(parser, 't_length', test_tl)
			data['y'].append(result[0])
			data['y1'].append(result[1])
		plot(data['x'], data['y'], 'Kemeny Score', 'TL vs Kemeny Score', 'TL', 'Kemeny Score')
		plot(data['x'], data['y1'], 'Kemeny Score', 'TL vs time (ms)', 'TL', 'time (ms)')

	if False:
		for test_nni in range(1, 125, 1):
			data['x'].append(test_nni)
			result = run_controlled_simulation(parser, 'num_non_improve', test_nni)
			data['y'].append(result[0])
			data['y1'].append(result[1])
		plot(data['x'], data['y'], 'Kemeny Score', 'num_non_improve vs Kemeny Score', 'num_non_improve', 'Kemeny Score')
		plot(data['x'], data['y1'], 'Kemeny Score', 'num_non_improve vs time (ms)', 'num_non_improve', 'time (ms)')


def main() -> None:
	parser = WMG()
	parser.read_file('../data/1994_Formula_One.wmg')
	parser.parse_file()

	run_tests(parser)


if __name__ == '__main__':
	main()
