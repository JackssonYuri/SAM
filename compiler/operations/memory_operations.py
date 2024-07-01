from compiler.instructions import Instructions

class Memory:

    instructions : Instructions
    instructions_temp : Instructions
    linetokens : list

    operand1 : int
    operand2 : int


    def __init__(self, instructions : Instructions, linetokens : list) -> None:
        
        self.linetokens = linetokens

        self.instructions = instructions
        self.instructions_temp = Instructions()

        self.operand1 = 0
        self.operand2 = 0

        
        if self.linetokens[0] == 'PUSHIMM':
            self.instructions = self.pushimm()

        elif self.linetokens[0] == 'DUP':
            self.instructions = self.dup()

        elif self.linetokens[0] == 'SWAP':
            self.instructions = self.swap()
        



    def pushimm(self) -> Instructions:

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        operand1 = int(self.linetokens[1])

        instructions_temp.push(operand1)

        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp
    

    def dup(self) -> Instructions:

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        operand1 = int(self.linetokens.pop())

        instructions_temp.push(operand1)
        instructions_temp.push(operand1)

        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp
    
    def swap(self) -> Instructions:

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        operand1 = int(self.linetokens.pop())
        operand2 = int(self.linetokens.pop())

        instructions_temp.push(operand2)
        instructions_temp.push(operand1)

        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp
    



    