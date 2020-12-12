#!/usr/bin/env python
"""
--- Day 11: Seating System ---
https://adventofcode.com/2020/day/11

Rank: 3140 / 1896
"""
import functools
import json
import re
from queue import Queue

from aocutils import *

DATA_INPUT = read_input('11', cast='str')
# DATA_INPUT = read_input('11t', cast='str')


def parse_input(line):
  return list(line)


@functools.lru_cache
def calc(c):
  if c == 0:
    return 1
  return calc(c - 1) + calc(c - 2) + calc(c - 3)


def adjacent_occupied(x, y, m):
  seats = []
  for i in (-1, 0, 1):
    for j in (-1, 0, 1):
      p = (x + i, y + j)
      if p != (x, y) and m.get(p, '.') == '#':
        seats.append(p)
  return seats


def adjacent_occupied2(x, y, m):
  seats = []
  for i in (-1, 0, 1):
    for j in (-1, 0, 1):
      if i == 0 and j == 0:
        continue
      p = (x + i, y + j)
      a = m.get(p, '')
      while a == '.':
        p = (p[0] + i, p[1] + j)
        a = m.get(p, '')
      if a == '#':
        seats.append(p)
  return seats


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
  data = [parse_input(line) for line in DATA_INPUT]
  m = {}
  for y in range(len(data)):
    for x in range(len(data[y])):
      m[(x, y)] = data[y][x]
  r = 0
  while True:
    r += 1
    d = dict(m)
    changes = 0
    for (x, y), s in d.items():
      seats = adjacent_occupied(x, y, d)
      if s == '#' and len(seats) >= 4:
        m[(x, y)] = 'L'
        changes += 1
      elif s == 'L' and len(seats) == 0:
        m[(x, y)] = '#'
        changes += 1
    if changes == 0:
      break
    # print(changes)
    # print(get_map(m, '.'))
  print(get_map(m, '.'))
  return sum(s == '#' for s in m.values())


@timer
def part2():
  data = [parse_input(line) for line in DATA_INPUT]
  m = {}
  for y in range(len(data)):
    for x in range(len(data[y])):
      m[(x, y)] = data[y][x]
  r = 0
  while True:
    r += 1
    d = dict(m)
    changes = 0
    for (x, y), s in d.items():
      seats = adjacent_occupied2(x, y, d)
      if s == '#' and len(seats) >= 5:
        m[(x, y)] = 'L'
        changes += 1
      elif s == 'L' and len(seats) == 0:
        m[(x, y)] = '#'
        changes += 1
    if changes == 0:
      break
    print(changes)
    print(get_map(m, '.'))
  print(get_map(m, '.'))
  return sum(s == '#' for s in m.values())


if __name__ == "__main__":
  # print(part1())
  print(part2())
