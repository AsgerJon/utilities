"""TypedField requires a strongly typed field."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from vistutils.fields import AbstractField


class TypedField(AbstractField):
  """TypedField requires a strongly typed field."""

  def __instantiate_inner_class__(self, instance: Any, owner: type) -> None:
    """Instantiates the inner class. """

  def _getInnerClass(self) -> type:
    """Getter-function for the inner-class"""

  def parse(self, *args, **kwargs) -> dict:
    """Overloaded parser"""

  def __init__(self, *args, **kwargs) -> None:
    AbstractField.__init__(self, *args, **kwargs)
    self.__inner_class__ = None
    self.__inner_creator__ = None

  def __get__(self, instance: Any, owner: type, **kwargs) -> Any:
    """Getter-function implementation"""
    if instance is None:
      pass
