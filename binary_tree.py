# That's a little implementation of a binary tree structure
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def add_item(self, item, root="no value") -> None:
        if self.root == None:
            self.root = Node(item)
        elif root != "no value":
            if item <= root.data:
                if root.left == None:
                    root.left = Node(item)
                else:
                    self.add_item(item, root.left)
            else:
                if root.right == None:
                    root.right = Node(item)
                else:
                    self.add_item(item, root.right)
        else:
            self.add_item(item, self.root)



binarytree = BinaryTree()
binarytree.add_item(50)
binarytree.add_item(25)
binarytree.add_item(75)
binarytree.add_item(13)
binarytree.add_item(44)
binarytree.add_item(63)
binarytree.add_item(87)
