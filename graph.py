class Vertex:
    def __init__(self, id):
        self.__id = id
        self.__connects = {}

    def addNeighbor(self, nbr, weight=0):
        self.__connects[nbr] = weight

    def deleteNeighbor(self, nbr):
        if nbr in self.__connects:
            self.__connects.pop(nbr)

    def getConnections(self):
        return self.__connects.keys

    def get_id(self):
        return self.__id

    def get_weight(self, nbr):
        return self.__connects.get(nbr)


class Graph:
    def __init__(self):
        self.__list = {}
