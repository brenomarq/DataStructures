# Neste arquivo, é implementada um algoritmo simples de árvore binária junto com alguns tipos de percurso (pre-order, in-order e pos-order)
class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def add_item(item: int, root: BTNode):
    if item <= root.data:
        if root.left == None:
            root.left = BTNode(item)
        else:
            add_item(item, root.left)
    else:
        if root.right == None:
            root.right = BTNode(item)
        else:
            add_item(item, root.right)


def pre_order(root: BTNode | None):
    if root == None:
        return None

    print(root.data)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root: BTNode | None):
    if root == None:
        return None

    in_order(root.left)
    print(root.data)
    in_order(root.right)


def pos_order(root: BTNode | None):
    if root == None:
        return None

    pos_order(root.left)
    pos_order(root.right)
    print(root.data)


binary_tree = BTNode(50)
add_item(25, binary_tree)
add_item(75, binary_tree)
add_item(13, binary_tree)
add_item(44, binary_tree)
add_item(63, binary_tree)
add_item(87, binary_tree)
pre_order(binary_tree)
print()
in_order(binary_tree)
print()
pos_order(binary_tree)
