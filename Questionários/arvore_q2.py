class ArvoreBinaria:
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir


def constituiArvoreBinariaDeBusca(raiz):
    constitui = True

    if raiz.esq != None:
        if raiz.esq.dado > raiz.dado:
            constitui = False
            return constitui
        else:
            constitui = constituiArvoreBinariaDeBusca(raiz.esq)

    if raiz.dir != None:
        if raiz.dir.dado < raiz.dado:
            constitui = False
            return constitui
        else:
            constitui = constituiArvoreBinariaDeBusca(raiz.dir)

    return constitui



raiz = ArvoreBinaria(7, ArvoreBinaria(4), ArvoreBinaria(10, ArvoreBinaria(11), ArvoreBinaria(15)))
print(constituiArvoreBinariaDeBusca(raiz))

