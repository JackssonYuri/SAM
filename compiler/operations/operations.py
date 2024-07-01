from .jump_operations import Jump
from .pointer_operations import Pointer
from .manipulation_operations import Manipulation
from .compare_operations import Compare
from .logical_operatitions import Logical
from .memory_operations import Memory
from .arithmetic_operations import Arithmetic
from compiler.instructions import Instructions


class Operations:

    instructions : Instructions

    arithmetic : Arithmetic
    logical : Logical
    compare : Compare
    memory : Memory
    manipulation : Manipulation
    pointer : Pointer
    jump : Jump

    filetokens : list
    linetokens : list
    jump_tokens : list = ['JUMP', 'JUMPC', 'JSR', 'JUMPIND']


    def __init__(self, instructions : Instructions, filetokens : list) -> None:
        
        self.instructions = instructions
        self.filetokens = filetokens

    def execute(self) -> Instructions:

        i : int = 0

        while i < len(self.filetokens):

            self.linetokens = self.filetokens[i]

            if self.linetokens[0] == 'STOP':
               break

            if self.linetokens[0] in self.jump_tokens:

                self.jump = Jump(self.instructions, self.filetokens, self.linetokens)

                if self.jump.jump_index() != -1:
                    i = self.jump.jump_index()


            

            self.arithmetic = Arithmetic(self.instructions, self.linetokens)
            self.logical = Logical(self.instructions, self.linetokens)
            self.compare = Compare(self.instructions, self.linetokens)
            self.memory = Memory(self.instructions, self.linetokens)
            self.manipulation = Manipulation(self.instructions, self.linetokens)
            self.pointer = Pointer(self.instructions, self.linetokens)


            
            self.instructions.sp = len(self.instructions.items)
            i = i + 1


        
        return self.instructions
    











    
       


                    

            

            

                    
    




                



                


                    

        






    



