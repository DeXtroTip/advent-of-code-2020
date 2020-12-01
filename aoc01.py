#!/usr/bin/env python
"""
--- Day 1: Report Repair ---
https://adventofcode.com/2020/day/1

Rank: 60 / 50
"""
from aocutils import read_input, timer

data_input = read_input('01', cast='int')


@timer
def part1():
  for i in range(0, len(data_input)):
    for j in range(i + 1, len(data_input)):
      if data_input[i] + data_input[j] == 2020:
        return data_input[i] * data_input[j]


@timer
def part2():
  for i in range(0, len(data_input)):
    for j in range(i + 1, len(data_input)):
      if data_input[i] + data_input[j] > 2020:
        continue
      for k in range(j + 1, len(data_input)):
        if data_input[i] + data_input[j] + data_input[k] == 2020:
          return data_input[i] * data_input[j] * data_input[k]


if __name__ == "__main__":
  print(part1())
  print(part2())
