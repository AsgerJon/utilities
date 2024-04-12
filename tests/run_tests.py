"""Script running the tests for the project."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
import unittest
from vistutils.dirs import Dream

with Dream(unittest.main,
           module='__main__',
           buffer=True,
           exit=False) as dream:
  dream.IN = 'latest_test_in.log'
  dream.OUT = 'latest_test_out.log'
  dream.ERR = 'latest_test_err.log'
