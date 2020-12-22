#!/usr/bin/env python
"""
--- Day 17: Conway Cubes ---
https://adventofcode.com/2020/day/17

Rank: 2238 / 1894
"""
import functools
import json
import re
from queue import Queue

from aocutils import *

DATA_INPUT = read_input('17', cast='str')
# DATA_INPUT = read_input('17t', cast='str')

DATA = {(x, y, 0): DATA_INPUT[y][x] for y in range(len(DATA_INPUT)) for x in range(len(DATA_INPUT[y]))}
DATA2 = {(x, y, 0, 0): DATA_INPUT[y][x] for y in range(len(DATA_INPUT)) for x in range(len(DATA_INPUT[y]))}


def parse_input(line):
  return line


@functools.lru_cache
def calc(c):
  if c == 0:
    return 1
  return calc(c - 1) + calc(c - 2) + calc(c - 3)


def get_map(map_, default_val, mapping=None):
  out = ''
  min_x = int(min(x for (x, y, z) in map_.keys()))
  max_x = int(max(x for (x, y, z) in map_.keys()))
  min_y = int(min(y for (x, y, z) in map_.keys()))
  max_y = int(max(y for (x, y, z) in map_.keys()))
  min_z = int(min(z for (x, y, z) in map_.keys()))
  max_z = int(max(z for (x, y, z) in map_.keys()))
  for z_coord in range(min_z, max_z + 1):
    out += 'z=' + str(z_coord) + '\n'
    for y_coord in range(min_y, max_y + 1):
      line = ''
      for x_coord in range(min_x, max_x + 1):
        map_val = map_.get((x_coord, y_coord, z_coord), default_val)
        line += str(mapping.get(map_val, map_val) if mapping is not None else map_val)
      out += line + '\n'
  return out


STATES = {}
STATES2 = {}


@functools.lru_cache
def get_neighbors(cycle, p):
  x, y, z = p
  m = {'active': set(), 'inactive': set()}
  for tz in range(z - 1, z + 2):
    for ty in range(y - 1, y + 2):
      for tx in range(x - 1, x + 2):
        p2 = (tx, ty, tz)
        if p == p2:
          continue
        if STATES[cycle].get(p2, '.') == '#':
          m['active'].add(p2)
        else:
          m['inactive'].add(p2)
  return m


@functools.lru_cache
def get_neighbors2(cycle, p):
  x, y, z, w = p
  m = {'active': set(), 'inactive': set()}
  for tw in range(w - 1, w + 2):
    for tz in range(z - 1, z + 2):
      for ty in range(y - 1, y + 2):
        for tx in range(x - 1, x + 2):
          p2 = (tx, ty, tz, tw)
          if p == p2:
            continue
          if STATES2[cycle].get(p2, '.') == '#':
            m['active'].add(p2)
          else:
            m['inactive'].add(p2)
  return m


@timer
def part1():
  cycle = 0
  STATES[0] = dict(DATA)
  while cycle < 6:
    state = dict(STATES[cycle])

    # print(cycle)
    # print(get_map(state, '.'))
    # print()

    min_x = int(min(x for (x, y, z) in state.keys()))
    max_x = int(max(x for (x, y, z) in state.keys()))
    min_y = int(min(y for (x, y, z) in state.keys()))
    max_y = int(max(y for (x, y, z) in state.keys()))
    min_z = int(min(z for (x, y, z) in state.keys()))
    max_z = int(max(z for (x, y, z) in state.keys()))
    for z_coord in range(min_z - 1, max_z + 2):
      for y_coord in range(min_y - 1, max_y + 2):
        for x_coord in range(min_x - 1, max_x + 2):
          p = (x_coord, y_coord, z_coord)
          val = state.get(p)
          neighbors = get_neighbors(cycle, p)
          if val == '#' and not len(neighbors['active']) in (2, 3):
            state[p] = '.'
          elif val != '#' and len(neighbors['active']) == 3:
            state[p] = '#'
    cycle += 1
    STATES[cycle] = state

  # print(cycle)
  # print(get_map(state, '.'))
  # print()

  return sum(v == '#' for v in STATES[cycle].values())


@timer
def part2():
  cycle = 0
  STATES2[0] = dict(DATA2)
  while cycle < 6:
    state = dict(STATES2[cycle])

    # print(cycle)
    # print(get_map(state, '.'))
    # print()

    min_x = int(min(x for (x, y, z, w) in state.keys()))
    max_x = int(max(x for (x, y, z, w) in state.keys()))
    min_y = int(min(y for (x, y, z, w) in state.keys()))
    max_y = int(max(y for (x, y, z, w) in state.keys()))
    min_z = int(min(z for (x, y, z, w) in state.keys()))
    max_z = int(max(z for (x, y, z, w) in state.keys()))
    min_w = int(min(w for (x, y, z, w) in state.keys()))
    max_w = int(max(w for (x, y, z, w) in state.keys()))
    for w_coord in range(min_w - 1, max_w + 2):
      for z_coord in range(min_z - 1, max_z + 2):
        for y_coord in range(min_y - 1, max_y + 2):
          for x_coord in range(min_x - 1, max_x + 2):
            p = (x_coord, y_coord, z_coord, w_coord)
            val = state.get(p)
            neighbors = get_neighbors2(cycle, p)
            if val == '#' and not len(neighbors['active']) in (2, 3):
              state[p] = '.'
            elif val != '#' and len(neighbors['active']) == 3:
              state[p] = '#'
    cycle += 1
    STATES2[cycle] = state

  # print(cycle)
  # print(get_map(state, '.'))
  # print()

  return sum(v == '#' for v in STATES2[cycle].values())


if __name__ == "__main__":
  # print(part1())
  print(part2())
