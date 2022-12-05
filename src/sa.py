from math import exp
from time import time, strftime
import logging


class SimulatedAnnealing:

    T: float
    T0: float
    TL: int
    start_time: float
    last_exec_time: float

    def __init__(self, T: float, T0: float, TL: int):
        self.start_time = time()
        self.last_exec_time = time()

        # Temperatures
        self.T = T          # Current temperature
        self.T0 = T0        # Initial temperature
        self.TL = TL        # Temperature length

    def cooling(self, x):
        return x

    def stopping_criteria(self) -> bool:
        return True

    def run_outer(self):
        while self.stopping_criteria():
            self.run_inner()
            self.T = 1

    def run_inner(self):
        uphill_moves = 0
        for i in range(0, self.TL):
            neighbor = 1
            delta_cost = self.cooling(x_best) - self.cooling()

            q = 0.1
            qt = exp(-1 * (delta_cost / self.T))
            if q < qt:
                uphill_moves += 1

    def get_execution_time(self, msg: str) -> None:
        self.last_exec_time = time()
        logging.info(f'{self.last_exec_time-self.start_time} {msg}')
