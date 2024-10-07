from node import Node
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next =  None
'''
#inserir (enqueue)
'''
- Atribui o valor a classe Node
- Verificar se a fila está vazia: O valor adicionado é dito como o "último da fila"
- SENAO o valor é dito como o "próximo"
- SE o primeiro valor for NONE, então o valor que entrou se torna o primeiro da fila
- Aumentar o tamanho da fila (size)

'''
#remover (dequeue)
'''
- Verifica se a lista está vazia e declara a exception
- Guarda o primeiro da lista numa variável
- O próximo da fila se torna o primeiro
- SE o primeiro da fila for None, então o último da fila é None
- Diminuir o tamanho da fila (size)
'''
#is_empty
#len
#repr
'''
- declara "r" como string vazia
- atribui o primeiro elemento ao ponteiro
- faz loop com while
- incrementa o r com str(ponteiro.data)
- atribui o proximo elemento ao ponteiro
- retorna r

'''


class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def enqueue(self, item):
        valor = Node(item) #adiciona o item na classe Node

        if self.is_empty():
            self.last = valor #SE estiver vazia:  O último valor da lista recebe o valor
        else:
            self.last.next = valor #SENAO O próximo recebe o valor

        if self.first is None:
            self.first = valor #SE o primeiro número for none: valor se torna o primeiro da fila

        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("A fila está vazia.")
        
        item = self.first.data

        self.first = self.first.next

        if self.first is None:
            self.last = None

        self._size -= 1

    def is_empty(self):
        return len(self) == 0
    
    def top(self):
        if self.is_empty():
            raise Exception("A lista está vazia.")
        return self.first.data
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        r = ""
        pontiero = self.first
        while(pontiero):
            r = r + str(pontiero.data) + "\n"
            pontiero = pontiero.next
        return r
    
    def __str__(self):
        return self.__repr__()

