#!/usr/bin/env python
"""
--- Day 9: Encoding Error ---
https://adventofcode.com/2020/day/9

Rank: 1025 / 823
"""
import functools
import json
import re

from aocutils import *

DATA_INPUT = read_input('09', cast='int')
# DATA_INPUT = read_input_split_first_line('09', cast='str')
# DATA_INPUT = read_input('09t', cast='int')
# DATA_INPUT = read_input_split_first_line('09t', cast='str')


def is_valid_sum(n, lst):
  for x in lst:
    for y in lst:
      if x + y == n and x != y:
        return True
  return False


@timer
def part1():
  total = 0
  lst = []
  d = {}
  s = set()
  for i, n in enumerate(DATA_INPUT):
    if i < 25:
      lst.append(n)
      continue
    # print(lst)
    if not is_valid_sum(n, lst):
      return n
    lst = lst[1:] + [n]
  return


@timer
def part2():
  lst = []
  g = -1
  for i, n in enumerate(DATA_INPUT):
    if i < 25:
      lst.append(n)
      continue
    if not is_valid_sum(n, lst):
      g = n
      break
    lst = lst[1:] + [n]

  # print(g)
  for i, n in enumerate(DATA_INPUT):
    j = i
    x = 0
    tmp = []
    while x < g:
      # print(tmp)
      tmp.append(DATA_INPUT[j])
      x += DATA_INPUT[j]
      j += 1
    # print()
    if x == g:
      return (min(tmp), max(tmp), min(tmp) + max(tmp))

  return


if __name__ == "__main__":
  print(part1())
  print(part2())
