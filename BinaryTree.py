from Node import Node
from ctypes import c_int64

'''
Basic BinaryTree implementation
'''
class BinaryTree():
    def __init__(self):
        # Initializes root node
        self.root = None

    def insert(self, value):
        '''
        Binary tree insert

        Parameters
        ----------
        value : int
            Integer value assigned to a node

        Returns
        -------
        Node
            Node that has been inserted into the binary tree
        '''
        # Return value
        ret_node = None
        # If the tree is empty, then add a root node
        if self.root is None:
            self.root = Node(value, None)
            ret_node = self.root

        elif value > self.root.value:
            if self.root.right is None:
                self.root.right = Node(value, self.root)
                ret_node = self.root.right
            else:
                ret_node = self.insertRecursive(self.root.right, self.root, value)
        else:
            if self.root.left is None:
                self.root.left = Node(value, self.root)
                ret_node = self.root.left
            else:
                ret_node = self.insertRecursive(self.root.left, self.root, value)    

        return ret_node

    def insertRecursive(self, node, parent, value):
        '''
        Recursive insert into a binary tree

        Parameters
        ----------
        node : Node
            Binary tree node
        parent : Node
            Parent of the passed in node, for root this will be None
        value : int
            Integer value assigned to a node
        
        Returns
        -------
        Node
            Node that has been inserted into the binary tree
        '''
        # Return value
        ret_node = None
        if value > node.value:
            if node.right is None:
                node.right = Node(value, node)
                ret_node = node.right
            else:
                ret_node = self.insertRecursive(node.right, node, value)
        else:
            if node.left is None:
                node.left = Node(value, node)
                ret_node
            else:
                ret_node = self.insertRecursive(node.left, node, value)

        return ret_node
        
    def print(self):
        '''
        Prints a binary tree
        
        Returns
        -------
        int
            Number of items in the binary tree
        '''
        # Depth of the tree at root level
        depth = 0
        print("Value: ", self.root.value, ", Depth: ", depth )
        # TODO: This is a hacky way of avoiding pass by value. Ctypes
        # uint64 are mutable, therefore you can pass by reference. This
        # is convenient for finding the number of nodes in a binary tree. 
        node_counter = c_int64(1)

        self.printRecursive(self.root.left, depth, node_counter)
        self.printRecursive(self.root.right, depth, node_counter)

        return node_counter.value

    
    def printRecursive(self, node, depth=None, node_counter=None):
        '''
        Recursive print method

        Parameters
        ----------
        node : Node
            Binary tree node
        depth : int
            depth of the current node
        node_counter : int
            running count of the nodes since intiating recursion
        '''
        if node is None:
            # Break out of recursion
            return
        else:
            if depth:
                # Depth of the tree at the current iteration
                depth += 1
            if node_counter:
                node_counter.value += 1 

            print("Value: ", node.value, ", Depth: ", depth )
            self.printRecursive(node.left, depth, node_counter )
            self.printRecursive(node.right, depth, node_counter )