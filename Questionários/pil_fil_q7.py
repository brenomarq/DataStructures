# Pilha e fila - Questão 7
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def remove(self):
        if self.items:
            return self.items.pop()

    def size(self):
        return len(self.items)

stack = Stack()
for _ in range(int(input())):
    entrada = input().split()
    stack.push(entrada)

quantidade_roupas = stack.size()
tempos = []
roupas = []
cores = []

while not stack.isEmpty():
    roupa, cor, tempo = stack.remove()
    roupas.append(roupa)
    cores.append(cor)
    tempos.append(int(tempo))

for i in range(quantidade_roupas):
    print(f"Tipo: {roupas[i]}, Cor: {cores[i]}")

print(f"Total de roupas: {quantidade_roupas}")
print(f"Total de tempo: {sum(tempos)}")

