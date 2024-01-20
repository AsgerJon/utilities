"""TypedField provides a strongly typed descriptor class. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils import maybeType, monoSpace, stringList
from vistutils.fields import AbstractField


class TypedField(AbstractField):
  """TypedField provides a strongly typed descriptor class. """

  def __init__(self, *args, **kwargs) -> None:
    AbstractField.__init__(self, *args, **kwargs)
    valueTypeKeys = stringList("""type, type_, valueType, """)
    valueTypeArg = None
    valueTypeKwarg = searchKey(type, *valueTypeKeys, **kwargs)
    defValKeys = stringList("""default, defVal, val0, defaultValue""")
    defValArg = None
    if args:
      if len(args) == 1:
        if isinstance(args[0], type):
          valueTypeArg = args[0]
        else:
          defValArg = args[0]
      if len(args) > 1:
        for arg in args:
          if isinstance(arg, type) and valueTypeArg is None:
            valueTypeArg = arg
        if valueTypeArg is None:
          e = """If multiple positional arguments are given, at least one 
          must be a type!"""
          raise TypeError(monoSpace(e))
        for arg in args:
          if isinstance(arg, valueTypeArg) and defValArg is None:
            defValArg = arg
