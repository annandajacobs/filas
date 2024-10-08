'''
7. Modifique a implementação FilaArray para que a capacidade da fila seja limitada a um parâmetro informado no construtor. Se enqueue for chamado quando a fila estiver cheia, lance a exceção FilaCheia.
'''
class FilaArray:
  
  CAPACIDADE_PADRAO = 5 

  def __init__(self):
    self._dados = [None] * FilaArray.CAPACIDADE_PADRAO
    self._tamanho = 0
    self._inicio = 0

  def __len__(self):
    return self._tamanho #O(1)

  def is_empty(self):
    return self._tamanho == 0
  
  def is_full(self):
    return self._tamanho == FilaArray.CAPACIDADE_PADRAO

  def first(self):
    if self.is_empty():
      raise Exception('A Fila está vazia')
    return self._dados[self._inicio]

  def dequeue(self):
    if self.is_empty():
      raise Exception('A Fila está vazia')
    result = self._dados[self._inicio]
    self._dados[self._inicio] = None
    self._inicio = (self._inicio + 1) % len(self._dados)
    self._tamanho -= 1
    return result

  def enqueue(self, eLemento): # - - x x x - 
    if self.is_full():
      raise Exception("A fila está cheia.")
    
    disponivel = (self._inicio + self._tamanho) % len(self._dados)
    self._dados[disponivel] = eLemento
    self._tamanho += 1

  def _altera_tamanho(self, novo_tamanho):   # novo_tamanho precisar ser >= len(self)
    dados_antigos = self._dados               # keep track of existing list
    self._dados = [None] * novo_tamanho       # allocate list with new capacity
    posicao = self._inicio
    for k in range(self._tamanho):            # only consider existing elements
      self._dados[k] = dados_antigos[posicao] # intentionally shift indices
      posicao = (1 + posicao) % len(dados_antigos) # use dados_antigos size as modulus
    self._inicio = 0                          # front has been realigned

  def show(self):
    print(self)

  def __str__(self):
    posicao = self._inicio
    result = "["
    
    for k in range(self._tamanho):
      result += str(self._dados[posicao]) + ", "
      posicao = (1 + posicao) % len(self._dados)
    result += f'] tamanho: {len(self)} capacidade {len(self._dados)}\n'
    return result


    