class Stack:

    items : list

    def __init__(self) -> None:
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []
    
    def push(self, item : object) -> None:
        self.items.append(item)

    def pop(self) -> object:
        if not self.isEmpty(): 
            return self.items.pop()
        else:
            raise IndexError('Não há elementos na lista')

    def peek(self) -> object:
        if not self.isEmpty(): 
            return self.items[len(self.items) - 1]
        else:
            raise IndexError('Não há elementos na lista')

    def size(self) -> int:
        return len(self.items)
    
    def copy(self) -> list:

        self.items_aux = self.items.copy()
        
        return self.items_aux