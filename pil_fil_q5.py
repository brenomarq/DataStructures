# Pilha e fila - Questão 5 (Incompleta)
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def remove(self):
        if self.items:
            return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[len(self.items) - 1]


peso = int(input())
pesos = Stack()
while peso != 0:
    pesos.push(peso)
    peso = int(input())
