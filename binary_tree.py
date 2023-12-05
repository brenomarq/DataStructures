# On this file, I'm implementing a simple binary tree algorithm
from data_managers import Queue


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

    def breadth_first(self):
        if self.__root == None:
            return None

        nodes = Queue()
        nodes.add(self.__root)
        while not nodes.is_empty():
            current_node = nodes.remove()
            print(current_node.data, end=" ")

            if current_node.left != None:
                nodes.add(current_node.left)

            if current_node.right != None:
                nodes.add(current_node.right)
        print()


bt = BinaryTree()
bt.add(50)
bt.add(25)
bt.add(75)
bt.add(13)
bt.add(37)
bt.add(63)
bt.add(87)

bt.pre_order()
bt.in_order()
bt.pos_order()
bt.breadth_first()
