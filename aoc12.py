#!/usr/bin/env python
"""
--- Day 12: Rain Risk ---
https://adventofcode.com/2020/day/12

Rank: 1558 / 1312
"""
from aocutils import read_input, timer


def parse_input(line):
  return (line[0], int(line[1:]))


DATA_INPUT = read_input('12', cast='str')
INSTRUCTIONS = [parse_input(line) for line in DATA_INPUT]

MOVES = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
TURN = {'L': lambda p: (-p[1], p[0]), 'R': lambda p: (p[1], -p[0])}


def manhattan(p1, p2):
  return sum(abs(a - b) for a, b in zip(p1, p2))


def get_move(action):
  return MOVES.get(action)


def get_turn_direction(action, value, direction):
  for _ in range(value, 0, -90):
    direction = TURN[action](direction)
  return direction


def simulate_navigation(instructions, starting_pos, starting_direction, has_waypoint=False):
  curr = starting_pos
  direction = starting_direction
  for action, value in instructions:
    move = direction if action == 'F' else get_move(action)
    if action == 'F' or (not has_waypoint and move is not None):
      curr = (curr[0] + move[0] * value, curr[1] + move[1] * value)
    elif action in ('L', 'R'):
      direction = get_turn_direction(action, value, direction)
    else:
      direction = (direction[0] + move[0] * value, direction[1] + move[1] * value)
  return manhattan(starting_pos, curr)


@timer
def part1():
  return simulate_navigation(INSTRUCTIONS, (0, 0), (1, 0))


@timer
def part2():
  return simulate_navigation(INSTRUCTIONS, (0, 0), (10, 1), has_waypoint=True)


if __name__ == "__main__":
  print(part1())
  print(part2())
