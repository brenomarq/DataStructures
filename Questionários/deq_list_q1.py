# Deque e lista - Questão 1
class Deque:
    def __init__(self):
        self.deque = []

    def inserir(self, item):
        self.deque.insert(0, item)

    def inserir_final(self, item):
        self.deque.append(item)

    def remover(self):
        return self.deque.pop(0)

    def remover_final(self):
        return self.deque.pop()

    def print_all(self):
        for elem in self.deque:
            print(elem)

deque = Deque()
while True:
    entrada = input().split()
    command = entrada[0]
    if len(entrada) == 2:
        item = int(entrada[1])

    if command == "I":
        deque.inserir(item)

    elif command == "F":
        deque.inserir_final(item)

    elif command == "P":
        print(deque.remover_final())

    elif command == "D":
        print(deque.remover())

    elif command == "X":
        break

deque.print_all()
