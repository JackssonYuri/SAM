
from compiler import Compiler
from compiler.stack import Stack
from operations.arithmetic_operations import Arithmetic


class Operations:

    stack : Stack
    arithmetic : Arithmetic
    filetokens : list

    def __init__(self, stack : Stack, filetokens : list) -> None:
        
        self.stack = stack
        self.filetokens = filetokens
        self.arithmetic = Arithmetic(self.stack, '')


    def execute(self):

        for linetoken in self.filetokens():

            for token in linetoken:

                self.arithmetic = Arithmetic(self.stack, token)

#                elif tokens == 'PUSH':
#                    self.compiler.tokens.pop()
#                    operand3 = int(self.compiler.tokens.pop[0])
#                    self.compiler.stack.push(operand3)

#                elif tokens == 'STOP':
#                    print('oi')
#                    break



    



