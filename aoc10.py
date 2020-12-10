#!/usr/bin/env python
"""
--- Day 10: Adapter Array ---
https://adventofcode.com/2020/day/10

Rank: 6451 / 2678
"""
from functools import lru_cache
from queue import Queue

from aocutils import read_input, timer

DATA_INPUT = read_input('10', cast='int')
DATA_INPUT_SET = set(DATA_INPUT)


@lru_cache(maxsize=None)
def calc(c):
  if c == 0:
    return 1
  if c not in DATA_INPUT_SET:
    return 0
  return calc(c - 1) + calc(c - 2) + calc(c - 3)


@timer
def part1():
  m = {1: set(), 2: set(), 3: set()}
  q = Queue()
  q.put(0)
  while not q.empty():
    c = q.get()
    for i in (1, 2, 3):
      if c + i in DATA_INPUT_SET:
        m[i].add(c + i)
        q.put(c + i)
        break
  return len(m[1]) * (len(m[3]) + 1)


@timer
def part2():
  return calc(max(DATA_INPUT))


if __name__ == "__main__":
  print(part1())
  print(part2())
