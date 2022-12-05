#!/usr/bin/python3
from sa import SimulatedAnnealing
from wmg import WMG
import logging


class CM3109Runner:

    parser: WMG

    def __init__(self):
        self.parser = WMG()
        self.parser.read_file('data/1994_Formula_One.wmg')
        self.parser.parse_file()

    def run(self) -> None:
        simu = SimulatedAnnealing(1.0, 1.0, 3)
        pass


if __name__ == '__main__':
    runner = CM3109Runner()
    runner.run()
