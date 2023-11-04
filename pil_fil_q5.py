# Pilha e fila - Questão 5
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

peso_desejado = int(input())
pesos_retirados = []
while True:
    if pesos.peek() == peso_desejado:
        peso_retirado = pesos.remove()
        pesos_retirados.append(peso_retirado)
        print(f"Peso retirado: {peso_retirado}")
        break
    elif pesos.isEmpty():
        break
    else:
        peso_retirado = pesos.remove()
        pesos_retirados.append(peso_retirado)
        print(f"Peso retirado: {peso_retirado}")

print(f"Anilhas retiradas: {len(pesos_retirados)}")
print(f"Peso total movimentado: {sum(pesos_retirados)}")
