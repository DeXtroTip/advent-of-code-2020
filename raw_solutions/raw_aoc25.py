#!/usr/bin/env python
"""
--- Day 25: Combo Breaker ---
https://adventofcode.com/2020/day/25

Rank: 2527 / 2070
"""
import json
import re
from functools import reduce
from queue import Queue

from aocutils import *

DATA_INPUT = read_input('25', cast='int')
# DATA_INPUT = read_input('25t', cast='int')

CARD, DOOR = DATA_INPUT


def transform(start, subject, loop_size):
  n = start
  for _ in range(loop_size):
    n = (n * subject) % 20201227
  return n


@timer
def part1():
  ls = 0
  subject = None
  n = 1
  while True:
    ls += 1
    n = transform(n, 7, 1)
    if n == CARD:
      subject = DOOR
      break
    if n == DOOR:
      subject = CARD
      break
  return transform(1, subject, ls)


if __name__ == "__main__":
  print(part1())
