#!/usr/bin/env python
"""
--- Day 24: Lobby Layout ---
https://adventofcode.com/2020/day/24

Rank: 386 / 468
"""
from aocutils import read_input, timer

# TODO: Not reviewed from raw solution

DATA_INPUT = read_input('24', cast='str')


def parse_input(line):
  return line


def check_adj(tiles, tile):
  x, y = tile
  count = 0
  for x2, y2 in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y), (x - 1, y + 1), (x + 1, y - 1)]:
    if tiles.get((x2, y2), False):
      count += 1
  return count


def calculate_tile(line):
  x, y = 0, 0
  i = 0
  c = line[i]
  while i < len(line):
    if c == 'e':
      x += 1
    elif c == 'se':
      x += 1
      y -= 1
    elif c == 'sw':
      y -= 1
    elif c == 'w':
      x -= 1
    elif c == 'nw':
      x -= 1
      y += 1
    elif c == 'ne':
      y += 1
    else:
      i += 1
      c += line[i]
      continue
    i += 1
    try:
      c = line[i]
    except:
      break
  return (x, y)


@timer
def part1():
  tiles = {}
  for line in DATA_INPUT:
    tile = calculate_tile(line)
    # print(tile)
    x = tiles.get(tile, False)
    tiles[tile] = not x
  # print(tiles)
  return sum(x for x in tiles.values())


@timer
def part2():
  tiles = {}
  for line in DATA_INPUT:
    tile = calculate_tile(line)
    x = tiles.get(tile, False)
    tiles[tile] = not x
  for day in range(100):
    coords = set()
    for x, y in tiles.keys():
      coords.add((x, y))
      coords.add((x + 1, y))
      coords.add((x - 1, y))
      coords.add((x, y + 1))
      coords.add((x, y - 1))
      coords.add((x - 1, y + 1))
      coords.add((x + 1, y - 1))
    tmp = dict(tiles)
    for c in coords:
      adj = check_adj(tmp, c)
      if tiles.get(c, False) and (adj == 0 or adj > 2):
        tiles[c] = not tiles.get(c, False)
      elif not tiles.get(c, False) and adj == 2:
        tiles[c] = not tiles.get(c, False)
  return sum(x for x in tiles.values())


if __name__ == "__main__":
  print(part1())
  print(part2())
