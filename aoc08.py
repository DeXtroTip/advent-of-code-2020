#!/usr/bin/env python
"""
--- Day 8: Handheld Halting ---
https://adventofcode.com/2020/day/8

Rank: 1080 / 1176
"""
from aoc2020_vm import BootCodeVM
from aocutils import read_input, timer

DATA_INPUT = read_input('08', cast='str')


@timer
def part1():
  vm = BootCodeVM(DATA_INPUT)
  vm.run()
  return vm.global_accumulator


@timer
def part2():
  vm = BootCodeVM(DATA_INPUT)
  for i, (op, arg) in vm.instructions.items():
    if op == BootCodeVM.NOP:
      vm.instruction_set(i, (BootCodeVM.JMP, arg))
    elif op == BootCodeVM.JMP:
      vm.instruction_set(i, (BootCodeVM.NOP, arg))
    else:
      continue
    result = vm.run()
    if result is not None:
      return result
    vm.reset()


if __name__ == "__main__":
  print(part1())
  print(part2())
