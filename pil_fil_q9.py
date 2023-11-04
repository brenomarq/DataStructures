# Pilha e fila - Questão 9
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def remove(self):
        if self.items:
            chamado = self.items.pop(0)
            self.items.append(chamado)

    def size(self):
        return len(self.items)

    def first(self):
        return self.items[0]

    def last(self):
        return self.items[-1]


fila = Queue()
nomes = input().split()

for nome in nomes:
    fila.push(nome)

for _ in range(int(input())):
    fila.remove()

print(f"Pessoa da frente: {fila.first()}")
print(f"Pessoa do fim: {fila.last()}")


