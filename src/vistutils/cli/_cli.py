"""CLI provides descriptors and decorators for class and instance
variables whose getter functions are terminal commands. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import subprocess
from typing import Callable, Any


class CLI:
  """The CLI class provides a method decorator to indicate that the
  decorated method is to receive the stdout and stderr from the commands
  sent to the constructor."""

  @staticmethod
  def _cleanString(msg: str) -> str:
    """Returns a cleaned up version of the string"""
    return msg.replace('\t', '  ')

  def __init__(self, *args, **kwargs) -> None:
    strArgs = [arg for arg in args if isinstance(arg, str)]
    self._command = ' '.join(strArgs)
    self.__inner_function__ = None

  def __call__(self, callMeMaybe: Callable = None) -> Any:
    """Sets the inner function or if inner function is already defined,
    runs the defined command and passes stdout and stderr to inner
    function."""
    if self.__inner_function__ is None and callMeMaybe is None:
      if self._command is None:
        raise RuntimeError
      self.__inner_function__ = lambda out, err: (out, err)
      returnVal = self._invoke()
      self.__inner_function__ = None
      return returnVal
    if self.__inner_function__ is None and callable(callMeMaybe):
      self._setInnerFunction(callMeMaybe)
      return self
    return self._invoke()

  def _setInnerFunction(self, callMeMaybe: Callable) -> None:
    """Sets the inner function to given callable"""
    self.__inner_function__ = callMeMaybe

  def _invoke(self, ) -> Any:
    """Executes the command and returns the values captured by stdout and
    stderr and passes them to inner function."""

  def _run(self) -> tuple[str, str]:
    """Executes the command in the command line"""
    res = subprocess.run(self._command, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = self._cleanString(res.stdout.decode('utf-8'))
    err = self._cleanString(res.stderr.decode('utf-8'))
