"""Tester class 02"""
#  GPL-3.0 license
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
    data = [self.name, self.age, self.hasSwag, self.value, self.score]
    keys = ['name', 'age', 'hasSwag', 'value', 'score']
    n = max([len(key) for key in keys])
    fmtSpec = '%%%ds: %%s' % (n + 1)
    lines = [fmtSpec % (key, data) for key, data in zip(keys, data)]
    return '\n'.join(lines)
