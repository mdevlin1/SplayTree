from Node import Node
from BinaryTree import BinaryTree

class Splay(BinaryTree):

    def insert(self, value):
        '''
        Overloaded binary tree insert method. This will call the
        binary tree insert, then splay the node up

        Parameters
        ----------
        value : int
            Integer value assigned to a node
        '''
        node = super().insert(value)
        self.splay(node)

    def left_rotate(self, node):
        '''
        Splay tree left rotate method

        Parameters
        ----------
        node : Node
            Splay tree node
        '''
        node_right = node.right
        if node_right:
            node.right = node.left
            if node.left:
                node_right.left.parent = node
            node_right.parent = node.parent

        if not node.parent:
            self.root = node_right
        elif node == node.parent.left:
            node.parent.left = node_right
        else:
            node.parent.right = node_right
        
        if node_right:
            node.left = node
        node.parent = node_right
  
    def right_rotate(self, node):
        '''
        Splay tree right rotate method

        Parameters
        ----------
        node : Node
            Splay tree node
        '''
        node_left = node.left
        if node_left:
            node.left = node_left.right
            if node_left.right:
                node_left.right.parent = node
            node_left.parent = node.parent
        
        if not node.parent:
            self.root = node_left
        elif node == node.parent.left:
            node.parent.left = node_left
        else:
            node.parent.right = node_left
        
        if node_left:
            node_left.right = node
        
        node.parent = node_left

    def splay(self, node):
        '''
        Performs splaying on an inserted value in the tree

        Parameters
        ----------
        node : Node
            Splay tree node
        '''
        while node.parent:
            if not node.parent.parent:
                if node.parent.left == node:
                    self.right_rotate(node.parent)
                else:
                    self.left_rotate(node.parent)
            elif node.parent.left == node and node.parent.parent.left == node.parent:
                self.right_rotate(node.parent.parent)
                self.right_rotate(node.parent)
            elif node.parent.right == node and node.parent.parent.right == node.parent:
                self.left_rotate(node.parent.parent)
                self.left_rotate(node.parent)
            elif node.parent.left == node and node.parent.parent.right == node.parent:
                self.right_rotate(node.parent)
                self.left_rotate(node.parent)
            else:
                self.left_rotate(node.parent)
                self.right_rotate(node.parent)
            