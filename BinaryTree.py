from Node import Node

'''
Basic BinaryTree implementation
'''
class BinaryTree():
    def __init__(self):
        # Initializes root node
        self.root = None

    def insert(self, value):
        # If the tree is empty, then add a root node
        if self.root is None:
            self.root = Node(value, None)

        elif value > self.root.value:
            if self.root.right is None:
                self.root.right = Node(value, self.root)
                self.splayUp(self.root.right)
            else:
                self.insertRecursive(self.root.right, self.root, value)

        else:
            if self.root.left is None:
                self.root.left = Node(value, self.root)
                self.splayUp(self.root.left)
            else:
                self.insertRecursive(self.root.left, self.root, value)    

    def insertRecursive(self, node, parent, value):
        if value > node.value:
            if node.right is None:
                node.right = Node(value, node)
                self.splayUp(node.right)
            else:
                self.insertRecursive(node.right, node, value)

        else:
            if node.left is None:
                node.left = Node(value, node)
                self.splayUp(node.left)
            else:
                self.insertRecursive(node.left, node, value)
