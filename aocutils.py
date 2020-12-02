#!/usr/bin/env python
"""
Generic utils for all AOC
"""
import math
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Union


@dataclass(frozen=True)
class Point:
  """Immutable Point implementation with some utility methods, available for both 2D and 3D."""
  x: float
  y: float
  z: Optional[float] = None

  def __add__(self, other: Union['Point', Tuple]) -> 'Point':
    if isinstance(other, tuple):
      other = tuple_to_point(other)
    new_x = self.x + other.x
    new_y = self.y + other.y
    if self.is_3d() and other.is_3d():
      return Point(new_x, new_y, self.z + other.z)
    return Point(new_x, new_y)

  def __sub__(self, other: Union['Point', Tuple]) -> 'Point':
    if isinstance(other, tuple):
      other = tuple_to_point(other)
    if other.is_2d():
      return self + Point(-self.x, -self.y)
    return self + Point(-self.x, -self.y, -self.z)

  def __eq__(self, other: Any) -> bool:
    if isinstance(other, tuple):
      other = tuple_to_point(other)
    if isinstance(other, Point):
      return self.x == other.x and self.y == other.y and self.z == other.z
    return False

  def is_2d(self) -> bool:
    """Check if it is a 2D point."""
    return self.z is None

  def is_3d(self) -> bool:
    """Check if it is a 3D point."""
    return self.z is not None

  def is_integer(self) -> bool:
    """Check if the point coordinates are whole numbers."""
    return (isinstance(self.x, int) or self.x.is_integer()) \
        and (isinstance(self.y, int) or self.y.is_integer()) \
        and (self.z is None or isinstance(self.z, int) or self.z.is_integer())

  def to_tuple(self) -> Tuple[float, ...]:
    """Return a tuple as (x, y) for 2D points or (x, y, z) for 3D points."""
    if self.is_2d():
      return (self.x, self.y)
    return (self.x, self.y, self.z)

  def distance(self, other: Union['Point', Tuple]) -> float:
    """Calculates Euclidean distance for the given points."""
    if isinstance(other, tuple):
      other = tuple_to_point(other)
    distance = sum(pow(a - b, 2) for a, b in zip((self.x, self.y), (other.x, other.y)))
    if self.is_3d() and other.is_3d():
      distance += pow(self.z - other.z, 2)
    return math.sqrt(distance)

  def manhattan(self, other: Union['Point', Tuple]) -> float:
    """Calculates Manhattan distance for the given points."""
    if isinstance(other, tuple):
      other = tuple_to_point(other)
    distance = sum(abs(a - b) for a, b in zip((self.x, self.y), (other.x, other.y)))
    if self.is_3d() and other.is_3d():
      distance += abs(self.z - other.z)
    return distance


def tuple_to_point(tuple_point: Tuple[float, ...]) -> Point:
  if len(tuple_point) in (2, 3):
    return Point(*tuple_point)
  raise Exception(f"Size of given tuple {len(tuple_point)} does not represent a 2D nor a 3D point.")


def timer(func):
  """Decorator to get execution time."""
  def wrapper(*args, **kwargs):
    start = time.time() * 1000
    func_out = func(*args, **kwargs)
    print(f'Executed in {time.time() * 1000 - start} ms')
    return func_out

  return wrapper


def read_input(input_number: str, cast: str = None, strip_lines: bool = True) -> List[str]:
  """
  Read input for given challenge day and return a list with all lines.
  If strip_lines is True, then strip each line.
  """
  with open(f"inputs/input{input_number}.in") as input_file:
    if cast == 'int':
      return [int(line.strip()) if strip_lines else line for line in input_file.readlines()]
    else:
      return [line.strip() if strip_lines else line for line in input_file.readlines()]


def read_input_split_first_line(input_number: str, cast: str = None, split_char: str = ',') -> List[int]:
  """Read input for given challenge day and return first line splitted by given char and casted to int."""
  if cast == 'int':
    return [int(n) for n in read_input(input_number)[0].split(split_char)]
  else:
    return [n for n in read_input(input_number)[0].split(split_char)]


def tuple_sum(tuple_a: Tuple[float, ...], tuple_b: Tuple[float, ...]) -> Tuple[float, ...]:
  """The resulting tuple is a element sum of the given tuples."""
  return tuple(map(sum, zip(tuple_a, tuple_b)))


def lcm(*values: int) -> int:
  """Calculate the lcm for a list of given arguments."""
  if len(values) < 1:
    raise Exception('Not enough values given (minimum required: 1).')
  result = values[0]
  for val in values[1:]:
    result = result * val // math.gcd(result, val)
  return result


def get_printable_map(map_: Dict[Point, Any],
                      default_val: Optional[Any] = ' ',
                      mapping: Optional[Dict[Any, Any]] = None) -> str:
  """Get a map in a printable way for a given map of FrozenPoints (2D int only) and mapping of values."""
  if any(point.is_3d() or not point.is_integer() for point in map_.keys()):
    raise Exception('Given map does not contain only 2D integer points.')
  if len(map_) == 0:
    return ''
  out = ''
  min_x = int(min(point.x for point in map_.keys()))
  max_x = int(max(point.x for point in map_.keys()))
  min_y = int(min(point.y for point in map_.keys()))
  max_y = int(max(point.y for point in map_.keys()))
  for y_coord in range(min_y, max_y + 1):
    line = ''
    for x_coord in range(min_x, max_x + 1):
      map_val = map_.get(Point(x_coord, y_coord), default_val)
      line += str(mapping.get(map_val, map_val) if mapping is not None else map_val)
    out += line + '\n'
  return out
