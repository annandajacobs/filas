'''
4. Considere o o método "_altera_tamanho" de FilaArray. Se as linhas "a" e "b" fossem alteradas, explique o que aconteceria:

Estaria ignorando o fato de que os elementos podem estar deslocados dentro do array original, devido ao comportamento circular. Isso resultaria em uma ordem incorreta dos elementos no novo array. 
Em vez de começar a cópia a partir de self._inicio e avançar circularmente, a cópia começaria sempre do início (dados_antigos[0]), o que quebraria a sequência correta de elementos na fila.
'''

class FilaVazia(Exception):
  pass

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

  def first(self):
    if self.is_empty():
      raise FilaVazia('A Fila está vazia')
    return self._dados[self._inicio]

  def dequeue(self):
    if self.is_empty():
      raise FilaVazia('A Fila está vazia')
    result = self._dados[self._inicio]
    self._dados[self._inicio] = None
    self._inicio = (self._inicio + 1) % len(self._dados)
    self._tamanho -= 1
    return result

  def enqueue(self, e): # - - x x x - 
    if self._tamanho == len(self._dados):
      self._altera_tamanho(2 * len(self._dados))
    disponivel = (self._inicio + self._tamanho) % len(self._dados)
    self._dados[disponivel] = e
    self._tamanho += 1

  def _altera_tamanho(self, novo_tamanho):   # novo_tamanho precisar ser >= len(self)
    dados_antigos = self._dados               # keep track of existing list
    self._dados = [None] * novo_tamanho       # allocate list with new capacity
    posicao = self._inicio
    for k in range(self._tamanho):            # only consider existing elements
      self._dados[k] = dados_antigos[posicao] # intentionally shift indices
      posicao = (posicao + 1) % len(dados_antigos) # use dados_antigos size as modulus
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


f = FilaArray()
f._altera_tamanho(7)
for i in range(7):
  f.enqueue(i)
f.show()