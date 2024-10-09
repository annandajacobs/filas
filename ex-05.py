'''
5. Descreva como implementar um TAD Pilha usando uma única fila como variável do TAD, e usando quaisquer variáveis dentro dos
métodos. Qual a avaliação do desempenho (utilizando a notação Big O) dos métodos push(), pop() e top()?
'''

class Fila:
    def __init__(self):
        """Inicializa uma fila vazia."""
        self._dados = []  # Usamos uma lista para armazenar os elementos da fila

    def enqueue(self, item):
        """Insere um item no final da fila."""
        self._dados.append(item)

    def dequeue(self):
        """Remove e retorna o primeiro item da fila."""
        if self.is_empty():
            raise Exception("A fila está vazia.")
        return self._dados.pop(0)  # Remove o primeiro item

    def is_empty(self):
        """Verifica se a fila está vazia."""
        return len(self._dados) == 0

    def size(self):
        """Retorna o número de elementos na fila."""
        return len(self._dados)


class Pilha:
    def __init__(self):
        """Inicializa uma pilha usando uma única fila."""
        self.fila = Fila()  # Cria uma instância de Fila

    def push(self, item):
        """Adiciona um item na pilha."""
        self.fila.enqueue(item)  # Insere o item na fila
        # Move todos os elementos da fila para o final
        for _ in range(self.fila.size() - 1):
            self.fila.enqueue(self.fila.dequeue())

    def pop(self):
        """Remove e retorna o item do topo da pilha."""
        if self.is_empty():
            raise Exception("A pilha está vazia.")
        return self.fila.dequeue()  # Remove o primeiro item, que é o topo da pilha

    def top(self):
        """Retorna o item do topo da pilha sem removê-lo."""
        if self.is_empty():
            raise Exception("A pilha está vazia.")
        return self.fila._dados[0]  # Retorna o primeiro item da fila

    def is_empty(self):
        """Verifica se a pilha está vazia."""
        return self.fila.is_empty()

    def size(self):
        """Retorna o número de elementos na pilha."""
        return self.fila.size()
