from math import exp
from time import time, strftime
from random import random
from ranking import RankedSet
from wmg import WMG
import logging


class SimulatedAnnealing:
	# Air conditioning <--- this is a joke
	current_t: float
	initial_t: float
	t_length: int
	max_iterations: int
	cooling_ratio: float

	# Timing variables
	start_time: float
	last_exec_time: float

	# Data set
	_wmg: WMG
	_ranking_initial: RankedSet
	_ranking_current: RankedSet
	_ranking_best: RankedSet

	def __init__(self, initial_t: float, t_length: int, max_iterations: int, cooling_ratio: float):
		self.start_time = time()
		self.last_exec_time = time()

		# Temperatures
		self.current_t = initial_t  # Current temperature
		self.initial_t = initial_t  # Initial temperature
		self.t_length = t_length  # Temperature length

		self.max_iterations = max_iterations  # Maximum iterations of outer loop
		self.cooling_ratio = cooling_ratio  # Change of the thermostat <-- another joke

	def set_wmg(self, wmg) -> None:
		self._wmg = wmg
		self._set_ranking_variables()

	def _set_ranking_variables(self):
		self._ranking_initial = \
			self._ranking_current = \
			self._ranking_best = RankedSet(self._wmg.participant_id_set)

	def update_temperature(self) -> None:
		self.current_t *= self.cooling_ratio

	def run_outer(self) -> None:
		# Stopping criterion
		for i in range(self.max_iterations):
			logging.debug(f'Outer loop iteration {i} / {self.max_iterations}')
			self.run_inner()
			self.update_temperature()

	def run_inner(self) -> None:
		uphill_moves = 0

		for i in range(self.t_length):
			logging.debug(f'\t- Inner loop iteration {i} / {self.t_length}')
			# new_ranking =
			delta_cost = 0
			if delta_cost > 0:
				change_pb = exp(-1 * delta_cost / self.current_t)
				if change_pb > random():
					uphill_moves += 1
			else:
				pass

	def get_execution_time(self, msg: str) -> None:
		self.last_exec_time = time()
		logging.info(f'{self.last_exec_time - self.start_time} {msg}')


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(asctime)s - %(message)s')
	sa = SimulatedAnnealing(100, 10, 10, 0.95)
	sa.run_outer()
	sa.get_execution_time('End of testing')
