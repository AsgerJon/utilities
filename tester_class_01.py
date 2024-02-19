"""Tester class 01"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.ezdata import EZData


class Point(EZData):
  """A simple point class"""
  x: float
  y: float

  def __str__(self, ) -> str:
    """String representation"""
    return '(%.3f, %.3f)' % (self.x, self.y)
