from compiler.instructions import Instructions

class Compare:

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


        
        if self.linetokens[0] == "GREATER":
            self.instructions = self.greater()

        elif self.linetokens[0] == "LESS":
            self.instructions = self.less()

        elif self.linetokens[0] == "EQUAL":
            self.instructions = self.equal()

        elif self.linetokens[0] == "ISNIL":
            self.instructions = self.isnil()



    def greater(self) -> Instructions:

        result : int = -1

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        operand1 = int(instructions_temp.pop())
        operand2 = int(instructions_temp.pop())

        if operand2 > operand1:

            result = 1

        elif operand2 <= operand1:

            result = 0


        instructions_temp.push(result)

        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp
    

    def less(self) -> Instructions:

        result : int = -1

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        operand1 = int(instructions_temp.pop())
        operand2 = int(instructions_temp.pop())

        if operand2 < operand1:

            result = 1

        elif operand2 >= operand1:
            
            result = 0


        instructions_temp.push(result)

        instructions_temp.pc = instructions_temp.pc + 1

        return instructions_temp
    
    def equal(self) -> Instructions:

        result : int = -1

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        operand1 = int(instructions_temp.pop())
        operand2 = int(instructions_temp.pop())

        if operand2 == operand1:

            result = 1

        elif operand2 != operand1:

            result = 0


        instructions_temp.push(result)

        instructions_temp.pc = instructions_temp.pc + 1

        

        return instructions_temp
    
    def isnil(self) -> Instructions:

        instructions_temp : Instructions = Instructions()

        instructions_temp = self.instructions

        operand1 = int(instructions_temp.pop())

        if operand1 == 0:

            result = 1

        elif operand1 != 0:

            result = 0

        instructions_temp.pc = instructions_temp.pc + 1

        instructions_temp.push(result)

        

        return instructions_temp