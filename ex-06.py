'''
6. Descrever como implementar o TAD Fila usando duas pilhas como variáveis do TAD, tal que todas as operações da fila sejam
executadas em O(1).
'''

from collections import deque

class FilaComDuasPilhas:
    def __init__(self):
        self.pilha_entrada = [] # é usada para inserir os elementos.
        self.pilha_saida = []   # é usada para remover os elementos.
    
    def enqueue(self, item):
        # Insere item no final da fila
        self.pilha_entrada.append(item)

    def dequeue(self):
    # Remove e retorna o primeiro elemento
        if self.is_empty():
            raise Exception("A pilha está vazia.")
        # se a pilha de saída estiver vazia, traferimos os elementos da pilha de entrada
        if not self.pilha_saida:
            while self.pilha_entrada:
                self.pilha_saida.append(self.pilha_entrada.pop())
        
        return self.pilha_saida.pop()
    
    def first(self):
        #Retorna o primeiro elemento da fila sem removê-lo.
        if self.is_empty():
            raise Exception("A pilha está vazia.")
        
        # Se a pilha de saída estiver vazia, transferimos os elementos da pilha de entrada
        if not self.pilha_saida:
            while self.pilha_entrada:
                self.pilha_saida.append(self.pilha_entrada.pop())
    
        return self.pilha_saida[-1] # O topo da pilha de saída contém o primeiro elemento da fila
    
    def is_empty(self):
        return not self.pilha_entrada and not self.pilha_saida
    
    def __len__(self):
        return len(self.pilha_entrada) + len(self.pilha_saida)
