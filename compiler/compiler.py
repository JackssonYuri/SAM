from instructions import Instructions
from stack import *
from lexical.lexical import *

class Compiler:

    instructions : Instructions
    lexical : Lexical
    filenames : list

    def __init__(self, filenames : list) -> None:
        
        self.instructions = Instructions()
        self.lexer = Lexical('')
        
        self.filenames = filenames
    
    def compile(self) -> None:

        for filename in self.filenames:
            self.lexical = Lexical(filename)



