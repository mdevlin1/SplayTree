from enum import Enum

# Enum that indicates if a node is to the
# left or the right of it's parent
class Position(Enum):
    LEFT = 1,
    RIGHT = 2

class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None 

    def findPosition(self):
        if self.value > self.parent.value:
            return Position.RIGHT
        elif self.value < self.parent.value:
            return Position.LEFT
        else:
            raise Exception('Undefined behavior, values do not fit binary tree definition')