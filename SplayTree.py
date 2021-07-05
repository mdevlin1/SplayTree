from Node import Node
from BinaryTree import BinaryTree

class Splay(BinaryTree):

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