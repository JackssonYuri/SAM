from stack import Stack


class Instructions(Stack):

    fbr : int
    sp : int
    pc : int

    def __init__(self) -> None:

        super().__init__()
        
        self.fbr = 0
        self.sp = 0
        self.pc = 0

    


        



