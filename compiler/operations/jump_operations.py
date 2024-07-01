

from compiler.instructions import Instructions


class Jump:

    instructions : Instructions
    filetokens : list
    linetokens : list

    index : int
    functions_index : dict



    def __init__(self, instructions : Instructions, filetokens : list, linetokens : list) -> None:
        
        self.instructions = instructions
        self.filetokens = filetokens
        self.linetokens = linetokens

        self.index = -1

        self.functions_index = self.functions()
        
        if self.linetokens[0] == 'JUMP':
            self.index = self.jump()

        elif self.linetokens[0] == 'JUMPC':
            self.index = self.jumpc()

        elif self.linetokens[0] == 'JSR':
            self.index = self.jsr()

        elif self.linetokens[0] == 'JUMPIND':
            self.index = self.jumpind()

    
    def jump(self) -> int:

        index_temp : int = -1

        operand = self.linetokens[1]
        index_temp = int(self.functions_index[operand])

        self.instructions.pc = self.instructions.pc + 1

        return index_temp

    def jumpc(self) -> int:

        index_temp : int = -1

        operand = self.linetokens[1]

        if self.instructions.pop() != 0:

            index_temp = int(self.functions_index[operand])

            self.instructions.pc = index_temp

        elif self.instructions.peek() == 0:

            self.instructions.pc = self.instructions.pc + 1

        return index_temp
    

    def jsr(self) -> int:

        index_temp : int = -1

        operand = self.linetokens[1]
        index_temp = int(self.functions_index[operand])

        self.instructions.push(None)

        self.instructions.jump_temp = self.instructions.pc + 1

        return index_temp

    def jumpind(self) -> int:

        index_temp : int = -1

        index_temp = self.instructions.jump_temp

        self.instructions.pop()

        self.instructions.pc = self.instructions.pc + 1
        
        return index_temp
    
    

    def functions(self) -> dict:

        functions_index : dict = {}
        
        for i, linetokens in enumerate(self.filetokens):

            for token in linetokens:

                symbol_index = token.find(':')

                if symbol_index == -1:
                    continue

                if symbol_index == (len(token) - 1):

                    token = token[0:len(token) - 1]

                    functions_index[token] = i


        return functions_index

    def jump_index(self) -> int:
        return self.index