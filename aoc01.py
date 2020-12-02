#!/usr/bin/env python
"""
--- Day 1: Report Repair ---
https://adventofcode.com/2020/day/1

Rank: Removed
"""
from aocutils import read_input, timer

DATA_INPUT = read_input('01', cast='int')


@timer
def part1():
  for i in range(0, len(DATA_INPUT)):
    for j in range(i + 1, len(DATA_INPUT)):
      if DATA_INPUT[i] + DATA_INPUT[j] == 2020:
        return DATA_INPUT[i] * DATA_INPUT[j]


@timer
def part2():
  for i in range(0, len(DATA_INPUT)):
    for j in range(i + 1, len(DATA_INPUT)):
      if DATA_INPUT[i] + DATA_INPUT[j] > 2020:
        continue
      for k in range(j + 1, len(DATA_INPUT)):
        if DATA_INPUT[i] + DATA_INPUT[j] + DATA_INPUT[k] == 2020:
          return DATA_INPUT[i] * DATA_INPUT[j] * DATA_INPUT[k]


if __name__ == "__main__":
  print(part1())
  print(part2())
