from copy import deepcopy

class Pilha:
    def __init__(self):
      self.items = []

    def empilhar(self, valor):
      self.items.append(valor)

    def desempilhar(self):
      return self.items.pop()

    def tamanho(self):
      return len(self.items)

    def vazia(self):
      return self.items == []

    def topo(self):
      return self.items[-1]

    def __str__(self):
      pilha = ''
      for item in self.items:
          pilha += str(item)  + ','    
      return pilha
      
class Fila:
  def __init__(self):
      self.items = []
  def enfileirar(self, item):
      self.items.insert(0, item)
  def desenfileirar(self):
      return self.items.pop()
  def tamanho(self):
      return len(self.items)
  def vazia(self):
      return self.items == []
  def frente(self):
      return self.items[-1]
    
  def inverte(self):
      pilha = Pilha()
      while not self.vazia():
          pilha.empilhar(self.desenfileirar())
      
      while not pilha.vazia():
          self.enfileirar(pilha.desempilhar())

  def ordenado(self):
      # para testar depois
      temp = deepcopy(self)
      while not temp.vazia():
          tirado = temp.desenfileirar()
          if tirado > temp.frente():
              return False
      return True
    
  def reduz_para_n(self, n):
      if self.tamanho() >= n:
          while (self.tamanho() != n):
              self.desenfileirar()

  def __str__(self):
      return ','.join([str(i) for i in self.items])

    
