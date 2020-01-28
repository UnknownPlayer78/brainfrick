import setuptools
from brainfrick import __version__

with open("README.md", "r") as f:
    long_description = f.read()

script_bin = "bin/brainfrick"

setuptools.setup(
    name="brainfrick",
    version=__version__,
    author="UnknownPlayer78, nddk10",
    author_email="info@tearlabs.xyz",
    description="A simple brainfuck interpreter and debugger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    scripts=[script_bin],
    #install_requires=requirements,
    url="https://github.com/UnknownPlayer78/brainfrick",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Freeware",
        "Operating System :: Unix",
    ]
)
