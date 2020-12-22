#!/usr/bin/env python
"""
--- Day 12: Rain Risk ---
https://adventofcode.com/2020/day/12

Rank: 1558 / 1312
"""
import functools
import json
import re
from queue import Queue

from aocutils import *

DATA_INPUT = read_input('12', cast='str')
# DATA_INPUT = read_input('12t', cast='str')

MOVES = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}


def parse_input(line):
  return (line[0], int(line[1:]))


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


def manhattan(p1, p2):
  return sum(abs(a - b) for a, b in zip(p1, p2))


@timer
def part1():
  data = [parse_input(line) for line in DATA_INPUT]
  curr = (0, 0)
  facing = (1, 0)
  for m, value in data:
    # print(curr, facing)
    # print(m, value)
    # print()
    pm = MOVES.get(m)
    if pm is not None:
      curr = (curr[0] + pm[0] * value, curr[1] + pm[1] * value)
    elif m == 'L':
      x = value // 90
      while x > 0:
        x -= 1
        if facing == (1, 0):
          facing = (0, 1)
        elif facing == (-1, 0):
          facing = (0, -1)
        elif facing == (0, 1):
          facing = (-1, 0)
        else:
          facing = (1, 0)
    elif m == 'R':
      x = value // 90
      while x > 0:
        x -= 1
        if facing == (1, 0):
          facing = (0, -1)
        elif facing == (-1, 0):
          facing = (0, 1)
        elif facing == (0, 1):
          facing = (1, 0)
        else:
          facing = (-1, 0)
    elif m == 'F':
      curr = (curr[0] + value * facing[0], curr[1] + value * facing[1])
  return curr, manhattan((0, 0), curr)


@timer
def part2():
  data = [parse_input(line) for line in DATA_INPUT]
  waypoint = (10, 1)
  curr = (0, 0)
  for m, value in data:
    # print(curr, waypoint)
    # print(m, value)
    # print()
    pm = MOVES.get(m)
    if pm is not None:
      waypoint = (waypoint[0] + pm[0] * value, waypoint[1] + pm[1] * value)
    elif m == 'L':
      t = value // 90
      while t > 0:
        t -= 1
        waypoint = (-waypoint[1], waypoint[0])
    elif m == 'R':
      t = value // 90
      while t > 0:
        t -= 1
        waypoint = (waypoint[1], -waypoint[0])
    elif m == 'F':
      curr = (curr[0] + value * waypoint[0], curr[1] + value * waypoint[1])
  return curr, manhattan((0, 0), curr)


if __name__ == "__main__":
  print(part1())
  print(part2())
