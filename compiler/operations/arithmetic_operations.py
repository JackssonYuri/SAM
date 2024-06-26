from compiler.instructions import Instructions

class Arithmetic:

    instructions : Instructions
    instructions_temp : Instructions
    linetokens : list

    operand1 : int
    operand2 : int
    result : int


    def __init__(self, instructions : Instructions, linetokens : list) -> None:
        
        self.linetokens = linetokens

        self.instructions = instructions
        self.instructions_temp = Instructions()

        self.operand1 = 0
        self.operand2 = 0
        self.result = 0

        
        if self.linetokens[0] == 'ADD':
            self.instructions = self.add()

        elif self.linetokens[0] == 'SUB':
            self.instructions = self.sub()

        elif self.linetokens[0] == 'TIMES':
            self.instructions = self.times()

        elif self.linetokens[0] == 'DIV':
            self.instructions = self.div()

        

        
    def add(self) -> Instructions:

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        operand1 = int(instructions_temp.pop())
        operand2 = int(instructions_temp.pop())

        result = int(operand2 + operand1)

        instructions_temp.push(result)

        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp
    

    def sub(self) -> Instructions:

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        operand1 = int(instructions_temp.pop())
        operand2 = int(instructions_temp.pop())

        result = int(operand2 - operand1)

        instructions_temp.push(result)

        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp
    
    def times(self) -> Instructions:

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        operand1 = int(instructions_temp.pop())
        operand2 = int(instructions_temp.pop())

        result = int(operand2 * operand1)

        instructions_temp.push(result)

        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp
       
    
    def div(self) -> Instructions:

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        operand1 = int(instructions_temp.pop())
        operand2 = int(instructions_temp.pop())

        result = int(operand2 / operand1)

        instructions_temp.push(result)

        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp


    