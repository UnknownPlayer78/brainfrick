from .__main__ import __version__
from .interpreter import Interpreter

def main(argv):
    file = " ".join(argv)
    bf = Interpreter(file=file)
    bf.run()