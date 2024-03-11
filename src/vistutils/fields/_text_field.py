"""TextField provides a strongly typed descriptor containing text."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any, Self

from vistutils.fields import MutableDescriptor


class _TextWrap:
  """This class wraps the string class providing compatibility with the
  TextField descriptor."""

  def getDefault(self, *args, **kwargs) -> Self:
    """Returns the default value for the field."""


class TextField(MutableDescriptor):
  """The TextField class provides a strongly typed descriptor containing
  text."""

  __default_value__ = None
  __fallback_value__ = ''

  def __init__(self, *args, **kwargs) -> None:
    MutableDescriptor.__init__(self, str, *args, **kwargs)
    for arg in args:
      if isinstance(arg, str) and self.__default_value__ is None:
        self.__default_value__ = arg
        break

  def __get__(self, instance: object, owner: type, **kwargs) -> str:
    """Returns the value of the descriptor."""
    pvtName = self._getPrivateName()
    if getattr(instance, pvtName, None) is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      setattr(instance, pvtName, self.__default_value__)
      return self.__get__(instance, owner, _recursion=True)
    val = getattr(instance, pvtName)
    if isinstance(val, str):
      return val
    return str(val)

  def __set__(self, instance: object, value: Any) -> None:
    """Sets the value of the descriptor."""
    pvtName = self._getPrivateName()
    if not isinstance(value, str):
      value = str(value)
    setattr(instance, pvtName, value)
