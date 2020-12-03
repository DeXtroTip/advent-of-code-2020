#!/usr/bin/env python
"""
--- Day 3: Toboggan Trajectory ---
https://adventofcode.com/2020/day/3

Rank: 4949 / 4113
"""
from functools import reduce

from aocutils import read_input, timer

DATA_INPUT = read_input('03', cast='str')


@timer
def part1():
  return sum(line[(i * 3) % len(line)] == '#' for i, line in enumerate(DATA_INPUT))


@timer
def part2():
  return reduce(lambda x, y: x * y, [
    sum(DATA_INPUT[j][(i * slope[0]) % len(DATA_INPUT[j])] == '#'
        for i, j in enumerate(range(0, len(DATA_INPUT), slope[1])))
    for slope in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
  ])


if __name__ == "__main__":
  print(part1())
  print(part2())
