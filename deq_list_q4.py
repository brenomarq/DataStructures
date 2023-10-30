# Deque e lista - Questão 4
class Deque:
    def __init__(self):
        self.deque = []

    def insere(self, item):
        self.deque.insert(0, item)

    def insere_final(self, item):
        self.deque.append(item)

    def remove(self):
        if self.deque:
            return self.deque.pop(0)

    def remove_final(self):
        if self.deque:
            return self.deque.pop()


entrada = input()
deque = Deque()
for elem in entrada:
    if elem.isdigit():
        deque.insere_final(elem)
    elif elem == "*":
        print(deque.remove(), end="")
    elif elem == "+":
        print(deque.remove_final(), end="")
    else:
        deque.insere(elem)
