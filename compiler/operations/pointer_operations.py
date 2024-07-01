

from compiler.instructions import Instructions


class Pointer:

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

        
        if self.linetokens[0] == 'ADDSP':
            self.instructions = self.addsp()

        elif self.linetokens[0] == 'LINK':
            self.instructions = self.link()

        elif self.linetokens[0] == 'POPFBR':
            self.instructions = self.popfbr()

    def addsp(self) -> Instructions:

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        operand = int(self.linetokens[1])

        instructions_temp.pc = instructions_temp.pc + 1

        if operand > 0:

            for _ in range(0, operand):
                self.instructions.push(None)

        elif operand <= 0:
            for _ in range(operand, 0):
                self.instructions.pop()
        

        return instructions_temp

    def link(self) -> Instructions:

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions
        
        self.instructions.push(None)

        instructions_temp.fbr = instructions_temp.sp
        
        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp
    
    def popfbr(self) -> Instructions:
        
        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions
        
        self.instructions.pop()

        instructions_temp.fbr = 0

        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp