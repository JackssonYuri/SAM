from stack import Stack

class Arithmetic:

    stack : Stack
    stack_temp : Stack
    tokens : list

    operand1 : int
    operand2 : int
    result : int

    accept_tokens : list = ['ADD', 'SUB', 'TIMES', 'DIV']

    def __init__(self, stack : Stack, tokens : list) -> None:
        
        self.tokens = tokens

        self.stack = stack
        self.stack_temp = Stack()

        self.operand1 = 0
        self.operand2 = 0
        self.result = 0

        if tokens.index(0) not in self.accept_tokens:
            return
        
        if tokens.index(0) == 'ADD':
            self.stack = self.add()

        elif tokens.index(0) == 'SUB':
            self.stack = self.sub()

        elif tokens.index(0) == 'TIMES':
            self.stack = self.times()

        elif tokens.index(0) == 'DIV':
            self.stack = self.div()

        

        
    def add(self) -> Stack:

        self.stack_temp : Stack = Stack()

        self.stack_temp = self.stack

        operand2 = self.stack_aux.pop()
        operand1 = self.stack_aux.pop()

        result = operand1 + operand2

        self.stack_aux.push(result)

        return self.stack_temp
    

    def sub(self) -> Stack:

        self.stack_temp : Stack = Stack()

        self.stack_temp = self.stack

        operand2 = self.stack_aux.pop()
        operand1 = self.stack_aux.pop()

        result = operand1 - operand2
        
        self.stack_aux.push(result)

        return self.stack_temp
    
    def times(self) -> Stack:

        self.stack_temp : Stack = Stack()

        self.stack_temp = self.stack

        operand2 = self.stack_aux.pop()
        operand1 = self.stack_aux.pop()

        result = operand1 * operand2
        
        self.stack_aux.push(result)

        return self.stack_temp
    
    def div(self) -> Stack:

        self.stack_temp : Stack = Stack()

        self.stack_temp = self.stack

        operand2 = self.stack_aux.pop()
        operand1 = self.stack_aux.pop()

        result = operand1 / operand2
        
        self.stack_aux.push(result)

        return self.stack_temp


    