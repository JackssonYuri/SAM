from .io import IO
from .operations.operations import Operations
from .instructions import *
from .stack import *
from .lexical.lexical import *

class Compiler:

    io : IO
    instructions : Instructions
    lexical : Lexical
    operations : Operations
    filenames : list
    result_operations : Instructions
    result_lexical : list


    def __init__(self) -> None:

        self.io = IO()

        self.filenames = self.io.input()

    
    def compile(self) -> None:

        for filename in self.filenames:

            self.instructions = Instructions()
            
            self.lexical = Lexical(filename)
            self.result_lexical = self.lexical.filetokens()

            self.operations = Operations(self.instructions, self.result_lexical)

            self.result_operations = self.operations.execute()

            self.io.print(filename, self.result_operations)
            self.io.output(filename, self.result_operations)



            


            


        


    


