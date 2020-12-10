#!/usr/bin/env python
"""
--- Day 10: Adapter Array ---
https://adventofcode.com/2020/day/10

Rank: 6451 / 2678
"""
import functools
import json
import re

from aocutils import *

DATA_INPUT = read_input('10', cast='int')
s = set(DATA_INPUT)


@timer
def part1():
  q = [0]
  j1 = set()
  j2 = set()
  j3 = set()
  DATA_INPUT.append(max(DATA_INPUT) + 3)
  while q:
    c = q[0]
    q = q[1:]
    news = []
    for i, n in enumerate(DATA_INPUT):
      if n - 1 == c:
        if c + 1 not in q:
          news.append(c + 1)
      elif n - 2 == c:
        if c + 2 not in q:
          news.append(c + 2)
      elif n - 3 == c:
        if c + 3 not in q:
          news.append(c + 3)
    if news:
      x = sorted(news)[0]
      q += [x]
      if x - 1 == c:
        j1.add(x)
      elif x - 2 == c:
        j2.add(x)
      elif x - 3 == c:
        j3.add(x)
  print(j1, j2, j3, len(j1), len(j3), len(j1) * len(j3))
  return len(j1) * len(j3)


@functools.lru_cache
def calc(c):
  if c == 0:
    return 1
  if c not in s:
    return 0
  return calc(c - 1) + calc(c - 2) + calc(c - 3)


@timer
def part2():
  return calc(max(DATA_INPUT))


if __name__ == "__main__":
  print(part1())
  print(part2())
