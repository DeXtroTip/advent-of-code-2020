#!/usr/bin/env python
"""
--- Day 2: Password Philosophy ---
https://adventofcode.com/2020/day/2

Rank: 460 / 476
"""
from aocutils import read_input, timer


def parse_line(line):
  tokens = line.split()
  c1, c2 = (int(t) for t in tokens[0].split('-'))
  char = tokens[1][0]
  password = tokens[2]
  return c1, c2, char, password


DATA_INPUT = [parse_line(line) for line in read_input('02', cast='str')]


def validate_policy_1(c1, c2, char, password):
  return c1 <= sum(c == char for c in password) <= c2


def validate_policy_2(c1, c2, char, password):
  return (password[c1 - 1] == char and password[c2 - 1] != char) \
    or (password[c1 - 1] != char and password[c2 - 1] == char)


@timer
def part1():
  return sum(validate_policy_1(*data) for data in DATA_INPUT)


@timer
def part2():
  return sum(validate_policy_2(*data) for data in DATA_INPUT)


if __name__ == "__main__":
  print(part1())
  print(part2())
