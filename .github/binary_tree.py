from node import Node

class BinaryTree:

  def __init__(self):
    self.root = None

  def adicionar(self,value):
    node = Node(value)
    if (self.root == None):
      self.root = node
    else:
      atual = self.root
      while True:
        ant = atual
        if (value < atual.value):
          atual = atual.esquerda
          if atual == None:
            ant.esquerda = node
            break
        else:
          atual = atual.direita
          if atual == None:
            ant.direita = node
            break

  def emOrdem(self, atual):
    if atual != None:
      self.emOrdem(atual.esquerda)
      print(atual.value, end = ' ')
      self.emOrdem(atual.direita)

  def preOrdem(self, atual):
    if atual != None:
      print(atual.value, end = ' ')
      self.preOrdem(atual.esquerda)
      self.preOrdem(atual.direita)

  def posOrdem(self, atual):
    if atual != None:
      self.posOrdem(atual.esquerda)
      self.posOrdem(atual.direita)
      print(atual.value, end = ' ')
     
  def mostrar(self):
    print("")
    print("Em ordem: ")
    self.emOrdem(self.root)
    print("")
    print("Pré ordem: ")
    self.preOrdem(self.root)
    print("")
    print("Pós ordem: ")
    self.posOrdem(self.root)
 
  def realocar(self, remove):
    pai_s = remove
    sucessor = remove
    atual = remove.direita
   
    while atual != None:
      pai_s = sucessor
      sucessor = atual
      atual = atual.esquerda

    if sucessor != remove.direita:
      pai_s.esquerda = sucessor.direita
      sucessor.direita = remove.direita
     
    return sucessor

  def remover(self, value):
    if self.root == None:
       print ("Árvore vazia.")

    atual = self.root
    pai = self.root
    f_esq = True

    while atual.value != value:
      pai = atual
      if value < atual.value:
        atual = atual.esquerda
        f_esq = True
      else:
        atual = atual.direita
        f_esq = False
      if atual == None:
        return False
       
    if atual.esquerda == None and atual.direita == None:
      if atual == self.root:
        self.root = None
      else:
        if f_esq:
          pai.esquerda = None
        else:
          pai.direita = None
         
    elif atual.esquerda == None:
      if atual == self.root:
        self.root = atual.direita
      else:
        if f_esq:
          pai.esquerda = atual.direita
        else:
          pai.direita = atual.direita

    elif atual.direita == None:
      if atual == self.root:
        self.root = atual.esquerda
      else:
        if f_esq:
          pai.esquerda = atual.esquerda
        else:
          pai.direita = atual.esquerda

    else:
      sucessor = self.realocar(atual)
      if atual == self.root:
        self.root = sucessor
      else:
        if f_esq:
          pai.esquerda = sucessor
        else:
          pai.direita = sucessor
      sucessor.esquerda = atual.esquerda
     
    return True