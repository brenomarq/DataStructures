# On this file, I implement some simple algorithms of queue and stack.
class Queue:
    def __init__(self):
        self.__elements = []

    def add(self, item):
        self.__elements.append(item)

    def remove(self):
        return self.__elements.pop(0)

    def size(self):
        return len(self.__elements)

    def is_empty(self):
        return self.__elements == []

    def peek(self):
        if not self.is_empty():
            return self.__elements[-1]


class Stack:
    def __init__(self):
        self.__elements = []

    def add(self, item):
        self.__elements.append(item)

    def remove(self):
        return self.__elements.pop()

    def size(self):
        return len(self.__elements)

    def is_empty(self):
        return self.__elements == []

    def peek(self):
        if not self.is_empty():
            return self.__elements[-1]
