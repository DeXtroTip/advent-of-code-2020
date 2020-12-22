#!/usr/bin/env python
"""
--- Day 6: Custom Customs ---
https://adventofcode.com/2020/day/6

Rank: 983 / 1471
"""
from aocutils import *

DATA_INPUT = read_input('06', cast='str')


@timer
def part1():
  DATA_INPUT.append('')
  total = 0
  tmp = set()
  for line in DATA_INPUT:
    if len(line) == 0:
      total += len(tmp)
      tmp = set()
      continue
    tmp = tmp | set(c for c in line)
  return total


@timer
def part2():
  DATA_INPUT.append('')
  total = 0
  tmp = set()
  is_first = True
  for line in DATA_INPUT:
    if len(line) == 0:
      total += len(tmp)
      tmp = set()
      is_first = True
      continue
    if is_first:
      tmp = set(c for c in line)
    else:
      tmp = tmp.intersection(set(c for c in line))
    is_first = False
  return total


if __name__ == "__main__":
  print(part1())
  print(part2())
