'''
Splay tree algorithm inspired by https://en.wikipedia.org/wiki/Splay_tree
'''
from Node import Node
from BinaryTree import BinaryTree

class Splay(BinaryTree):
    def __init__( self ):
        ''' Splay tree constructor'''
        BinaryTree.__init__( self )

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
        child_node = node.right
        if child_node:
            node.right = child_node.left
            if child_node.left:
                child_node.left.parent = node
            child_node.parent = node.parent

        if not node.parent:
            self.root = child_node
        elif node == node.parent.left:
            node.parent.left = child_node
        else:
            node.parent.right = child_node
        
        if child_node:
            child_node.left = node
        node.parent = child_node


    def right_rotate(self, node):
        '''
        Splay tree right rotate method

        Parameters
        ----------
        node : Node
            Splay tree node
        '''
        child_node = node.left
        if child_node:
            node.left = child_node.right
            if child_node.right:
                child_node.right.parent = node
            child_node.parent = node.parent
        
        if not node.parent:
            self.root = child_node
        elif node == node.parent.left:
            node.parent.left = child_node
        else:
            node.parent.right = child_node
        
        if child_node:
            child_node.right = node
        
        node.parent = child_node

    def splay(self, node):
        '''
        Performs splaying on an inserted value in the tree

        Parameters
        ----------
        node : Node
            Splay tree node
        '''
        while node and node.parent:
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
            