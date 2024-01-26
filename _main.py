"""Main tester script"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys

from vistutils.waitaminute import EffortException

if sys.version_info.minor < 11:
  from typing import NoReturn as Never
else:
  from typing import Never


def LOL_NO() -> Never:
  """LMAO"""
  raise EffortException


def tester00() -> None:
  """Hello world"""
  stuff = [os, sys, 'Hello world!', ]
  try:
    stuff.append(LOL_NO())
  except EffortException as effortException:
    stuff.append(effortException)
  for item in stuff:
    print(item)


if __name__ == '__main__':
  tester00()
