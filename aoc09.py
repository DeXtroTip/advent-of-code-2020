#!/usr/bin/env python
"""
--- Day 9: Encoding Error ---
https://adventofcode.com/2020/day/9

Rank: 1025 / 823
"""
import functools

from aocutils import read_input, timer

N_PREVIOUS = 25

DATA_INPUT = read_input('09', cast='int')


def is_valid_sum(n, lst):
  return any(x + y == n for i, x in enumerate(lst) for y in lst[i:])


@functools.lru_cache(maxsize=1)
def find_invalid_number():
  previous_numbers = DATA_INPUT[:N_PREVIOUS]
  for n in DATA_INPUT[N_PREVIOUS:]:
    if not is_valid_sum(n, previous_numbers):
      return n
    previous_numbers = previous_numbers[1:] + [n]


@timer
def part1():
  return find_invalid_number()


@timer
def part2():
  invalid_n = find_invalid_number()
  curr_lst = []
  curr_sum = 0
  i = 0
  while i < len(DATA_INPUT):
    while curr_sum < invalid_n:
      curr_lst.append(DATA_INPUT[i])
      curr_sum += curr_lst[-1]
      i += 1
    while curr_sum > invalid_n:
      curr_sum -= curr_lst[0]
      curr_lst.pop(0)
    if len(curr_lst) > 1 and curr_sum == invalid_n:
      return min(curr_lst) + max(curr_lst)


if __name__ == "__main__":
  print(part1())
  print(part2())
