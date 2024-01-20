"""This file add the src folder to the path where python is looking for
modules."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys


class Test:
  """Importing this class adds src to the path where python is looking for
  modules."""
  here = os.path.dirname(os.path.abspath(__file__))
  sys.path.append(os.path.join(here, 'src'))
