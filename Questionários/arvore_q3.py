class ArvoreBinaria:
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir


def pre_order_esq(r, holder):
    if r == None:
        return

    holder.append(r.dado)
    pre_order_esq(r.esq, holder)
    pre_order_esq(r.dir, holder)


def pre_order_dir(r, holder):
    if r == None:
        return

    holder.append(r.dado)
    pre_order_dir(r.dir, holder)
    pre_order_dir(r.esq, holder)


def verificaSimetria(raiz):
    esq = []
    dir = []

    pre_order_esq(raiz.esq, esq)
    pre_order_dir(raiz.dir, dir)

    return esq == dir






