#!/usr/bin/env python
"""
--- Day 19: Monster Messages ---
https://adventofcode.com/2020/day/19

Rank: 1882 / 1239
"""
import functools

from aocutils import read_input, timer

DATA_INPUT = read_input('19', cast='str')

RULES = {}
for line in DATA_INPUT[:DATA_INPUT.index('')]:
  if not line:
    break
  rule_id, rule_expr = line.split(':')
  if '"' in rule_expr:
    RULES[int(rule_id)] = rule_expr.replace('"', '').strip()
  else:
    RULES[int(rule_id)] = [
      tuple(int(subrule_id) for subrule_id in subrule.strip().split(' ')) for subrule in rule_expr.strip().split('|')
    ]


@functools.lru_cache
def match_rule(msg, rule_id):
  if isinstance(RULES[rule_id], str):
    return [msg[1:]] if msg and msg[0] == RULES[rule_id] else []
  matches = []
  for subrules in RULES[rule_id]:
    msgs = [msg]
    for rule_id in subrules:
      tmp_msgs = []
      for m in msgs:
        tmp_msgs += match_rule(m, rule_id)
      msgs = tmp_msgs
      if not msgs:
        break
    matches += msgs
  return matches


@timer
def part1():
  return sum('' in match_rule(line, 0) for line in DATA_INPUT[DATA_INPUT.index('') + 1:])


@timer
def part2():
  RULES[8] = [(42, ), (42, 8)]
  RULES[11] = [(42, 31), (42, 11, 31)]
  return sum('' in match_rule(line, 0) for line in DATA_INPUT[DATA_INPUT.index('') + 1:])


if __name__ == "__main__":
  print(part1())
  print(part2())
