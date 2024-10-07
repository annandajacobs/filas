'''
Estaria ignorando o fato de que os elementos podem estar deslocados dentro do array original, devido ao comportamento circular. Isso resultaria em uma ordem incorreta dos elementos no novo array. 
Em vez de começar a cópia a partir de self._inicio e avançar circularmente, a cópia começaria sempre do início (dados_antigos[0]), o que quebraria a sequência correta de elementos na fila.
'''

class Node:
    def __init__(self, data):
        """Inicializa um nó com o valor e o ponteiro para o próximo nó."""
        self.data = data
        self.next = None

class Fila:
    def __init__(self):
        """Inicializa uma fila vazia."""
        self.first = None
        self.last = None
        self._size = 0

    def enqueue(self, item):
        """Insere um item no final da fila."""
        novo_nodo = Node(item)

        if self.is_empty():
            self.first = novo_nodo
        else:
            self.last.next = novo_nodo

        self.last = novo_nodo
        self._size += 1

    def dequeue(self):
        """Remove e retorna o primeiro item da fila."""
        if self.is_empty():
            raise Exception("A fila está vazia.")

        item = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None

        self._size -= 1
        return item

    def is_empty(self):
        """Verifica se a fila está vazia."""
        return self._size == 0

    def inicio(self):
        """Retorna o primeiro item da fila sem removê-lo."""
        if self.is_empty():
            raise Exception("A fila está vazia.")
        return self.first.data

    def alterar_tamanho(self, new_size):
        """Altera o tamanho da fila para o novo tamanho e copia os elementos."""
        if new_size < self._size:
            raise Exception("Novo tamanho não pode ser menor que o tamanho atual da fila.")

        dados_antigos = [None] * self._size  # Criar um array para armazenar os dados
        posicao = self.first
        
        # Copia os elementos da fila para o array auxiliar
        for i in range(self._size):
            dados_antigos[i] = posicao.data  # Adiciona o dado do nó
            posicao = posicao.next  # Avança para o próximo nó
        
        # Cria uma nova lista com o novo tamanho
        self.data = [None] * new_size
        
        # Copia os dados do array auxiliar para a nova lista
        for k in range(self._size):
            self.data[k] = dados_antigos[k]
        
        # Reseta a fila, pode-se redefinir first e last se necessário
        self.first = None
        self.last = None
        self._size = 0  # Zera o tamanho atual da fila

        # Repreenche a fila com os dados copiados
        for item in dados_antigos:
            self.enqueue(item)

