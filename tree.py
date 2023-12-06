# On this file, I'll implement a simple tree algorithm with some methods and attributes
from data_managers import Queue


class Tree:
    def __init__(self, data: str | int):
        self.__data = data
        self.__branches = []

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value: str | int):
        self.__data = value

    @property
    def branches(self):
        return self.__branches

    def add_branch(self, key: str | int):
        self.__branches.append(Tree(key))

    def remove_branch(self, key: str | int):
        for i, branch in enumerate(self.__branches):
            if key == branch.data:
                return self.__branches.pop(i).data

    def how_many_branches(self):
        return len(self.__branches)

    def breadth_first_seach(self):
        root = self
        all_nodes = []

        nodes = Queue()
        nodes.add(root)
        while not nodes.is_empty():
            current_node = nodes.remove()
            all_nodes.append(current_node.data)


            for branch in current_node.branches:
                nodes.add(branch)

        return all_nodes


v1 = Tree(1)
v1.add_branch(2)
v1.add_branch(3)

v2 = v1.branches[0]
v2.add_branch(4)
v2.add_branch(5)
v2.add_branch(6)

v5 = v2.branches[1]
v5.add_branch(10)

v3 = v1.branches[-1]
v3.add_branch(7)

print(v1.breadth_first_seach())