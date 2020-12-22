#!/usr/bin/env python
"""
--- Day 22: Crab Combat ---
https://adventofcode.com/2020/day/22

Rank: 4628 / 3082
"""
import functools
import json
import re
from queue import Queue

from aocutils import *

DATA_INPUT = read_input('22', cast='str')
# DATA_INPUT = read_input('22t', cast='str')

PLAYERS = {1: [], 2: []}
curr_player = 1
for line in DATA_INPUT:
  if not line:
    curr_player = 2
  elif line.startswith('Player'):
    continue
  else:
    PLAYERS[curr_player].append(int(line))


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
  while PLAYERS[1] and PLAYERS[2]:
    c1 = PLAYERS[1][0]
    c2 = PLAYERS[2][0]
    PLAYERS[1] = PLAYERS[1][1:]
    PLAYERS[2] = PLAYERS[2][1:]

    if c1 > c2:
      PLAYERS[1] += [c1, c2]
    elif c2 > c1:
      PLAYERS[2] += [c2, c1]
    else:
      assert False
  total = 0
  for i, c in enumerate(PLAYERS[1][::-1], start=1):
    total += c * i
  for i, c in enumerate(PLAYERS[2][::-1], start=1):
    total += c * i
  return total


def game(d1, d2):
  previous = set()
  winner = None
  i = 0
  while d1 and d2:
    i += 1
    m = '.'.join(str(x) for x in d1) + ',' + '.'.join(str(x) for x in d2)
    if m in previous:
      winner = 1
      break
    previous.add(m)

    c1 = d1[0]
    c2 = d2[0]
    d1 = d1[1:]
    d2 = d2[1:]

    sub_winner = None
    if len(d1) >= c1 and len(d2) >= c2:
      sub_winner, _ = game(list(d1[:c1]), list(d2[:c2]))
    else:
      if c1 > c2:
        sub_winner = 1
      else:
        sub_winner = 2

    if sub_winner == 1:
      d1 += [c1, c2]
    else:
      d2 += [c2, c1]
  if winner is None:
    if not d1:
      winner = 2
    if not d2:
      winner = 1
  if winner == 1:
    return 1, d1
  else:
    return 2, d2


@timer
def part2():
  winner, deck = game(list(PLAYERS[1]), list(PLAYERS[2]))
  total = 0
  for i, c in enumerate(deck[::-1], start=1):
    total += c * i
  return total


if __name__ == "__main__":
  # print(part1())
  print(part2())
