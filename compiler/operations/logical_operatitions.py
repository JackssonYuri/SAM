from compiler.instructions import Instructions

class Logical:

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

        
        if self.linetokens[0] == 'NOT':
            self.instructions = self.not_op()

        elif self.linetokens[0] == 'OR':
            self.instructions = self.or_op()

        elif self.linetokens[0] == 'AND':
            self.instructions = self.and_op()

        


    def not_op(self) -> Instructions:
        pass
    

    def or_op(self) -> Instructions:
        pass
    
    def and_op(self) -> Instructions:
        pass