'''
7. Modifique a implementação FilaArray para que a capacidade da fila seja limitada a um parâmetro informado no construtor. Se enqueue for chamado quando a fila estiver cheia, lance a exceção FilaCheia.
'''
from node import Node

class Fila:
    def __init__(self, capacidade):
        """Inicializa uma fila vazia com uma capacidade limitada."""
        self.first = None  # Aponta para o primeiro nó (cabeça)
        self.last = None   # Aponta para o último nó (cauda)
        self._size = 0     # Contador para o número de elementos na fila
        self._capacidade = capacidade  # Capacidade máxima da fila

    def enqueue(self, item):
        """Insere um item no final da fila."""
        if self._size >= self._capacidade:
            raise Exception("A fila está cheia.")
        
        new_node = Node(item)  # Cria um novo nó com o valor fornecido

        if self.is_empty():
            self.first = new_node  # Se a fila estiver vazia, o novo nó é o primeiro
        else:
            self.last.next = new_node  # Conecta o último nó ao novo nó

        self.last = new_node  # Atualiza o ponteiro 'last' para o novo nó
        self._size += 1

    def dequeue(self):
        """Remove e retorna o primeiro item da fila."""
        if self.is_empty():
            raise Exception("A fila está vazia.")
        
        item = self.first.data  # Pega o dado do primeiro nó
        self.first = self.first.next  # Move o ponteiro para o próximo nó

        if self.first is None:
            self.last = None  # Se a fila ficou vazia, last também se torna None
        
        self._size -= 1
        return item

    def first_element(self):
        """Retorna o primeiro item da fila sem removê-lo."""
        if self.is_empty():
            raise Exception("A fila está vazia.")
        return self.first.data

    def is_empty(self):
        """Verifica se a fila está vazia."""
        return self.first is None

    def __len__(self):
        """Retorna o número de elementos na fila."""
        return self._size

    