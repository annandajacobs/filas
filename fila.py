from node import Node
#construtor => __init__
#inserir
#remover
#len
#size
#__repr__
#__str__

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def enqueue(self, item):
        value = Node(item)

        if self.is_empty():
            self.last = value
        else:
            self.last.next = value
            self.last = value

        if self.first is None:
            self.first = value
        
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("A fila está vazia.")
        
        primeiro = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None

        self._size -= 1

    def top(self):
        if self.is_empty():
            raise Exception("A fila está vazia")
        return self.first.data

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0 
    
    def __repr__(self):
        r = ""
        ponteiro = self.first
        while(ponteiro):
            r = r + str(ponteiro.data) + "\n"
            ponteiro = ponteiro.next
        return r
    
    def __str__(self):
        return self.__repr__()

# f = Queue()
# f.enqueue(1) 
# f.enqueue(2) 
# f.enqueue(3) 
# f.enqueue(4) 
# f.enqueue(5) 
# f.dequeue()
# f.dequeue()

# print(repr(f))
# print(f.top())