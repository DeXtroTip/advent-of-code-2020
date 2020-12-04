#!/usr/bin/env python
"""
--- Day 4: Passport Processing ---
https://adventofcode.com/2020/day/4

Rank: 1672 / 801
"""
import re

from aocutils import read_input, timer

DATA_INPUT = read_input('04', cast='str')


def parse_passports():
  data = DATA_INPUT + ['']
  passports = []
  current = {}
  for line in data:
    if not len(line):
      passports.append(current)
      current = {}
      continue
    for token in line.split(' '):
      t1, t2 = token.split(':')
      current[t1] = t2
  return passports


def is_valid_passport_1(passport):
  return set(passport.keys()).issuperset({'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'})


def is_valid_passport_2(passport):
  field = passport.get('byr', '')
  if not ((match := re.match('^(\\d{4})$', field)) and 1920 <= int(match.group(1)) <= 2002):  # noqa
    return False
  field = passport.get('iyr', '')
  if not ((match := re.match('^(\\d{4})$', field)) and 2010 <= int(match.group(1)) <= 2020):  # noqa
    return False
  field = passport.get('eyr', '')
  if not ((match := re.match('^(\\d{4})$', field)) and 2020 <= int(match.group(1)) <= 2030):  # noqa
    return False
  field = passport.get('hgt', '')
  if not (((match := re.match('^(\\d+)cm$', field)) and 150 <= int(match.group(1)) <= 193) or  # noqa
          ((match := re.match('^(\\d+)in$', field)) and 59 <= int(match.group(1)) <= 76)):  # noqa
    return False
  field = passport.get('hcl', '')
  if re.match('^#[0-9a-f]{6}$', field) is None:
    return False
  field = passport.get('ecl', '')
  if field not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
    return False
  field = passport.get('pid', '')
  if re.match('^\\d{9}$', field) is None:
    return False
  return True


@timer
def part1():
  return sum(is_valid_passport_1(p) for p in parse_passports())


@timer
def part2():
  return sum(is_valid_passport_2(p) for p in parse_passports())


if __name__ == "__main__":
  print(part1())
  print(part2())
