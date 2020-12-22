#!/usr/bin/env python
"""
--- Day 14: Docking Data ---
https://adventofcode.com/2020/day/14

Rank: 661 / 373
"""
from aocutils import clear_bit, read_input, set_bit, timer


def parse_input(line):
  if 'mask' in line:
    return list(line.split('=')[1].strip())
  else:
    tokens = line.split('=')
    return int(tokens[0].strip()[4:-1]), int(tokens[1].strip())


DATA_INPUT = read_input('14', cast='str')
DATA = [parse_input(line) for line in DATA_INPUT]


def apply_mask(mask, val):
  for i, n in enumerate(mask[::-1]):
    if n == '1':
      val = set_bit(val, i)
    elif n == '0':
      val = clear_bit(val, i)
  return val


def apply_mask_v2(mask, val):
  floating_bits = []
  for i, n in enumerate(mask[::-1]):
    if n == '1':
      val = set_bit(val, i)
    elif n == 'X':
      floating_bits.append(i)
  results = {val}
  for bit in floating_bits:
    for val in list(results):
      results.add(set_bit(val, bit))
      results.add(clear_bit(val, bit))
  return list(results)


@timer
def part1():
  mem = {}
  for item in DATA:
    if len(item) > 2:
      mask = item
    else:
      mem[item[0]] = apply_mask(mask, item[1])
  return sum(mem.values())


@timer
def part2():
  mem = {}
  for item in DATA:
    if len(item) > 2:
      mask = item
    else:
      for idx in apply_mask_v2(mask, item[0]):
        mem[idx] = item[1]
  return sum(mem.values())


if __name__ == "__main__":
  print(part1())
  print(part2())
