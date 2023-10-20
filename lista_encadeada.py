# Lista encadeada
class Lista():
    def __init__(self, elem, prox=None):
        self.elem = elem
        self.prox = prox


def adiciona(lista, elem):
    if lista.prox == None:
        lista.prox = Lista(elem)
    else:
        adiciona(lista.prox, elem)


def retira(lista, elem):
    if lista.prox == elem:
        aux = lista.prox.prox
        lista.prox = aux
    retira(lista.prox, elem)


lista = Lista(1)
adiciona(lista, 2)
adiciona(lista, 3)
