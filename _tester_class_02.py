"""Tester class 02"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.fields import TypedField


class Test02:
  """LOL"""
  x = TypedField(7)
  y = TypedField(int)
  z = TypedField(type=int, defVal=7)

  def __str__(self) -> str:
    """String representation"""
    return '(%d, %d, %d)' % (self.x, self.y, self.z)
