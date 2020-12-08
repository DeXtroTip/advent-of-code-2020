from typing import Dict, List, Optional, Set, Tuple


class BootCodeVM:
  ACC = 'acc'
  JMP = 'jmp'
  NOP = 'nop'

  OPERATIONS: Dict[str, int] = {
    ACC: 1,
    JMP: 1,
    NOP: 1,
  }

  raw_code: List[str]
  code: List[Tuple[str, Tuple[int, ...]]]
  instructions: Dict[int, Tuple[str, Tuple[int, ...]]]

  global_accumulator: int
  instruction_pointer: int

  instructions_ran = Set[int]

  is_infinite_loop: bool

  def __init__(self, raw_code: List[Tuple[str, int]]) -> None:
    self.raw_code = raw_code[::]
    self._parse_code()
    self._initialize()

  def _parse_code(self) -> None:
    self.code = []
    for line in self.raw_code:
      inst, arg = line.split(' ')
      arg = int(arg)
      self.code.append((inst, (arg, )))

  def _initialize(self) -> None:
    self._init_instructions_from_code()
    self.global_accumulator = 0
    self.instruction_pointer = 0
    self.instructions_ran = set()
    self.is_infinite_loop = False

  def _init_instructions_from_code(self) -> None:
    self.instructions = {i: instruction for i, instruction in enumerate(self.code)}

  def instruction_get(self, index: int) -> Tuple[str, int]:
    return self.instructions.get(index, 0)

  def instruction_set(self, index: int, inst: Tuple[str, int]) -> None:
    self.instructions[index] = inst

  def reset(self) -> None:
    self._initialize()

  def run(self) -> Optional[int]:
    while self.instruction_pointer in self.instructions:
      if self.instruction_pointer in self.instructions_ran:
        self.is_infinite_loop = True
        return None

      instr = self.instruction_get(self.instruction_pointer)
      op, args = instr

      if op not in BootCodeVM.OPERATIONS:
        raise Exception(f"Invalid operation: {op}")
      # num_args = BootCodeVM.OPERATIONS.get(op)

      self.instructions_ran.add(self.instruction_pointer)
      self.instruction_pointer += 1

      if op == BootCodeVM.ACC:
        val = args[0]
        self.global_accumulator += val
      elif op == BootCodeVM.NOP:
        pass
      elif op == BootCodeVM.JMP:
        val = args[0]
        self.instruction_pointer += val - 1
      else:
        raise Exception(f"Invalid operation: {op}")

    return self.global_accumulator
