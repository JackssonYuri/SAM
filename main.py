from stack.stack import *
from lexer.lexical_analysis import *

def execute(filename):
    stack = Stack()
    lexer = Lexer(filename)
    tokens = lexer.tokenize()

    for token in tokens:
        if token == 'ADD':
            operand2 = stack.pop()
            operand1 = stack.pop()

            result = operand1 + operand2
            stack.push(result)

        elif token == 'PUSH':
            tokens.pop()
            operand3 = int(tokens.pop[0])
            stack.push(operand3)

        elif token == 'STOP':
            print('oi')
            break

    print(stack.items)
filename = 'sam1.sam'
# s : Stack = Stack()

# s.pop()

# print(s.items)

execute(filename)

