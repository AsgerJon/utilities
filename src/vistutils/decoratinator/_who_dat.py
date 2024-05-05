"""WhoDat replaces"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.decoratinator import AbstractDecorator


class WhoDat(AbstractDecorator):
  """WhoDat replaces"""

  def _apply(self, decoratedClass: type) -> type:
    """Apply the WhoDat decorator to the decorated class."""
    return decoratedClass
