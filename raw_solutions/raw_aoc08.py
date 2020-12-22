#!/usr/bin/env python
"""
--- Day 8: Handheld Halting ---
https://adventofcode.com/2020/day/8

Rank: 1080 / 1176
"""
import functools
import json
import re

from aocutils import *

DATA_INPUT = read_input('08', cast='str')
# DATA_INPUT = read_input('08t', cast='str')


@timer
def part1():
  acc = 0
  i = 0
  insts = set()
  while i < len(DATA_INPUT):
    if i in insts:
      return acc
    insts.add(i)
    line = DATA_INPUT[i]
    inst, tmp = line.split(' ')
    if tmp[0] == '+':
      val = int(tmp[1:])
    else:
      val = int(tmp)
    # print(inst, val)
    if inst == 'acc':
      acc += val
    elif inst == 'jmp':
      i += val
      continue
    elif inst == 'nop':
      pass
    i += 1
  return


@timer
def part2():
  o_inp = []
  for line in DATA_INPUT:
    inst, tmp = line.split(' ')
    if tmp[0] == '+':
      val = int(tmp[1:])
    else:
      val = int(tmp)
    o_inp.append((inst, val))

  used = set()
  while True:
    # print(used)
    inp = list(o_inp)
    if len(used) == len(o_inp):
      return None
    for j, (x, y) in enumerate(o_inp):
      if j in used:
        continue
      used.add(j)
      if x == 'jmp':
        inp[j] = ('nop', y)
        break
      elif x == 'nop':
        inp[j] = ('jmp', y)
        break
      else:
        continue

    # print(inp)

    acc = 0
    i = 0
    insts = set()
    while i < len(inp):
      if i in insts:
        break
      insts.add(i)
      inst, val = inp[i]
      # print(inst, val)
      if inst == 'acc':
        acc += val
      elif inst == 'jmp':
        i += val
        continue
      elif inst == 'nop':
        pass
      i += 1
    if i == len(inp):
      return acc
  return acc


if __name__ == "__main__":
  print(part1())
  print(part2())
