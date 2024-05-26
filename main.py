"""Main tester script"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import cmath
import os
import sys
import time

from pyperclip import copy

from tester_class_03 import TesterClass03, TesterClass04

# from PySide6.QtGui import QColor

if sys.version_info < (3, 11):
  from typing_extensions import Never
else:
  from typing import Never, Callable

from tester_class_01 import Point
from tester_class_02 import Test
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


def tester05() -> None:
  """Testing EZData"""
  test = Test()
  print(test)
  test.name = 'John Dee Znuts'
  test.age = 43
  test.hasSwag = True
  test.value = 1.0
  test.score = 420 + 69j
  print(test)
  print(cmath.phase(test.score))

  lol = Test()
  lol.name = 'bob'
  lol.name = 7
  lol.hasSwag = False
  test.value = 1.5
  lol.score = 69 + 420j
  print(lol)


def tester06() -> None:
  """MineCraft 1.20.6 FTW!"""
  red, green, blue = 144, 255, 0
  colNum = red * 2 ** 16 + green * 2 ** 8 + blue
  print(colNum)


def tester07() -> None:
  """MineCraft 1.20.6 FTW!"""
  test = TesterClass03()
  test2 = TesterClass04()
  print(test.__class__)
  print(test2.__class__)


def tester08() -> None:
  """FUCK YOU"""
  fileId = '/home/AsgerJon/lmao.txt'
  data = None
  lines = []
  with open(fileId, 'r', encoding='utf8') as f:
    data = f.readlines()
    for line in data:
      if '6.7.1' in line:
        lines.append(line.replace('\n', ''))
  for item in lines:
    print('|%s|' % item)
  fuck = '\n'.join(lines)
  copy(fuck)


def main(callMeMaybe: Callable) -> None:
  """Main Tester Script"""
  tic = time.perf_counter_ns()
  print('Running python script located at: \n%s' % sys.argv[0])
  print('Running function: %s' % callMeMaybe.__name__)
  print('Started at: %s' % time.ctime())
  print(77 * '-')
  retCode = 0
  try:
    retCode = callMeMaybe()
  except BaseException as exception:
    print('Exception: %s' % exception)
    retCode = -1
    raise exception
  retCode = 0 if retCode is None else retCode
  print(77 * '-')
  print('Return Code: %s' % retCode)
  toc = time.perf_counter_ns() - tic
  print('Runtime: %.3E seconds' % (toc * 1e-09,))


if __name__ == '__main__':
  main(tester08)
