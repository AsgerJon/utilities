"""BaseNamespace subclasses the AbstractNamespace and provides standard
dictionary behaviour, but includes logging of item accessor method calls. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from utils.metas import AbstractNamespace


class BaseNamespace(AbstractNamespace):
  """BaseNamespace subclasses the AbstractNamespace and provides standard
  dictionary behaviour, but includes logging of item accessor method
  calls. """

  def __init__(self, *args, **kwargs) -> None:
    AbstractNamespace.__init__(self, *args, **kwargs)

  def __explicit_get_item__(self, key: str, ) -> Any:
    """Implementation of item retrieval"""
    return dict.__getitem__(self, key)

  def __explicit_set_item__(self, key: str, val: Any, old: Any) -> None:
    """Implementation of item value setting"""
    return dict.__setitem__(self, key, val)

  def __explicit_del_item__(self, key: str, oldVal: Any) -> None:
    """Implementation of entry deletion. """
    return dict.__delitem__(self, key)
