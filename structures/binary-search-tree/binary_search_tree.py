#!/usr/bin/python

from tree_node import TreeNode

class BSTree(object):

    def __init__(self):
        self.root = None

    def insert(self, x):
        node = TreeNode(x)
        if not self.root:
            self.root = node
        else:
            self._insert(self.root, node)
    
    def _insert(self, current, node):
        if node.key < current.key:
            if current.left:
                self._insert(current.left, node)
            else:
                node.parent = current
                current.left = node
        else:
            if current.right:
                self._insert(current.right, node)
            else:
                node.parent = current
                current.right = node

    
    def delete(self, x):
        to_delete = self.find(x)
        if to_delete:
            if to_delete == self.root:
                if to_delete.left == None and to_delete.right == None:
                    self.root = None
                elif to_delete.left and to_delete.right:
                    self._delete(to_delete)
                elif to_delete.left:
                    to_delete.left.parent = None
                    self.root = to_delete.left
                elif to_delete.right:
                    to_delete.right.parent = None
                    self.root = to_delete.right
            else:
                self._delete(to_delete)


    def _delete(self, node):
        if node.left and node.right:
            right_min = self._findMin(node.right)
            node.key = right_min.key
            self._delete(right_min)
        elif node.left == None and node.right == None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left:
            if node.parent.left == node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        elif node.right:
            if node.parent.left == node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right


    def find(self, x):
        return self._find(self.root, x)

    def _find(self, current, x):
        while current != None:
            if x == current.key:
                return current
            elif x < current.key:
                current = current.left
            else:
                current = current.right
        return current
    
    def findMin(self):
        return self._findMin(self.root)

    def _findMin(self, current):
        while True:
            if current.left:
                current = current.left
            else:
                return current

    def findMax(self):
        return self._findMax(self.root)

    def _findMax(self, current):
        while True:
            if current.right:
                current = current.right
            else:
                return current
    
    def inOrderWalk(self):
        current = self.root
        self._inOrderWalk(current)
        print "\n" 

    def _inOrderWalk(self, current):
        if current.left:
            self._inOrderWalk(current.left)
        print (current.key),
        if current.right:
            self._inOrderWalk(current.right)
