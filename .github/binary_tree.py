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
      while atual.esquerda != None or atual.direita != None:
        if (node < atual.node):
          atual = atual.setEsquerda()
          if atual == None:
            node.esquerda = node
        else:
          atual = atual.setDireita()
          if atual == None:
            node.direita = node

  def emOrdem(self, atual):
    if atual != None:
      self.emOrdem(atual.esquerda)
      print(atual.value)
      self.emOrdem(atual.direita)

  def mostrar(self):
    self.emOrdem(self.root)