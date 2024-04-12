"""Tester class 01"""
#  GPL-3.0 license
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
