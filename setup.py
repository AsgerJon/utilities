import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vistutils",
    version="0.0.1",
    author="Asger Jon Vistisen",
    description="Helpful utility functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    py_modules=["vistutils"],
    package_dir={'':'vistutils/src'},
    install_requires=[]
)
