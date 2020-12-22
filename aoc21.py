#!/usr/bin/env python
"""
--- Day 21: ... ---
https://adventofcode.com/2020/day/21

Rank: 1497 / 1253
"""
from aocutils import read_input, timer

DATA_INPUT = read_input('21', cast='str')


def parse_input(line):
  tokens = line.split('(')
  ingredients = set(tokens[0].strip().split(' '))
  allergens = tokens[1].strip()[9:-1].split(', ')
  return ingredients, allergens


PARSED_DATA = [parse_input(line) for line in DATA_INPUT]
ALLERGENS = {}
INGREDIENTS = {}
for ings, alls in PARSED_DATA:
  for ing in ings:
    INGREDIENTS[ing] = INGREDIENTS.get(ing, 0) + 1
  for a in alls:
    ALLERGENS[a] = set(ings) if a not in ALLERGENS else ALLERGENS[a].intersection(ings)


@timer
def part1():
  not_allergens = set(ing for ing in INGREDIENTS.keys()
                      if ing not in set(a for alls in ALLERGENS.values() for a in alls))
  return sum(ing in not_allergens for ings, _ in PARSED_DATA for ing in iter(ings))


@timer
def part2():
  allergens = dict(ALLERGENS)
  while any(len(ings) > 1 for ings in allergens.values()):
    for allergen, ings in allergens.items():
      if len(ings) > 1:
        continue
      ing = next(iter(ings))
      for other_allergen, other_ings in allergens.items():
        if other_allergen != allergen and ing in other_ings:
          other_ings.remove(ing)
  return ','.join(next(iter(allergens[allergen])) for allergen in sorted(allergens.keys()))


if __name__ == "__main__":
  print(part1())
  print(part2())
