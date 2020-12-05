#!/usr/bin/env python
"""
--- Day 5: Binary Boarding ---
https://adventofcode.com/2020/day/5

Rank: 699 / 810
"""
from aocutils import read_input, timer

DATA_INPUT = read_input('05', cast='str')


def calculate_region(lower, upper, lst):
  for x in lst:
    if x == 'lower':
      upper -= (upper - lower + 1) // 2
    else:
      lower += (upper - lower + 1) // 2
  return upper


def get_row(bp):
  return calculate_region(0, 127, ['lower' if c == 'F' else 'upper' for c in bp])


def get_col(bp):
  return calculate_region(0, 7, ['lower' if c == 'L' else 'upper' for c in bp])


def seat_id(bp):
  return get_row(bp[:7]) * 8 + get_col(bp[7:])


@timer
def part1():
  return max(seat_id(p) for p in DATA_INPUT)


@timer
def part2():
  seats = {seat_id(bp) for bp in DATA_INPUT}
  return [s for s in range(min(seats), max(seats) + 1) if s not in seats][0]


if __name__ == "__main__":
  print(part1())
  print(part2())
