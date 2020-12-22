#!/usr/bin/env python
"""
--- Day 13: Shuttle Search ---
https://adventofcode.com/2020/day/13

Rank: 2576 / 8758
"""
import functools
import json
import re
from queue import Queue

from aocutils import *

DATA_INPUT = read_input('13', cast='str')
# DATA_INPUT = read_input('13t', cast='str')


def parse_input(line):
  return [int(n) for n in line.split(',') if n.isdigit()]


def parse_input2(line):
  return [int(n) if n.isdigit() else None for n in line.split(',')]


@timer
def part1():
  bus = int(DATA_INPUT[0])
  data = sorted(parse_input(DATA_INPUT[1]))
  i = 1
  checks = [None for i in range(len(data))]
  while None in checks:
    for j, x in enumerate(data):
      if checks[j] is not None:
        continue
      a = x * i
      if a >= bus:
        checks[j] = (a - bus)
    i += 1
  i = checks.index(min(checks))
  return data[i] * checks[i]


def calc_first(a, b, diff):
  n = 1
  while True:
    # a,x,b => bx - ay = diff <=> x = (diff + ay) / b
    m = (diff + n * a) / b
    if m == int(m):
      return a * n
    n += 1


@timer
def part2():
  data = parse_input2(DATA_INPUT[1])
  first = data[0]
  lst = []
  for i, n in enumerate(data[1:], start=1):
    if n is None:
      continue
    lst.append((calc_first(first, n, i), lcm(first, n)))
  print(lst)
  first = max(lst, key=lambda x: x[1])
  k = lst.index(first)
  lst = lst[:k] + lst[k + 1:]
  i = 1
  while True:
    g = first[0] + first[1] * i
    if all((g - s) % l == 0 for s, l in lst):
      return g
    i += 1


if __name__ == "__main__":
  print(part1())
  print(part2())
