#!/usr/bin/env python
"""
--- Day 15: Rambunctious Recitation ---
https://adventofcode.com/2020/day/15

Rank: 2499 / 1325
"""
import functools
import json
import re
from queue import Queue

from aocutils import *

DATA_INPUT = read_input_split_first_line('15', cast='int')
# DATA_INPUT = read_input_split_first_line('15t', cast='int')


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
  numbers = {n: [i, i] for i, n in enumerate(DATA_INPUT, start=1)}
  turn = len(numbers)
  last_number = DATA_INPUT[-1]
  first_time = True
  while turn < 2020:
    turn += 1
    # print(turn, last_number, numbers)
    if first_time:
      next_number = 0
      lst = numbers.get(next_number, [])
      if not lst:
        first_time = True
        lst = [turn, turn]
      else:
        first_time = False
        lst = lst[1:] + [turn]
      numbers[next_number] = lst
      last_number = next_number
    else:
      lst_last = numbers[last_number]
      next_number = lst_last[1] - lst_last[0]
      lst = numbers.get(next_number, [])
      if not lst:
        first_time = True
        lst = [turn, turn]
      else:
        first_time = False
        lst = lst[1:] + [turn]
      numbers[next_number] = lst
      last_number = next_number
  # print(numbers)
  # print(turn, last_number)
  return last_number


@timer
def part2():
  numbers = {n: [i, i] for i, n in enumerate(DATA_INPUT, start=1)}
  turn = len(numbers)
  last_number = DATA_INPUT[-1]
  first_time = True
  while turn < 30000000:
    turn += 1
    # print(turn, last_number, numbers)
    if first_time:
      next_number = 0
      lst = numbers.get(next_number, [])
      if not lst:
        first_time = True
        lst = [turn, turn]
      else:
        first_time = False
        lst = lst[1:] + [turn]
      numbers[next_number] = lst
      last_number = next_number
    else:
      lst_last = numbers[last_number]
      next_number = lst_last[1] - lst_last[0]
      lst = numbers.get(next_number, [])
      if not lst:
        first_time = True
        lst = [turn, turn]
      else:
        first_time = False
        lst = lst[1:] + [turn]
      numbers[next_number] = lst
      last_number = next_number
  # print(numbers)
  # print(turn, last_number)
  return last_number


if __name__ == "__main__":
  print(part1())
  print(part2())
