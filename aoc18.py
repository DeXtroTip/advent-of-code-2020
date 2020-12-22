#!/usr/bin/env python
"""
--- Day 18: Operation Order ---
https://adventofcode.com/2020/day/18

Rank: 6427 / 5314
"""
import re

from aocutils import read_input, timer

DATA_INPUT = [re.sub('(\\d+)', 'NewInt(\\1)', line) for line in read_input('18', cast='str')]


class NewInt:
  def __init__(self, v):
    self.v = v

  def __add__(self, o):
    return NewInt(self.v + o.v)

  def __sub__(self, o):
    return NewInt(self.v * o.v)

  def __mul__(self, o):
    return NewInt(self.v + o.v)


@timer
def part1():
  return sum(eval(line.replace('*', '-')).v for line in DATA_INPUT)


@timer
def part2():
  return sum(eval(line.replace('*', '-').replace('+', '*')).v for line in DATA_INPUT)


if __name__ == "__main__":
  print(part1())
  print(part2())
