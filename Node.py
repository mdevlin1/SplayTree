from enum import Enum

# Enum that indicates if a node is to the
# left or the right of it's parent
class Position(Enum):
    LEFT = 1,
    RIGHT = 2

'''
Binary tree node class
'''
class Node:
    def __init__(self, value, parent):
        '''
        Node constructor

        Parameters
        ----------
        value : int
            integer value assigned to a node
        parent : Node
            Parent of a node, for root this will be None
        '''
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None 

    def findPosition(self):
        '''
        Location a binary node is to be placed, based on the parent nodes value

        Returns
        -------
        Position
            position enum value indicating left or right insertion
        '''
        if self.value > self.parent.value:
            return Position.RIGHT
        elif self.value < self.parent.value:
            return Position.LEFT
        else:
            raise Exception('Undefined behavior, values do not fit binary tree definition')