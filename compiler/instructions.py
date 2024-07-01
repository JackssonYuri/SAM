from .stack import Stack


class Instructions(Stack):

    fbr : int
    sp : int
    pc : int
    items_temp : list
    jump_temp : int

    def __init__(self) -> None:

        super().__init__()
        
        self.fbr = 0
        self.sp = 0
        self.pc = 0
        self.items_temp = []
        self.jump_temp = -1
        

    def push_tmp(self, item : object) -> None:
        self.items_temp.append(item)

    def pop_tmp(self) -> object:
        if not self.isEmpty_tmp(): 
            return self.items_temp.pop()
        else:
            raise IndexError('Não há elementos na lista')
        

    def size_tmp(self) -> int:
        return len(self.items_temp)
        
    def reverse_tmp(self):
        return self.items_temp.reverse()
    
    def isEmpty_tmp(self) -> bool:
        return self.items_temp == []
    
    


        



