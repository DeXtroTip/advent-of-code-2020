#!/usr/bin/env python
"""
--- Day 15: Rambunctious Recitation ---
https://adventofcode.com/2020/day/15

Rank: 2499 / 1325
"""
from aocutils import read_input_split_first_line, timer

DATA_INPUT = read_input_split_first_line('15', cast='int')


def calculate_turn_number(goal_turn):
  numbers = {n: {'last': i, 'before': i} for i, n in enumerate(DATA_INPUT, start=1)}
  turn = len(numbers)
  n = DATA_INPUT[-1]
  while turn < goal_turn:
    turn += 1
    n = numbers[n]['last'] - numbers[n]['before']
    numbers[n] = {'before': numbers.get(n, {}).get('last') or turn, 'last': turn}
  return n


@timer
def part1():
  return calculate_turn_number(2020)


@timer
def part2():
  # TODO: Needs review, currently takes ~15s to run...
  return calculate_turn_number(30000000)


if __name__ == "__main__":
  print(part1())
  print(part2())
