#!/usr/bin/python

RED = 'r'
BLACK = 'b'

class RBTreeNode(object):
    
    def __init__(self, key=None, color=BLACK, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

