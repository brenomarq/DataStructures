# Pilha e fila - Questão 1
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
            
            
entrada = input();
fila = Queue();
for elem in entrada:
    if elem == "*":
        print(fila.dequeue(), end="")
    else:
        fila.enqueue(elem)
