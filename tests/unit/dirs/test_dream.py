"""This module contains unit tests for the Dream class in the
vistutils.dirs module.

Each method in the Dream class has a corresponding test method in this
module.
The tests cover both the happy path and edge cases, ensuring that the
Dream class
functions as expected in a variety of scenarios.

The tests make use of the unittest and 'unittest.mock' libraries for
creating the test
cases and mocking the necessary objects and methods, respectively."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

from vistutils.dirs import Dream, getProjectRoot


class DreamTests(unittest.TestCase):
  def defaultLogDirReturnsProjectRootWhenNotSet(self) -> None:
    """
    Test that the default log directory returns the project root when not
    set.
    """
    dream = Dream(lambda: None)
    with patch('os.path.isabs', return_value=True):
      self.assertEqual(dream._defaultLogDir(), getProjectRoot())

  def defaultLogDirRaisesErrorWhenNotAbsolute(self) -> None:
    """
    Test that the default log directory raises an error when not absolute.
    """
    dream = Dream(lambda: None)
    dream.__default_log_dir__ = "relative/path"
    with self.assertRaises(NotADirectoryError):
      dream._defaultLogDir()

  def outLogPathReturnsAbsoluteWhenSet(self) -> None:
    """
    Test that the out log path returns absolute when set.
    """
    dream = Dream(lambda: None)
    dream.outLogFile = "/absolute/path"
    self.assertEqual(dream._outLogPath(), "/absolute/path")

  def outLogPathRaisesErrorWhenRecursionOccurs(self) -> None:
    """
    Test that the out log path raises an error when recursion occurs.
    """
    dream = Dream(lambda: None)
    dream.outLogFile = "relative/path"
    with self.assertRaises(RecursionError):
      dream._outLogPath(_recursion=True)

  def inLogPathReturnsAbsoluteWhenSet(self) -> None:
    """
    Test that the in log path returns absolute when set.
    """
    dream = Dream(lambda: None)
    dream.inLogFile = "/absolute/path"
    self.assertEqual(dream._inLogPath(), "/absolute/path")

  def inLogPathRaisesErrorWhenRecursionOccurs(self) -> None:
    """
    Test that the in log path raises an error when recursion occurs.
    """
    dream = Dream(lambda: None)
    dream.inLogFile = "relative/path"
    with self.assertRaises(RecursionError):
      dream._inLogPath(_recursion=True)

  def errLogPathReturnsAbsoluteWhenSet(self) -> None:
    """
    Test that the err log path returns absolute when set.
    """
    dream = Dream(lambda: None)
    dream.errLogFile = "/absolute/path"
    self.assertEqual(dream._errLogPath(), "/absolute/path")

  def errLogPathRaisesErrorWhenRecursionOccurs(self) -> None:
    """
    Test that the err log path raises an error when recursion occurs.
    """
    dream = Dream(lambda: None)
    dream.errLogFile = "relative/path"
    with self.assertRaises(RecursionError):
      dream._errLogPath(_recursion=True)

  def enterMethodSetsStreams(self) -> None:
    """
    Test that the enter method sets the streams.
    """
    dream = Dream(lambda: None)
    with dream:
      self.assertEqual(sys.stdin, dream.strIn)
      self.assertEqual(sys.stdout, dream.strOut)
      self.assertEqual(sys.stderr, dream.strErr)

  def exitMethodResetsStreamsAndWritesLogs(self) -> None:
    """
    Test that the exit method resets the streams and writes logs.
    """
    dream = Dream(lambda: None)
    with patch('builtins.open', new_callable=MagicMock) as mock_open:
      dream.__exit__(None, None, None)
      self.assertEqual(sys.stdin, sys.__stdin__)
      self.assertEqual(sys.stdout, sys.__stdout__)
      self.assertEqual(sys.stderr, sys.__stderr__)
      self.assertEqual(mock_open.call_count, 3)

  @staticmethod
  def callMethodCallsMainFunction() -> None:
    """
    Test that the call method calls the main function.
    """
    main_func = MagicMock()
    dream = Dream(main_func)
    dream()
    main_func.assert_called_once()

  @staticmethod
  def posMethodCallsMainFunctionWhenNotCalled() -> None:
    """
    Test that the pos method calls the main function when not called.
    """
    errors = []
    main_func = MagicMock()
    dream = Dream(main_func)
    try:
      +dream
    except AttributeError as attributeError:
      errors.append(attributeError)
    main_func.assert_called_once()

  def posMethodRaisesErrorWhenRecursionOccurs(self) -> None:
    """
    Test that the pos method raises an error when recursion occurs.
    """
    dream = Dream(lambda: None)
    with self.assertRaises(RecursionError):
      dream.__pos__(_recursion=True)

  def matmulMethodSetsEnvironmentVariables(self) -> None:
    """
    Test that the matmul method sets environment variables.
    """
    dream = Dream(lambda: None)
    dream @ {"VAR": "value"}
    self.assertEqual(os.environ["VAR"], "value")

  def matmulMethodReadsEnvironmentFromFile(self) -> None:
    """
    Test that the matmul method reads environment from file.
    """
    dream = Dream(lambda: None)
    with patch('builtins.open', new_callable=MagicMock) as mock_open:
      mock_open.return_value.__enter__.return_value = ["VAR=value\n"]
      dream @ "env_file"
      self.assertEqual(os.environ["VAR"], "value")

  def matmulMethodRaisesErrorWhenFileNotFound(self) -> None:
    """
    Test that the matmul method raises an error when file not found.
    """
    dream = Dream(lambda: None)
    with self.assertRaises(FileNotFoundError):
      dream @ "non_existent_file"
