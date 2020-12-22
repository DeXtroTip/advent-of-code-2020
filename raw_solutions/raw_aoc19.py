#!/usr/bin/env python
"""
--- Day 19: Monster Messages ---
https://adventofcode.com/2020/day/19

Rank: 1882 / 1239
"""
import functools
import json
import re
from queue import Queue

from aocutils import *

DATA_INPUT = read_input('19', cast='str')
# DATA_INPUT = read_input('19t', cast='str')

RULES = {}


@functools.lru_cache
def is_valid_rule(msg, rule):
  rule_char = RULES[rule].get('char')
  if rule_char is not None:
    return [msg[1:]] if msg and msg[0] == rule_char else []
  subrules = RULES[rule].get('subrules')
  valids = []
  for subrule in subrules:
    msgs = [msg]
    for r in subrule:
      tmp_msgs = []
      for m in msgs:
        tmp_msgs += is_valid_rule(m, r)
      msgs = tmp_msgs
      if not msgs:
        break
    if msgs:
      valids += msgs
  return valids


@timer
def part1():
  data = [line for line in DATA_INPUT]
  valid_msgs = []
  invalid_msgs = []
  is_msg = False
  for line in data:
    if not line:
      is_msg = True
      continue
    if not is_msg:
      i, r = line.split(':')
      if '"' in r:
        r = r.replace('"', '').strip()
        RULES[int(i)] = {'char': r}
      else:
        RULES[int(i)] = {'subrules': []}
        subrules = r.strip().split('|')
        for sr in subrules:
          parts = sr.strip().split(' ')
          x = tuple(int(y) for y in parts)
          RULES[int(i)]['subrules'].append(x)
    else:
      is_valid = is_valid_rule(line, 0)
      if '' in is_valid:
        valid_msgs.append(line)
      else:
        invalid_msgs.append(line)
  return len(valid_msgs)


@timer
def part2():
  RULES[8]['subrules'] = [(42, ), (42, 8)]
  RULES[11]['subrules'] = [(42, 31), (42, 11, 31)]
  data = [line for line in DATA_INPUT]
  valid_msgs = []
  invalid_msgs = []
  is_msg = False
  for line in data:
    if not line:
      is_msg = True
      continue
    if not is_msg:
      pass
    else:
      is_valid = is_valid_rule(line, 0)
      if '' in is_valid:
        valid_msgs.append(line)
      else:
        invalid_msgs.append(line)
  return len(valid_msgs)


if __name__ == "__main__":
  print(part1())
  print(part2())
