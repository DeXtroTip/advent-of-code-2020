#!/usr/bin/env python
"""
--- Day 20: Jurassic Jigsaw ---
https://adventofcode.com/2020/day/20

Rank: 4112 / 1567
"""
import functools
import json
import re
from queue import Queue

from aocutils import *

DATA_INPUT = read_input('20', cast='str')
# DATA_INPUT = read_input('20t', cast='str')

MONSTER = [
  '                  # ',
  '#    ##    ##    ###',
  ' #  #  #  #  #  #   ',
]


def generate_tile_variations(tile, size):
  variations = {}
  curr_variation = dict(tile)
  for i in range(4):
    new_var = {}
    flipped_x = {}
    flipped_y = {}
    for (x, y), w in curr_variation.items():
      new_var[(-y + size - 1, x)] = w
    for (x, y), w in new_var.items():
      flipped_x[(-x + size - 1, y)] = w
      flipped_y[(x, -y + size - 1)] = w
    variations[(i, 0)] = new_var
    variations[(i, 1)] = flipped_x
    variations[(i, 2)] = flipped_y
    curr_variation = new_var
  return variations


def try_match(var1, var2):
  matches = []
  for m in ('up', 'down', 'right', 'left'):
    if m == 'up':
      if all(var1[(i, 0)] == var2[(i, TILE_SIZE - 1)] for i in range(TILE_SIZE)):
        matches.append(m)
    elif m == 'down':
      if all(var1[(i, TILE_SIZE - 1)] == var2[(i, 0)] for i in range(TILE_SIZE)):
        matches.append(m)
    elif m == 'right':
      if all(var1[(TILE_SIZE - 1, i)] == var2[(0, i)] for i in range(TILE_SIZE)):
        matches.append(m)
    elif m == 'left':
      if all(var1[(0, i)] == var2[(TILE_SIZE - 1, i)] for i in range(TILE_SIZE)):
        matches.append(m)
  return matches


def is_corner(pos_x, pos_y):
  return (pos_x, pos_y) == (0, 0) or (pos_x, pos_y) == (IMAGE_SIZE - 1, 0) or (pos_x, pos_y) == (0, IMAGE_SIZE - 1) \
    or (pos_x, pos_y) == (IMAGE_SIZE - 1, IMAGE_SIZE - 1)


def is_edge(pos_x, pos_y):
  return pos_x == 0 or pos_x == IMAGE_SIZE - 1 or pos_y == 0 or pos_y == IMAGE_SIZE - 1


def find_tile(pos_x, pos_y, used_tiles, last_var, match):
  if pos_y == IMAGE_SIZE:
    global USED_TILES
    USED_TILES = list(used_tiles)
    return {}

  next_x = pos_x
  next_y = pos_y
  next_match = match

  if next_match == 'right':
    next_x += 1
  elif next_match == 'left':
    next_x -= 1
  elif next_match == 'down' and next_x == IMAGE_SIZE - 1:
    next_x -= 1
    next_match = 'left'
  elif next_match == 'down' and next_x == 0:
    next_x += 1
    next_match = 'right'

  if next_x == -1:
    next_match = 'down'
    next_y += 1
    next_x = 0
  elif next_x == IMAGE_SIZE:
    next_match = 'down'
    next_y += 1
    next_x = IMAGE_SIZE - 1

  for tile_id, variations in TILE_VARIATIONS.items():
    if tile_id in used_tiles:
      continue
    possible_variations = set()
    for v_id, edges in TILE_EDGES[tile_id].items():
      if is_corner(pos_x, pos_y):
        if len(edges) == 2:
          possible_variations.add(v_id)
      elif is_edge(pos_x, pos_y):
        if len(edges) == 3:
          possible_variations.add(v_id)
      else:
        if len(edges) == 4:
          possible_variations.add(v_id)
    for i, v in enumerate(variations):
      if i not in possible_variations:
        continue
      if not last_var or match in try_match(last_var, v):
        next_tiles = find_tile(next_x, next_y, used_tiles + [tile_id], v, next_match)
        if next_tiles is not None:
          return {(pos_x, pos_y): v, **next_tiles}
  return None


def count_monsters(image):
  max_x = int(max(x for (x, y) in image.keys()))
  max_y = int(max(y for (x, y) in image.keys()))
  monsters = 0
  for y in range(max_y + 2 - len(MONSTER)):
    for x in range(max_x + 2 - len(MONSTER[0])):
      is_monster = all(MONSTER[iy][ix] == ' ' or (MONSTER[iy][ix] == '#' and image[(x + ix, y + iy)] == '#')
                       for iy in range(len(MONSTER)) for ix in range(len(MONSTER[0])))
      if is_monster:
        monsters += 1
  return monsters


@timer
def part1():
  find_tile(0, 0, [], {}, 'right')
  return functools.reduce(lambda x, y: x * y,
                          [USED_TILES[0], USED_TILES[IMAGE_SIZE - 1], USED_TILES[-IMAGE_SIZE], USED_TILES[-1]])


@timer
def part2():
  image_tiles = find_tile(0, 0, [], {}, 'right')
  image = {}
  i = 0
  j = 0
  for c, (tile_id, tile) in enumerate(image_tiles.items()):
    for (x, y), w in tile.items():
      if x in (0, TILE_SIZE - 1) or y in (0, TILE_SIZE - 1):
        continue
      image[((x - 1) + i * (TILE_SIZE - 2), (y - 1) + j * (TILE_SIZE - 2))] = w
    i += 1 if j % 2 == 0 else -1
    if i == IMAGE_SIZE:
      i -= 1
      j += 1
    elif i == -1:
      i += 1
      j += 1
  image_variations = list(generate_tile_variations(image, IMAGE_SIZE * (TILE_SIZE - 2)).values())
  for i, var in enumerate(image_variations):
    monsters = count_monsters(var)
    if monsters:
      return sum(o == '#' for o in var.values()) - monsters * sum(o == '#' for line in MONSTER for o in line)


USED_TILES = []
TILE_MAP = {}
for line in DATA_INPUT:
  if not line:
    continue
  if line.startswith('Tile'):
    tile_id = int(line[:-1].split(' ')[1])
    TILE_MAP[tile_id] = {}
    i = 0
  else:
    TILE_SIZE = len(line)
    for j in range(len(line)):
      TILE_MAP[tile_id][(j, i)] = line[j]
    i += 1
IMAGE_SIZE = int(len(TILE_MAP)**0.5)

TILE_VARIATIONS = {
  tile_id: list(generate_tile_variations(tile, TILE_SIZE).values())
  for tile_id, tile in TILE_MAP.items()
}

TILE_EDGES = {}
for tile_id, variations in TILE_VARIATIONS.items():
  edges = {i: set() for i in range(len(variations))}
  for o_tid, o_vars in TILE_VARIATIONS.items():
    if tile_id == o_tid:
      continue
    for i, v1 in enumerate(variations):
      for v2 in o_vars:
        if try_match(v1, v2):
          edges[i].add(o_tid)
          break
  TILE_EDGES[tile_id] = edges

if __name__ == "__main__":
  print(part1())
  print(part2())
