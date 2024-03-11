"""Tester class 02"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.fields import TextField, IntField, Flag, FloatField, \
  ComplexField


class Test:
  """Test if the stuff works lol"""

  name = TextField('John Doe')
  age = IntField(42)
  hasSwag = Flag(False)
  value = FloatField(0.0)
  score = ComplexField(69 + 420j)

  def __str__(self, ) -> str:
    """Let's list all the descriptor fields right here!"""
    return (f'{self.name=}, {self.age=}, {self.hasSwag=}, {self.value=}, '
            f'{self.score=}')
