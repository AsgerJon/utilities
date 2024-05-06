"""TesterClass03"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from types import MethodType

from vistutils.decoratinator import WhoDat


class YOLO:
  """YOLO class"""

  def __call__(self, cls: type) -> type:
    """Call"""

    def __func__(this, ) -> str:
      print(this)
      return getattr(this, '__qualname__', )

    setattr(cls, '__str__', MethodType(__func__, cls))

    return cls


@YOLO()
class TesterClass03:
  """Tester class 03"""


class TesterClass04:
  """LMAO"""
