#!/usr/bin/env python
"""
--- Day 22: Crab Combat ---
https://adventofcode.com/2020/day/22

Rank: 4628 / 3082
"""
from aocutils import read_input, timer

DATA_INPUT = read_input('22', cast='str')

PLAYERS = {1: [], 2: []}
curr_player = 1
for line in DATA_INPUT:
  if line.startswith('Player'):
    continue
  if not line:
    curr_player = 2
  else:
    PLAYERS[curr_player].append(int(line))


def game(d1, d2, has_recursive=False):
  previous = set()
  while d1 and d2:
    m = (tuple(d1), tuple(d2))
    if m in previous:
      return (1, d1)
    previous.add(m)

    c1, d1 = d1[0], d1[1:]
    c2, d2 = d2[0], d2[1:]

    if has_recursive and len(d1) >= c1 and len(d2) >= c2:
      winner, _ = game(list(d1[:c1]), list(d2[:c2]), has_recursive=True)
    elif c1 > c2:
      winner = 1
    else:
      winner = 2

    if winner == 1:
      d1 += [c1, c2]
    else:
      d2 += [c2, c1]
  return (1, d1) if d1 else (2, d2)


@timer
def part1():
  return sum(c * i for i, c in enumerate(game(list(PLAYERS[1]), list(PLAYERS[2]))[1][::-1], start=1))


@timer
def part2():
  return sum(c * i for i, c in enumerate(game(list(PLAYERS[1]), list(PLAYERS[2]), True)[1][::-1], start=1))


if __name__ == "__main__":
  print(part1())
  print(part2())
