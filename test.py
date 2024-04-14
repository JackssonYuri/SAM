from sys import *
from os import *

from compiler.compiler import Compiler



examples_path : str = 'examples/input'

filenames : list = []

compiler : Compiler



if __name__ == '__main__':

    for path in listdir(examples_path):

        filenames.append(path)

    
    compiler = Compiler(filenames)

    compiler.compile()

    
    

    
