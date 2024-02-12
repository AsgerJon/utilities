"""Main tester script"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys
from typing import Never

from vistutils.waitaminute import typeMsg, EffortException

from test import Test
from vistutils import maybe


def LOL_NO() -> Never:
  """LMAO"""
  raise EffortException


def tester00() -> None:
  """Hello world"""
  stuff = [os, sys, Test, maybe]
  for item in stuff:
    print(item)


def tester01() -> None:
  """Complex number test"""
  e = typeMsg('lol', 69, type('LMAO', (), {}))
  print(e)


def tester02() -> None:
  """Hello world"""
  stuff = [os, sys, 'Hello world!', ]
  try:
    stuff.append(LOL_NO())
  except EffortException as effortException:
    stuff.append(effortException)
  for item in stuff:
    print(item, type(item))


if __name__ == '__main__':
  tester02()
