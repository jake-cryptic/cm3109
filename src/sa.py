from copy import copy
from math import exp
from time import time
from random import random
from ranking import RankedSet
from wmg import WMG
import logging


class SimulatedAnnealing:
	# Air conditioning
	current_t: float
	initial_t: float
	t_length: int
	max_uphill_moves: int
	uphill_moves: int
	cooling_ratio: float

	# Timing variables
	start_time: float
	last_exec_time: float

	# Data set
	_wmg: WMG
	_ranking_initial: RankedSet
	_ranking_current: RankedSet
	_ranking_best: RankedSet

	def __init__(self, initial_t: float, t_length: int, max_uphill_moves: int, cooling_ratio: float):
		self.start_time = time()
		self.last_exec_time = time()

		# Temperatures
		self.current_t = initial_t  # Current temperature
		self.initial_t = initial_t  # Initial temperature
		self.t_length = t_length  # Temperature length

		self.max_uphill_moves = max_uphill_moves  # Maximum uphill moves
		self.uphill_moves = 0  	# Uphill moves reset to 0
		self.cooling_ratio = cooling_ratio  # Change of the thermostat
		logging.info(f'Running SimulatedAnnealing with parameters:\n\t- initial_t = {initial_t}\n\t- t_length = {t_length}\n\t- max_uphill_moves = {max_uphill_moves}\n\t- cooling_ratio = {cooling_ratio}')

	def set_wmg(self, wmg: WMG) -> None:
		self._wmg = wmg

	def initialise_rankings(self, id_list: list = []) -> None:
		if not id_list:
			id_list = self._wmg.participant_id_list

		self._ranking_initial = \
			self._ranking_current = \
			self._ranking_best = RankedSet(id_list, self._wmg.participant_matrix)

	def update_temperature(self) -> None:
		self.current_t *= self.cooling_ratio

	def run_outer(self) -> None:
		# Stopping criterion
		while self.uphill_moves < self.max_uphill_moves:
			logging.debug(f'Outer loop iteration {self.uphill_moves} / {self.max_uphill_moves}')

			# Function to run the inner loop
			self.run_inner()

			# This function sets the new temperature based on the cooling ratio
			self.update_temperature()

	def run_inner(self) -> None:
		for i in range(self.t_length):
			# If we have reached max number of uphill moves break out of loop
			if self.uphill_moves >= self.max_uphill_moves:
				break

			# Generate a neighbouring solution to check
			new_ranking = self._ranking_current.get_neighbour()

			# Compute the change of the cost
			delta_cost = new_ranking.score - self._ranking_current.score

			if delta_cost <= 0:
				# If this neighbour has the same or better score, move to it
				self._ranking_current = copy(new_ranking)

				# If new ranking has a better score than the best... then it is the best
				if new_ranking.score < self._ranking_best.score:
					self._ranking_best = copy(new_ranking)
			else:
				# In this case, the score of the newly tested neighbour is worse than the current
				# e ^ (-delta_cost / current_temperature)
				change_pb = exp(-1 * delta_cost / self.current_t)

				# Random decimal between 0 and 1
				q = random()

				# Uphill move
				if q < change_pb:
					self._ranking_current = copy(new_ranking)
					self.uphill_moves += 1
					logging.debug(f'Uphill move counter: {self.uphill_moves} / {self.max_uphill_moves}')

	def get_execution_time(self, msg: str) -> str:
		self.last_exec_time = time()
		return f'{round(self.last_exec_time - self.start_time, 5)}s execution time. {msg}'

	def get_best_ranking(self) -> RankedSet:
		return self._ranking_best


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(asctime)s - %(message)s')
	sa = SimulatedAnnealing(100, 10, 10, 0.95)
	sa.run_outer()
	sa.get_execution_time('End of testing')
