#!/usr/bin/env python
"""
--- Day 17: Conway Cubes ---
https://adventofcode.com/2020/day/17

Rank: 2238 / 1894
"""
import functools

from aocutils import read_input, timer

DATA_INPUT = read_input('17', cast='str')

DATA_3D = {(x, y, 0): DATA_INPUT[y][x] for y in range(len(DATA_INPUT)) for x in range(len(DATA_INPUT[y]))}
DATA_4D = {(x, y, 0, 0): DATA_INPUT[y][x] for y in range(len(DATA_INPUT)) for x in range(len(DATA_INPUT[y]))}

STATES_3D = {}
STATES_4D = {}


@functools.lru_cache
def get_neighbors_3d(cycle, p):
  x, y, z = p
  m = {'active': set(), 'inactive': set()}
  for tz in range(z - 1, z + 2):
    for ty in range(y - 1, y + 2):
      for tx in range(x - 1, x + 2):
        p2 = (tx, ty, tz)
        if p == p2:
          continue
        if STATES_3D[cycle].get(p2, '.') == '#':
          m['active'].add(p2)
        else:
          m['inactive'].add(p2)
  return m


@functools.lru_cache
def get_neighbors_4d(cycle, p):
  x, y, z, w = p
  m = {'active': set(), 'inactive': set()}
  for tw in range(w - 1, w + 2):
    for tz in range(z - 1, z + 2):
      for ty in range(y - 1, y + 2):
        for tx in range(x - 1, x + 2):
          p2 = (tx, ty, tz, tw)
          if p == p2:
            continue
          if STATES_4D[cycle].get(p2, '.') == '#':
            m['active'].add(p2)
          else:
            m['inactive'].add(p2)
  return m


@timer
def part1():
  cycle = 0
  STATES_3D[0] = dict(DATA_3D)
  while cycle < 6:
    state = dict(STATES_3D[cycle])
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
          neighbors = get_neighbors_3d(cycle, p)
          if val == '#' and not len(neighbors['active']) in (2, 3):
            state[p] = '.'
          elif val != '#' and len(neighbors['active']) == 3:
            state[p] = '#'
    cycle += 1
    STATES_3D[cycle] = state
  return sum(v == '#' for v in STATES_3D[cycle].values())


@timer
def part2():
  # TODO: Needs review, takes more than 3 seconds to finish
  cycle = 0
  STATES_4D[0] = dict(DATA_4D)
  while cycle < 6:
    state = dict(STATES_4D[cycle])
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
            neighbors = get_neighbors_4d(cycle, p)
            if val == '#' and not len(neighbors['active']) in (2, 3):
              state[p] = '.'
            elif val != '#' and len(neighbors['active']) == 3:
              state[p] = '#'
    cycle += 1
    STATES_4D[cycle] = state
  return sum(v == '#' for v in STATES_4D[cycle].values())


if __name__ == "__main__":
  print(part1())
  print(part2())
