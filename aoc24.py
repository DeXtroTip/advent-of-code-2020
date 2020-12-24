#!/usr/bin/env python
"""
--- Day 24: Lobby Layout ---
https://adventofcode.com/2020/day/24

Rank: 386 / 468
"""
from aocutils import read_input, timer

DATA_INPUT = read_input('24', cast='str')

MOVES = {
  'e': (lambda x, y: (x + 1, y)),
  'se': (lambda x, y: (x + 1, y - 1)),
  'ne': (lambda x, y: (x, y + 1)),
  'w': (lambda x, y: (x - 1, y)),
  'sw': (lambda x, y: (x, y - 1)),
  'nw': (lambda x, y: (x - 1, y + 1)),
}


def parse_input(line):
  directions = []
  idx = 0
  while idx < len(line):
    c = line[idx]
    if c in ('n', 's'):
      idx += 1
      c += line[idx]
    idx += 1
    directions.append(c)
  return directions


def calculate_tile(directions):
  x, y = 0, 0
  for d in directions:
    x, y = MOVES[d](x, y)
  return x, y


@timer
def part1():
  tiles = {}
  for direction in DIRECTIONS:
    tile = calculate_tile(direction)
    tiles[tile] = not tiles.get(tile, False)
  return sum(c for c in tiles.values())


@timer
def part2():
  tiles = {}
  for direction in DIRECTIONS:
    tile = calculate_tile(direction)
    tiles[tile] = not tiles.get(tile, False)
  for _ in range(100):
    coords = set()
    for x, y in tiles.keys():
      coords.add((x, y))
      for m in MOVES.values():
        coords.add(m(x, y))
    tiles_copy = dict(tiles)
    for x, y in coords:
      adj = sum(tiles_copy.get(m(x, y), False) for m in MOVES.values())
      if tiles.get((x, y), False) and (adj == 0 or adj > 2):
        tiles[(x, y)] = not tiles.get((x, y), False)
      elif not tiles.get((x, y), False) and adj == 2:
        tiles[(x, y)] = not tiles.get((x, y), False)
  return sum(x for x in tiles.values())


if __name__ == "__main__":
  DIRECTIONS = [parse_input(line) for line in DATA_INPUT]
  print(part1())
  print(part2())
