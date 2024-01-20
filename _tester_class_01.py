"""Tester class"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.metas import AbstractMetaclass


class Test01(metaclass=AbstractMetaclass):
  """LOL"""

  def __init__(self, *args, **kwargs) -> None:
    self._name = None
    if args:
      self._name = args[0]
