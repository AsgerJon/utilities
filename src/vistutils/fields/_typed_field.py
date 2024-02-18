"""TypedField provides a strongly typed descriptor class"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.fields import AbstractField
from vistutils.waitaminute import typeMsg


class TypedField(AbstractField):
  """TypedField provides a strongly typed descriptor class"""

  @classmethod
  def _parseArgs(cls, *args, **kwargs) -> dict:
    """Parses the positional arguments"""
    defVal = None
    valType = None
    if len(args) > 2:
      e = """The TypedField constructor takes 1 to 2 positional 
      arguments, but received: %d""" % len(args)
      raise TypeError(e)
    defKeys = stringList("""defaultValue, value type""")

  def __init__(self, *args, **kwargs) -> None:
    AbstractField.__init__(self, *args)
    _parsed = self._parseArgs(*args, **kwargs)
    self.__value_type__ = None

  def getType(self, ) -> type:
    """Getter-function for the type"""
    return self.__type__

  def __set__(self, instance: object, value: Any) -> None:
    """Set the value of the field"""
    if not isinstance(value, self.__type__):
      raise TypeError(f"Value '{value}' is not of type '{self.__type__}'")
    super().__set__(instance, value)
