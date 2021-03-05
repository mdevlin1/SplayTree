from Node import Node

class Splay:
    def __init__(self):
        self.root = None

    def insert(self, value):
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


    def zig(self, parent, node):
        if node.right is None and node.left is None:
            node.parent.left = None
            temp_parent = node.parent.parent
            node.parent.parent = node

            node.right = node.parent
            node.parent = temp_parent
            self.splayUp(node)

        elif node.right is None or node.left is None:
            if node.right is None:
                node.parent.left = None
                temp_parent = node.parent.parent
                node.parent.parent = node

                node.right = node.parent
                node.parent = temp_parent
                self.splayUp(node)

            else:
                node.parent.left = None
                temp_parent = node.parent.parent
                node.parent.parent = node

                temp_child = node.right
                node.right = node.parent
                node.right.left = temp_child
                node.parent = temp_parent
                self.splayUp(node)

        else:
            node.parent.left = None
            temp_parent = node.parent.parent
            node.parent.parent = node

            temp_child = node.right
            node.right = node.parent
            node.right.left = temp_child
            node.parent = temp_parent
            self.splayUp(node)


    def zag(self, parent, node):
        if node.right is None and node.left is None:
            temp_parent = node.parent.parent
            node.parent.parent = node

            node.left = node.parent
            node.left.right = None
            node.parent = temp_parent
            self.splayUp(node)

        elif node.right is None or node.left is None:
            if node.right is None:
                node.parent.right = None
                temp_parent = node.parent.parent
                node.parent.parent = node

                temp_child = node.left
                node.left = node.parent
                node.left.right = temp_child
                node.parent = temp_parent
                self.splayUp(node)

            else:
                node.parent.right = None
                temp_parent = node.parent.parent
                node.parent.parent = node

                node.left = node.parent
                node.parent = temp_parent
                self.splayUp(node)

        else:
            node.parent.right = None
            temp_parent = node.parent.parent
            node.parent.parent = node

            temp_child = node.left
            node.left = node.parent
            node.left.right = temp_child
            node.parent = temp_parent
            self.splayUp(node)


    def splayUp(self, node):
        if node.parent == self.root:
            self.root = node

        if node == self.root:
            return

        if node.value > node.parent.value:
            zag(parent, node)
        else:
            zig(parent, node)