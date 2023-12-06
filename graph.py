# On this file, I'll implement a simple graph algorithm.
class Vertex:
    def __init__(self, id) -> None:
        self.__id = id
        self.__connections = {}
        self.__status = "not visited"

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, key):
        self.__id = key

    def add_neighbor(self, nbr, weight=0):
        self.__connections[nbr] = weight

    def delete_neighbor(self, nbr):
        if nbr in self.__connections:
            self.__connections.pop(nbr)

    def get_status(self):
        return self.__status

    def get_connections(self):
        return self.__connections

    def get_weight(self, nbr):
        if nbr in self.__connections:
            return self.__connections[nbr]
        return "Connection not found"

    def __str__(self):
        return f"{self.__id} is connected to {[x.id for x in self.__connections]}"


class Graph:
    def __init__(self) -> None:
        self.__elements = {}

    def add_vertex(self, key):
        self.__elements[key] = Vertex(key)

    def delete_vertex(self, key):  # Need better implementation
        for element in self.__elements.values():
            element.delete_neighbor(key)

        if key in self.__elements:
            self.__elements.pop(key)

    def get_vertex(self, key):
        if key in self.__elements:
            return self.__elements[key]

    def add_edge(self, src, dst, cost=0):
        if src not in self.__elements:
            self.add_vertex(src)
        if dst not in self.__elements:
            self.add_vertex(dst)

        self.get_vertex(src).add_neighbor(self.get_vertex(dst), cost)


graph = Graph()
graph.add_vertex("v1")
graph.add_vertex("v2")
graph.add_vertex("v3")

graph.add_edge("v1", "v3", 5)
graph.add_edge("v3", "v4", 8)
graph.delete_vertex("v4")
print("Done")
