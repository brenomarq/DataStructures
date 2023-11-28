class Vertex:
    def __init__(self, key):
        self.__key = key
        self.__connect_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.__connect_to[nbr] = weight

    def del_neighbor(self, nbr):
        ...


class Graph:
    def __init__(self):
        self.__vert_list = {}
