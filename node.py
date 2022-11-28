class Node:

  def __init__(self, value, direita = None, esquerda = None):
    self.value = value
    self.direita = direita
    self.esquerda = esquerda

  def setDireita(self, direita):
    self.direita = direita

  def setEquerda(self, esquerda):
    self.esquerda = esquerda