#!/usr/bin/env python
"""
--- Day 14: Docking Data ---
https://adventofcode.com/2020/day/14

Rank: 661 / 373
"""
import functools
import json
import re
from queue import Queue

from aocutils import *

DATA_INPUT = read_input('14', cast='str')
# DATA_INPUT = read_input('14t', cast='str')


def parse_input(line):
  if 'mask' in line:
    tokens = line.split('=')
    return list(tokens[1].strip())
  else:
    tokens = line.split('=')
    mem_pos = int(tokens[0].strip()[4:-1])
    val = int(tokens[1].strip())
    return mem_pos, val


@functools.lru_cache
def calc(c):
  if c == 0:
    return 1
  return calc(c - 1) + calc(c - 2) + calc(c - 3)


def set_bit(value, bit):
  return value | (1 << bit)


def clear_bit(value, bit):
  return value & ~(1 << bit)


def apply_mask(mask, val):
  x = val
  for i, n in enumerate(mask[::-1]):
    if n == '1':
      x = set_bit(x, i)
    elif n == '0':
      x = clear_bit(x, i)
  return x


def apply_mask2(mask, val):
  floating_bits = []
  x = val
  for i, n in enumerate(mask[::-1]):
    if n == '1':
      x = set_bit(x, i)
    elif n == '0':
      pass
    elif n == 'X':
      floating_bits.append(i)
  output = [x]
  for b in floating_bits:
    for o in output:
      w = set_bit(o, b)
      y = clear_bit(o, b)
      if w not in output:
        output.append(w)
      if y not in output:
        output.append(y)
  return output


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
  mask = None
  mem = {}
  for line in data:
    if len(line) > 2:
      mask = line
    else:
      idx, val = line
      mem[idx] = apply_mask(mask, val)
  print(mem)
  return sum(mem.values())


@timer
def part2():
  data = [parse_input(line) for line in DATA_INPUT]
  mask = None
  mem = {}
  for line in data:
    if len(line) > 2:
      mask = line
    else:
      idx, val = line
      idxx = apply_mask2(mask, idx)
      for i in idxx:
        mem[i] = val
  # print(mem)
  return sum(mem.values())


if __name__ == "__main__":
  # print(part1())
  print(part2())
