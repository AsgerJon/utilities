"""This module contains tests for the Stream class. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from io import StringIO
import unittest

from vistutils.dirs import Stream


class StreamTests(unittest.TestCase):
  def writingToStreamCapturesOutput(self) -> None:
    """
    Test that writing to the stream captures the output.
    """
    # Arrange
    stream: Stream = Stream(StringIO())
    # Act
    stream.write("Hello, World!")
    # Assert
    self.assertEqual(stream.collect(), ["Hello, World!"])

  def readingFromStreamCapturesOutput(self) -> None:
    """
    Test that reading from the stream captures the output.
    """
    # Arrange
    input_stream: StringIO = StringIO("Hello, World!")
    stream: Stream = Stream(input_stream)
    # Act
    stream.read()
    # Assert
    self.assertEqual(stream.collect(), ["Hello, World!"])

  def multipleWritesAreCapturedInOrder(self) -> None:
    """
    Test that multiple writes to the stream are captured in order.
    """
    # Arrange
    stream: Stream = Stream(StringIO())
    # Act
    stream.write("Hello,")
    stream.write(" World!")
    # Assert
    self.assertEqual(stream.collect(), ["Hello,", " World!"])

  def multipleReadsAreCapturedInOrder(self) -> None:
    """
    Test that multiple reads from the stream are captured in order.
    """
    # Arrange
    input_stream: StringIO = StringIO("Hello,\nWorld!")
    stream: Stream = Stream(input_stream)
    # Act
    stream.read(6)
    stream.read()
    # Assert
    self.assertEqual(stream.collect(), ["Hello,", "\nWorld!"])

  def collectDoesNotClearTheCaptureList(self) -> None:
    """
    Test that calling collect does not clear the capture list.
    """
    # Arrange
    stream: Stream = Stream(StringIO())
    # Act
    stream.write("Hello, World!")
    stream.collect()
    # Assert
    self.assertEqual(stream.collect(), ["Hello, World!"])
