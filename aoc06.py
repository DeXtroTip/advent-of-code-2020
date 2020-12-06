#!/usr/bin/env python
"""
--- Day 6: Custom Customs ---
https://adventofcode.com/2020/day/6

Rank: 983 / 1471
"""
from functools import reduce

from aocutils import read_input, timer


def parse_input(lines):
  groups = []
  current_group = []
  for line in lines:
    if not len(line):
      groups.append(current_group)
      current_group = []
    else:
      current_group.append(line)
  return groups


DATA_INPUT = read_input('06', cast='str')
if len(DATA_INPUT[-1]):
  DATA_INPUT.append('')
DATA_INPUT = parse_input(DATA_INPUT)


@timer
def part1():
  return sum(len(reduce(lambda x, y: x | y, (set(a for a in answers) for answers in group))) for group in DATA_INPUT)


@timer
def part2():
  return sum(len(reduce(lambda x, y: x & y, (set(a for a in answers) for answers in group))) for group in DATA_INPUT)


if __name__ == "__main__":
  print(part1())
  print(part2())
