#!/usr/bin/env python
"""
--- Day 7: Handy Haversacks ---
https://adventofcode.com/2020/day/7

Rank: 401 / 590
"""
from aocutils import read_input, timer


def parse_input(inp):
  d = {}
  for line in inp:
    line = line[:-1]
    tokens = line.split(' ')
    bag = f'{tokens[0]} {tokens[1]}'
    d[bag] = {}
    for token in ' '.join(tokens[4:]).split(', '):
      if token.startswith('no'):
        continue
      token2 = token.split(' ')
      d[bag][f'{token2[1]} {token2[2]}'] = int(token2[0])
  return d


DATA_INPUT = parse_input(read_input('07', cast='str'))


@timer
def part1():
  bags = set()
  while True:
    tmp = set(bags)
    bags |= set(k for k, v in DATA_INPUT.items() for bag in v.keys() if bag == 'shiny gold' or bag in bags)
    if tmp == bags:
      return len(bags)


@timer
def part2():
  total = 0
  q = [('shiny gold', 1)]
  while q:
    bag, n = q[0]
    total += n
    q = q[1:] + [(k, n * v) for k, v in DATA_INPUT[bag].items()]
  return total - 1


if __name__ == "__main__":
  print(part1())
  print(part2())
