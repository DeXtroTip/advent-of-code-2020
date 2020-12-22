#!/usr/bin/env python
"""
--- Day 21: ... ---
https://adventofcode.com/2020/day/21

Rank: 1497 / 1253
"""
import functools
import json
import re
from queue import Queue

from aocutils import *

DATA_INPUT = read_input('21', cast='str')
# DATA_INPUT = read_input('21t', cast='str')


def parse_input(line):
  tokens = line.split('(')
  ingredients = set(tokens[0].strip().split(' '))
  allergens = tokens[1].strip()[9:-1].split(', ')
  return ingredients, allergens


@timer
def part1():
  data = [parse_input(line) for line in DATA_INPUT]
  print(data)
  allergens = {}
  all_ingredients = {}
  for ingredients, alls in data:
    for ing in ingredients:
      x = all_ingredients.get(ing, 0)
      x += 1
      all_ingredients[ing] = x
    for a in alls:
      if a not in allergens:
        allergens[a] = set(ingredients)
      else:
        allergens[a] = allergens[a].intersection(ingredients)
  not_allergens = set(all_ingredients.keys())
  for a_ings in allergens.values():
    not_allergens = not_allergens.difference(a_ings)
  print(allergens)
  print(all_ingredients)
  print(not_allergens)
  total = 0
  for ings, _ in data:
    for ing in ings:
      if ing in not_allergens:
        total += 1
  return total


@timer
def part2():
  data = [parse_input(line) for line in DATA_INPUT]
  allergens = {}
  all_ingredients = {}
  for ingredients, alls in data:
    for ing in ingredients:
      x = all_ingredients.get(ing, 0)
      x += 1
      all_ingredients[ing] = x
    for a in alls:
      if a not in allergens:
        allergens[a] = set(ingredients)
      else:
        allergens[a] = allergens[a].intersection(ingredients)
  not_allergens = set(all_ingredients.keys())
  for a_ings in allergens.values():
    not_allergens = not_allergens.difference(a_ings)
  print(allergens)
  print(all_ingredients)
  print(not_allergens)
  while any(len(x) > 1 for x in allergens.values()):
    for allergen, ings in allergens.items():
      if len(ings) > 1:
        continue
      ing = next(iter(ings))
      for a2, ings2 in allergens.items():
        if len(ings2) == 1:
          continue
        if ing in ings2:
          ings2.remove(ing)
  a_ings = []
  for allergen in sorted(allergens.keys()):
    a_ings.append(next(iter(allergens[allergen])))
  return ','.join(a_ings)


if __name__ == "__main__":
  # print(part1())
  print(part2())
