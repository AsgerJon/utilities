"""Main tester script"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys
from test import Test


def tester00() -> None:
  """Hello world"""
  stuff = [os, sys, Test]
  for item in stuff:
    print(item)


if __name__ == '__main__':
  tester00()
