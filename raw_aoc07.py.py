#!/usr/bin/env python
"""
--- Day 7: Handy Haversacks ---
https://adventofcode.com/2020/day/7

Rank: 401 / 590
"""
import json
from functools import *

from aocutils import *

DATA_INPUT = read_input('07', cast='str')


@timer
def part1():
  total = 0
  lst = []
  d = {}
  s = set()
  for line in DATA_INPUT:
    line = line[:-1]
    tokens = line.split(' ')
    k = tokens[0] + ' ' + tokens[1]
    d[k] = {}
    tokens = ' '.join(tokens[4:]).split(', ')
    for token in tokens:
      if token.startswith('no'):
        continue
      t = token.split(' ')
      d[k][t[1] + ' ' + t[2]] = int(t[0])
  while True:
    old = set(s)
    for k, v in d.items():
      for vv in v:
        if vv == 'shiny gold' or vv in s:
          s.add(k)
    if old == s:
      break
  return len(s)


@timer
def part2():
  total = 0
  lst = []
  d = {}
  s = set()
  for line in DATA_INPUT:
    line = line[:-1]
    tokens = line.split(' ')
    k = tokens[0] + ' ' + tokens[1]
    d[k] = {}
    tokens = ' '.join(tokens[4:]).split(', ')
    for token in tokens:
      if token.startswith('no'):
        continue
      t = token.split(' ')
      d[k][t[1] + ' ' + t[2]] = int(t[0])
  q = [('shiny gold', 1)]
  while q:
    bag, n = q[0]
    # print(q, bag, n)
    q = q[1:]
    total += n
    for k, v in d[bag].items():
      q.append((k, n * v))
  return total - 1


if __name__ == "__main__":
  print(part1())
  print(part2())
