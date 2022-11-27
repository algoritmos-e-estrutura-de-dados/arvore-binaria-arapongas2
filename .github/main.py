from binary_tree import BinaryTree

arvore = BinaryTree()

arvore.adicionar(40)
arvore.adicionar(20)
arvore.adicionar(30)
arvore.adicionar(60)
arvore.adicionar(70)
arvore.adicionar(10)
arvore.adicionar(50)
arvore.adicionar(35)
arvore.adicionar(55)
arvore.adicionar(75)
arvore.adicionar(45)
arvore.adicionar(65)

arvore.mostrar()

print("")
arvore.remover(75)
arvore.mostrar()

print("")
arvore.remover(50)
arvore.mostrar()

print("")
arvore.remover(60)
arvore.mostrar()

print("")
arvore.remover(20)
arvore.mostrar()