"""Main tester script"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys
from typing import Never

from tester_class_01 import Point
from vistutils.dirs import Dream
from vistutils.waitaminute import typeMsg, EffortException

from vistutils.parse import maybe


def LOL_NO() -> Never:
  """LMAO"""
  raise EffortException


def tester00() -> None:
  """Hello world"""
  stuff = [os, sys, maybe]
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


def tester03() -> None:
  """Let's call print from a lambda"""
  callMeMaybe = lambda hereIsMyNumber: print(hereIsMyNumber)
  callMeMaybe('So call me maybe')


def tester04() -> None:
  """Testing EZData"""
  p = Point(1, 2)
  print(p)
  p.x = 3
  p.y = 4
  print(p)
  print(p.x, p.y)


with Dream(tester04) @ 'lmao.env' as dream:
  dream()
