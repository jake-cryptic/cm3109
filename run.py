#!/usr/bin/python3
from wmg import WMG
from math import exp
import logging


def simulated_annealing(e: float, t: float) -> float:
    return exp(-1 * (e / t))


class CM3109Runner:

    parser: WMG

    def __init__(self):
        self.parser = WMG()
        self.parser.read_file('1994_Formula_One.wmg')
        self.parser.parse_file()

    def run(self) -> None:
        pass


if __name__ == '__main__':
    runner = CM3109Runner()
    runner.run()
