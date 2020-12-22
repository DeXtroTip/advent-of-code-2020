#!/usr/bin/env python
"""
--- Day 16: Ticket Translation ---
https://adventofcode.com/2020/day/16

Rank: 1225 / 785
"""
import functools
import json
import re
from queue import Queue

from aocutils import *

DATA_INPUT = read_input('16', cast='str')
# DATA_INPUT = read_input('16t', cast='str')


def parse_input(line):
  return line


@functools.lru_cache
def calc(c):
  if c == 0:
    return 1
  return calc(c - 1) + calc(c - 2) + calc(c - 3)


def get_map(map_, default_val, mapping=None):
  out = ''
  min_x = int(min(x for (x, y) in map_.keys()))
  max_x = int(max(x for (x, y) in map_.keys()))
  min_y = int(min(y for (x, y) in map_.keys()))
  max_y = int(max(y for (x, y) in map_.keys()))
  for y_coord in range(min_y, max_y + 1):
    line = ''
    for x_coord in range(min_x, max_x + 1):
      map_val = map_.get((x_coord, y_coord), default_val)
      line += str(mapping.get(map_val, map_val) if mapping is not None else map_val)
    out += line + '\n'
  return out


@timer
def part1():
  part = 0
  rules = {}
  nearby = []
  for line in DATA_INPUT:
    if not line:
      part += 1
      continue
    if part == 0:
      tokens = line.split(':')
      t2 = tokens[1].split(' ')[1:]
      r1min, r1max = [int(x) for x in t2[0].split('-')]
      r2min, r2max = [int(x) for x in t2[2].split('-')]
      rules[tokens[0]] = ((r1min, r1max), (r2min, r2max))
    elif part == 1:
      if line.startswith('your ticket:'):
        pass
      pass
    else:
      if line.startswith('nearby tickets:'):
        continue
      tokens = [int(x) for x in line.split(',')]
      nearby.append(tuple(tokens))

  error_rate = 0

  for ticket in nearby:
    for v in ticket:
      is_valid = False
      for (r1min, r1max), (r2min, r2max) in rules.values():
        if r1min <= v <= r1max or r2min <= v <= r2max:
          is_valid = True
          break
      if not is_valid:
        error_rate += v

  return error_rate


@timer
def part2():
  part = 0
  rules = {}
  mine = None
  nearby = []
  for line in DATA_INPUT:
    if not line:
      part += 1
      continue
    if part == 0:
      tokens = line.split(':')
      t2 = tokens[1].split(' ')[1:]
      r1min, r1max = [int(x) for x in t2[0].split('-')]
      r2min, r2max = [int(x) for x in t2[2].split('-')]
      rules[tokens[0]] = ((r1min, r1max), (r2min, r2max))
    elif part == 1:
      if line.startswith('your ticket:'):
        continue
      tokens = [int(x) for x in line.split(',')]
      mine = tuple(tokens)
    else:
      if line.startswith('nearby tickets:'):
        continue
      tokens = [int(x) for x in line.split(',')]
      nearby.append(tuple(tokens))

  to_remove = []
  for i, ticket in enumerate(nearby):
    for v in ticket:
      is_valid = False
      for (r1min, r1max), (r2min, r2max) in rules.values():
        if r1min <= v <= r1max or r2min <= v <= r2max:
          is_valid = True
          break
      if not is_valid:
        to_remove.append(i)
        break
  for j, i in enumerate(to_remove):
    nearby = nearby[:i - j] + nearby[i - j + 1:]

  possible_orders = {r: {i for i in range(len(mine))} for r in rules.keys()}
  for ticket in nearby:
    tmp = {r: set() for r in rules.keys()}
    for i, v in enumerate(ticket):
      for rule, ((r1min, r1max), (r2min, r2max)) in rules.items():
        if r1min <= v <= r1max or r2min <= v <= r2max:
          tmp[rule].add(i)
    for k, v in possible_orders.items():
      possible_orders[k] = set(tmp[k]).intersection(v)

  while any(len(x) > 1 for x in possible_orders.values()):
    print(possible_orders)
    for k, v in possible_orders.items():
      if len(v) == 1:
        for k2, v2 in possible_orders.items():
          if k == k2:
            continue
          a = list(v)[0]
          if a in v2:
            v2.remove(a)

  result = 1
  for k, v in possible_orders.items():
    print(v)
    if k.startswith('departure'):
      i = list(v)[0]
      result *= mine[i]

  return result


if __name__ == "__main__":
  # print(part1())
  print(part2())
