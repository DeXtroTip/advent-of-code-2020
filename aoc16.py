#!/usr/bin/env python
"""
--- Day 16: Ticket Translation ---
https://adventofcode.com/2020/day/16

Rank: 1225 / 785
"""
from functools import reduce

from aocutils import read_input, timer

DATA_INPUT = read_input('16', cast='str')


def parse_data_input():
  part = 0
  rules = {}
  nearby = []
  for line in DATA_INPUT:
    if not line:
      part += 1
    elif part == 0:
      name, tokens = line.split(':')
      r1, _, r2 = tokens.split(' ')[1:]
      r1min, r1max = [int(x) for x in r1.split('-')]
      r2min, r2max = [int(x) for x in r2.split('-')]
      rules[name] = ((r1min, r1max), (r2min, r2max))
    elif part == 1 and not line.startswith('your ticket:'):
      tokens = [int(x) for x in line.split(',')]
      mine = tuple(int(x) for x in line.split(','))
    elif part == 2 and not line.startswith('nearby tickets:'):
      nearby.append(tuple(int(x) for x in line.split(',')))
  return rules, mine, nearby


@timer
def part1():
  rules, _, nearby = parse_data_input()
  return sum(v for ticket in nearby for v in ticket if not any(r1min <= v <= r1max or r2min <= v <= r2max
                                                               for (r1min, r1max), (r2min, r2max) in rules.values()))


@timer
def part2():
  rules, mine, nearby = parse_data_input()
  to_remove = [
    i for i, ticket in enumerate(nearby) for v in ticket
    if not any(r1min <= v <= r1max or r2min <= v <= r2max for (r1min, r1max), (r2min, r2max) in rules.values())
  ]
  for i in to_remove[::-1]:
    nearby = nearby[:i] + nearby[i + 1:]

  possible_orders = {r: {i for i in range(len(mine))} for r in rules.keys()}
  for ticket in nearby:
    tmp = {r: set() for r in rules.keys()}
    for i, v in enumerate(ticket):
      for rule, ((r1min, r1max), (r2min, r2max)) in rules.items():
        if r1min <= v <= r1max or r2min <= v <= r2max:
          tmp[rule].add(i)
    for k, v in possible_orders.items():
      possible_orders[k] = set(tmp[k]).intersection(v)

  while any(len(x) > 1 for x in possible_orders.values()):
    for k, v in possible_orders.items():
      if len(v) == 1:
        for k2, v2 in possible_orders.items():
          if k == k2:
            continue
          x = next(x for x in v)
          if x in v2:
            v2.remove(x)
  return reduce(lambda x, y: x * y,
                (mine[next(a for a in v)] for k, v in possible_orders.items() if k.startswith('departure')))


if __name__ == "__main__":
  print(part1())
  print(part2())
