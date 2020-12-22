#!/usr/bin/env python
"""
--- Day 18: Operation Order ---
https://adventofcode.com/2020/day/18

Rank: 6427 / 5314
"""
import functools
import json
import re
from queue import Queue

from aocutils import *

DATA_INPUT = read_input('18', cast='str')
# DATA_INPUT = read_input('18t', cast='str')


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


def calculate(text):
  text = text.strip()
  if text[0] in ('+', '*'):
    text = text[1:].strip()
  if text[-1] in ('+', '*'):
    text = text[:-1].strip()
  if '(' not in text and ')' not in text:
    tokens = text.split(' ')
    while '+' in tokens:
      to_rem = []
      for i, c in enumerate(tokens):
        if c == '+':
          tokens[i - 1] = str(int(tokens[i - 1]) + int(tokens[i + 1]))
          to_rem.append(i)
          break
      for i in to_rem[::-1]:
        tokens = tokens[:i] + tokens[i + 2:]
    total = int(tokens[0])
    t = None
    for c in tokens[1:]:
      if c.isdigit():
        total = total + int(c) if t == '+' else total * int(c)
      else:
        t = c
    return total
  else:
    while '(' in text and ')' in text:
      cd = 0
      idx_start_p = None
      for i in range(len(text)):
        if text[i] == '(':
          cd += 1
          if idx_start_p is None:
            idx_start_p = i
        if text[i] == ')':
          cd -= 1
          if cd == 0:
            idx_end_p = i
            break
      a = calculate(text[idx_start_p + 1:idx_end_p])
      text = text[:idx_start_p] + str(a) + text[idx_end_p + 1:]
    return calculate(text)


def calculate2(text):
  text = text.strip()
  if text[0] in ('+', '*'):
    text = text[1:].strip()
  if text[-1] in ('+', '*'):
    text = text[:-1].strip()
  if '(' not in text and ')' not in text:
    tokens = text.split(' ')
    total = int(tokens[0])
    t = None
    for c in tokens[1:]:
      if c.isdigit():
        total = total + int(c) if t == '+' else total * int(c)
      else:
        t = c
    return total
  else:
    while '(' in text and ')' in text:
      cd = 0
      idx_start_p = None
      for i in range(len(text)):
        if text[i] == '(':
          cd += 1
          if idx_start_p is None:
            idx_start_p = i
        if text[i] == ')':
          cd -= 1
          if cd == 0:
            idx_end_p = i
            break
      a = calculate(text[idx_start_p + 1:idx_end_p])
      text = text[:idx_start_p] + str(a) + text[idx_end_p + 1:]
    return calculate(text)


@timer
def part1():
  data = [parse_input(line) for line in DATA_INPUT]
  results = []
  for line in data:
    results.append(calculate(line))
  return sum(results)


@timer
def part2():
  data = [parse_input(line) for line in DATA_INPUT]
  results = []
  for line in data:
    results.append(calculate(line))
  print(results)
  return sum(results)


if __name__ == "__main__":
  # print(part1())
  print(part2())
