#!/usr/bin/python

RED = 'r'
BLACK = 'b'

class RBTreeNode(object):
    
    def __init__(self, key, color=RED, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

