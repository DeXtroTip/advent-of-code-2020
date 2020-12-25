#!/usr/bin/env python
"""
--- Day 25: Combo Breaker ---
https://adventofcode.com/2020/day/25

Rank: 2527 / 2070
"""
from aocutils import read_input, timer

DATA_INPUT = read_input('25', cast='int')
CARD, DOOR = DATA_INPUT


def transform(n, subject, loop_size):
  for _ in range(loop_size):
    n = (n * subject) % 20201227
  return n


@timer
def part1():
  ls, n = 1, 1
  while not (n := transform(n, 7, 1)) in (CARD, DOOR):
    ls += 1
  return transform(1, DOOR if n == CARD else CARD, ls)


if __name__ == "__main__":
  print(part1())
