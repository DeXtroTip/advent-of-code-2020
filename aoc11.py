#!/usr/bin/env python
"""
--- Day 11: Seating System ---
https://adventofcode.com/2020/day/11

Rank: 3140 / 1896
"""
from aocutils import read_input, timer

DATA_INPUT = read_input('11', cast='str')

ORIGINAL_SEATS = {(x, y): DATA_INPUT[y][x] for y in range(len(DATA_INPUT)) for x in range(len(DATA_INPUT[y]))}


def get_adjacent_occupied(seat, seats):
  return sum(
    (i != 0 or j != 0) and seats.get((seat[0] + i, seat[1] + j)) == '#' for i in (-1, 0, 1) for j in (-1, 0, 1))


def get_adjacent_line_occupied(seat, seats):
  occupied = 0
  for i in (-1, 0, 1):
    for j in (-1, 0, 1):
      if i == 0 and j == 0:
        continue
      next_seat = (seat[0] + i, seat[1] + j)
      while seats.get(next_seat, '') == '.':
        next_seat = (next_seat[0] + i, next_seat[1] + j)
      if seats.get(next_seat, '') == '#':
        occupied += 1
  return occupied


def calculate_occupied(calc_adjacent_func, occupied_threshold):
  seats = dict(ORIGINAL_SEATS)
  had_changes = True
  while had_changes:
    had_changes = False
    curr_seats = dict(seats)
    for seat, state in curr_seats.items():
      if state == '.':
        continue
      occupied = calc_adjacent_func(seat, curr_seats)
      if (state == 'L' and occupied == 0) or (state == '#' and occupied >= occupied_threshold):
        seats[seat] = 'L' if state == '#' else '#'
        had_changes = True
  return sum(seat == '#' for seat in seats.values())


@timer
def part1():
  return calculate_occupied(get_adjacent_occupied, 4)


@timer
def part2():
  return calculate_occupied(get_adjacent_line_occupied, 5)


if __name__ == "__main__":
  print(part1())
  print(part2())
