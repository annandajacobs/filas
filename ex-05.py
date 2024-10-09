'''
5. Descreva como implementar um TAD Pilha usando uma única fila como variável do TAD, e usando quaisquer variáveis dentro dos
métodos. Qual a avaliação do desempenho (utilizando a notação Big O) dos métodos push(), pop() e top()?
'''

class PilhacomFila:
    def __init__(self):
        self.pilha = []

    def is_empty(self):
        return len(self.fila) == 0

    def top(self):
        if self.is_empty():
            raise Exception("A pilha está vazia.")
        return self.pilha[0]
        
    def push(self, elemento):
        tamanho_original = len(self.pilha)
        self.pilha.append(elemento)

        for i in range(tamanho_original):
            self.pilha.append(self.pilha.pop(0)) #move do inicio para o final

    def pop(self):
        if self.is_empty():
            raise Exception("A pilha está vazia.")
        return self.pilha.pop(0)
    



