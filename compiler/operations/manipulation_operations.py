from compiler.instructions import Instructions

class Manipulation:

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
        self.remove_size = 0


        if self.linetokens[0] == 'PUSHABS':
            self.instructions = self.pushabs()

        elif self.linetokens[0] == 'STOREABS':
            self.instructions = self.storeabs()

        elif self.linetokens[0] == 'PUSHOFF':
            self.instructions = self.pushoff()

        elif self.linetokens[0] == 'STOREOFF':
            self.instructions = self.storeoff()
        

    
    
    def pushabs(self) -> Instructions:

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        remove_size = instructions_temp.size() - int(self.linetokens[1]) - 1

        for _ in range(0, remove_size):
            operand = instructions_temp.pop()
            instructions_temp.push_tmp(operand)


        operand1 = instructions_temp.pop()

        instructions_temp.push(operand1)


        for _ in range(0, remove_size):
            operand = instructions_temp.pop_tmp()
            instructions_temp.push(operand)

        instructions_temp.push(operand1)

        instructions_temp.items_temp = []

        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp
        


    def storeabs(self) -> Instructions:

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        remove_size = instructions_temp.size() - int(self.linetokens[1]) - 1

        operand1 = instructions_temp.pop()

        for _ in range(0, remove_size):
            operand = instructions_temp.pop()
            instructions_temp.push_tmp(operand)


        instructions_temp.items_temp.pop()

        instructions_temp.push(operand1)

        for _ in range(0, remove_size - 1):
            operand = instructions_temp.pop_tmp()
            instructions_temp.push(operand)


        instructions_temp.items_temp = []

        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp

    def pushoff(self) -> Instructions:
        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        remove_size = instructions_temp.size() - int(self.linetokens[1]) - 1
        remove_size = remove_size - instructions_temp.fbr

        for _ in range(0, remove_size):
            operand = instructions_temp.pop()
            instructions_temp.push_tmp(operand)


        operand1 = instructions_temp.pop()

        instructions_temp.push(operand1)


        for _ in range(0, remove_size):
            operand = instructions_temp.pop_tmp()
            instructions_temp.push(operand)

        instructions_temp.push(operand1)

        instructions_temp.items_temp = []

        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp
    
    def storeoff(self) -> Instructions:

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        remove_size = instructions_temp.size() - int(self.linetokens[1]) - 1
        remove_size = remove_size - instructions_temp.fbr

        operand1 = instructions_temp.pop()

        for _ in range(0, remove_size):
            operand = instructions_temp.pop()
            instructions_temp.push_tmp(operand)


        instructions_temp.items_temp.pop()

        instructions_temp.push(operand1)

        for _ in range(0, remove_size - 1):
            operand = instructions_temp.pop_tmp()
            instructions_temp.push(operand)


        instructions_temp.stack_temp = []

        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp