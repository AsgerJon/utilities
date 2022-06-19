"""vistutils is a collection of modules providing helpful utility
functions"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
  name="Vistutils", version="0.0.1",
  description="""vistutils is a collection of modules providing helpful 
  utility functions""", long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/AsgerJon/vistutils",  # Optional
  author="Asger Jon Vistisen",
  author_email="asgerjon2@gmail.com",
  packages=find_packages(where="src")
)
