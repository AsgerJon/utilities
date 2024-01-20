"""Main tester script"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys

from icecream import ic

from _tester_class_01 import Test01
from test import Test
from vistutils import maybe
from vistutils.metas import AbstractMetaclass

ic.configureOutput(includeContext=True)


def tester00() -> None:
  """Hello world"""
  stuff = [os, sys, Test, ic, maybe]
  for item in stuff:
    print(item)


def tester01() -> None:
  """Test of __self__ on __prepare__"""
  func = AbstractMetaclass.__prepare__
  ic(getattr(func, '__self__', 'NOT FOUND!'))
  ic(getattr(func, '__func__', 'NOT FOUND!'))


def tester02() -> None:
  """Test of metaclass"""
  bla = Test01('lmao')


if __name__ == '__main__':
  tester02()
