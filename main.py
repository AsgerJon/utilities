"""Main tester script"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys

from test import Test
from vistutils import maybe, ComplexNumber


def tester00() -> None:
  """Hello world"""
  stuff = [os, sys, Test, maybe]
  for item in stuff:
    print(item)


def tester01() -> None:
  """Complex number test"""
  a = ComplexNumber(5., 4.)
  print(a)
  print(a.RE)
  print(a.IM)


if __name__ == '__main__':
  tester00()
