from math import exp
from time import time, strftime
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

    def __init__(self, initial_t: float, t_length: int, max_iterations: int, cooling_ratio: float):
        self.start_time = time()
        self.last_exec_time = time()

        # Temperatures
        self.current_t = initial_t              # Current temperature
        self.initial_t = initial_t              # Initial temperature
        self.t_length = t_length                # Temperature length

        self.max_iterations = max_iterations    # Maximum iterations of outer loop
        self.cooling_ratio = cooling_ratio      # Change of the thermostat <-- another joke

    def cooling(self, x):
        return x

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
            #neighbor = 1
            #delta_cost = self.cooling(x_best) - self.cooling()

            q = 0.1
            #qt = exp(-1 * (delta_cost / self.T))
            #if q < qt:
            #    uphill_moves += 1

    def get_execution_time(self, msg: str) -> None:
        self.last_exec_time = time()
        logging.info(f'{self.last_exec_time-self.start_time} {msg}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(asctime)s - %(message)s')
    sa = SimulatedAnnealing(100, 10, 10, 0.95)
    sa.run_outer()
