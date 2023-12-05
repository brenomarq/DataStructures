class Node:
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value


class BinaryTree:
    def __init__(self):
        self.__root = None

    def add(self, item, root=None):
        if self.__root == None:
            self.__root = Node(item)
        elif root == None:
            self.add(item, self.__root)
        else:
            if item <= root.data:
                if root.left == None:
                    root.left = Node(item)
                else:
                    self.add(item, root.left)
            else:
                if root.right == None:
                    root.right = Node(item)
                else:
                    self.add(item, root.right)

    def pre_order(self, root="No value"):
        if root == "No value":
            self.pre_order(self.__root)
            print()
        elif root == None:
            return None
        else:
            print(root.data, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self, root="No value"):
        if root == "No value":
            self.in_order(self.__root)
            print()
        elif root == None:
            return None
        else:
            self.in_order(root.left)
            print(root.data, end=" ")
            self.in_order(root.right)

    def pos_order(self, root="No value"):
        if root == "No value":
            self.pos_order(self.__root)
            print()
        elif root == None:
            return None
        else:
            self.pos_order(root.left)
            self.pos_order(root.right)
            print(root.data, end=" ")


bt = BinaryTree()
entrada = input()
while entrada != "quack":
    if entrada.isdigit():
        bt.add(int(entrada))

    elif entrada == "pre":
        bt.pre_order()

    elif entrada == "in":
        bt.in_order()

    else:
        bt.pos_order()

    entrada = input()
