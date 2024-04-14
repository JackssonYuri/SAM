from sys import *
from os import *

from compiler.compiler import Compiler

examples_path : str = 'examples/input'

filenames : list = []

compiler : Compiler



if __name__ == '__main__':

    if len(argv) == 1:

        for path in listdir(examples_path):

            filenames.append(path)

    
    elif len(argv) > 1:

        filenames = argv.copy()

        filenames.pop()


    
    compiler = Compiler(filenames)

    compiler.compile()