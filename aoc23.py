#!/usr/bin/env python
"""
--- Day 23: Crab Cups ---
https://adventofcode.com/2020/day/23

Rank: 1681 / 3944
"""
from aocutils import read_input, timer

# TODO: Not reviewed from raw solution

DATA_INPUT = read_input('23', cast='str')[0]


@timer
def part1():
  cups = list(DATA_INPUT)
  GOAL_MOVES = 100
  n_cups = len(cups)
  idx = 0
  for move in range(GOAL_MOVES):
    p1, p2 = cups[:idx], cups[idx + 4:]
    r = cups[idx + 1:idx + 4]
    if len(r) < 3:
      p1 = p1[(3 - len(r)):]
      r += cups[:(3 - len(r))]
    d = str(int(cups[idx]) - 1)
    while d in r or int(d) < 1:
      d = str(int(d) - 1)
      if int(d) < 1:
        d = str(n_cups)
    if d in p1:
      jdx = p1.index(d)
      p1 = p1[:jdx + 1] + r + p1[jdx + 1:]
      if len(p1) > idx:
        p2 += p1[:len(p1) - idx]
        p1 = p1[len(p1) - idx:]
    else:
      jdx = p2.index(d)
      p2 = p2[:jdx + 1] + r + p2[jdx + 1:]
    cups = p1 + [cups[idx]] + p2
    idx = (idx + 1) % n_cups
  x = cups.index('1')
  return ''.join(cups[x + 1:] + cups[:x])


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

  def insert(self, node, n=1):
    aux = node
    for _ in range(n - 1):
      aux = aux.next
    self.next, aux.next = node, self.next


@timer
def part2():
  GOAL_MOVES = 10000000
  cups = {int(v): Node(int(v)) for v in DATA_INPUT}
  for n in range(10, 1000001):
    cups[n] = Node(n)
  n_cups = len(cups)
  for c1, c2 in zip(list(cups.values()), list(cups.values())[1:]):
    c1.next = c2
  cups[1000000].next = cups[int(DATA_INPUT[0])]
  curr = cups[int(DATA_INPUT[0])]
  for m in range(GOAL_MOVES):
    p = curr.next
    curr.next = p.next.next.next
    d = curr.val - 1
    while d < 1 or d in [p.val, p.next.val, p.next.next.val]:
      d -= 1
      if d < 1:
        d = n_cups
    curr = curr.next
    cups[d].insert(p, 3)
  aux = curr
  while True:
    if aux.val == 1:
      return aux.next.val * aux.next.next.val
    aux = aux.next


if __name__ == "__main__":
  print(part1())
  print(part2())
