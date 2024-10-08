'''
8. Em certas aplicações do TAD fila, é comum repetidamente realizar dequeue e então, imediamente, realizar enqueue com o mesmo
elemento. Modifique a implementação FilaArray para incluir um método rodar() que deve ser semanticamente identifico a f.enqueue(f.dequeue) .
'''


#construtor => __init__
#inserir
#remover
#len
#size
#__repr__
#__str__

class FilaArray():
    CAPACIDADE_PADRAO = 5
    def __init__(self):
        self._dados = [None] * FilaArray.CAPACIDADE_PADRAO #criar a fila e mult. por capacidade
        self._size = 0 #definir o tamanho
        self._first = 0 #definir o primeiro da fila
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("A fila está vazia.")

        elemento = self._dados[self._first]
        self._dados[self._first] = None
        self._first = (self._first + 1 ) % len(self._dados)
        self._size -= 1
        return elemento
    
    def enqueue(self, elemento):
        if self._size == len(self._dados):
            self.alterar_tamanho(2 * len(self._dados))
        
        disponivel = (self._first + self._size) % len(self._dados)
        self._dados[disponivel] = elemento
        self._size += 1

    def front(self):
        if self.is_empty():
            raise Exception("A fila está vazia.")
        return self._dados[self._first]
    
    def alterar_tamanho(self, new_size):
        if self._size >= new_size:
            raise Exception("O tamanho é menor que o anterior.")
        
        dados_antigos = self._dados
        self._dados = [None] * new_size
        posicao = self._first

        for i in range(self._size): #adiciona os dados antigos na nova fila
            self._dados[i] = dados_antigos[posicao] # novos dados no msm local do anterior
            posicao = (1 + posicao) % len(dados_antigos) #nostra a próxima posição
        self._first = 0

    def rodar(self):
        if self.is_empty():
            raise Exception("A fila está vazia.")
        item = self.dequeue() # pega o elemento excluído
        self.enqueue(item)    # adiciona novamente

    def show(self):
        print(self)
