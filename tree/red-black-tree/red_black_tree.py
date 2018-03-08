#!/usr/bin/python

from red_black_tree_node import *

class RBTree(object):

    def __init__(self):
        self.nil = RBTreeNode()
        self.root = self.nil

    def insert(self, x):
        node = RBTreeNode(x, RED, self.nil, self.nil)
        if self.root == self.nil:
            self.root = node
            node.parent = self.nil
        else:
            self._insert(self.root, node)

        self.fixAfterInsert(node)

    def _insert(self, current, node):
        if node.key < current.key:
            if current.left != self.nil:
                self._insert(current.left, node)
            else:
                node.parent = current
                current.left = node
        else:
            if current.right != self.nil:
                self._insert(current.right, node)
            else:
                node.parent = current
                current.right = node

    def fixAfterInsert(self, node):
        # Case 1: new node is root
        if self.root == node:
            node.color = BLACK
        # Case 2: new node's parent is BLACK
        elif node.parent.color == BLACK:
            return
        # Case 3&4: parent is RED 
        else:
            # Case 3: uncle is RED 
            if node.parent.parent.left.color == RED and node.parent.parent.right.color == RED:
                node.parent.parent.color = RED
                node.parent.parent.right.color = BLACK 
                node.parent.parent.left.color = BLACK
                self.fixAfterInsert(node.parent.parent)
            # Case 4: uncle is BLACK 
            else:
                # Case 4.1: parent is grand-parent's left child
                if node.parent.parent.left == node.parent:
                    # case 4.1.1: node is right child
                    if node.parent.right == node:
                        self.leftRotate(node.parent)
                        node = node.left
                    # case 4.1.2: node is left child
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.rightRotate(node.parent.parent)
                # Case 4.2: parent is grand-parent's right child
                elif node.parent.parent.right == node.parent:
                    # case 4.2.1: node is left child
                    if node.parent.left == node:
                        self.rightRotate(node.parent)
                        node = node.right
                    # case 4.2.2: node is right child
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.leftRotate(node.parent.parent)


    def delete(self, x):
        to_delete = self.find(x)
        if to_delete != self.nil:
            self._delete(to_delete)


    def _delete(self, node):

        if node.left == self.nil or node.right == self.nil:
            to_delete = node
        else:
            to_delete = self._findMin(node.right)
            node.key = to_delete.key

        if to_delete.left != self.nil:
            curr = to_delete.left
        else:
            curr = to_delete.right

        curr.parent = to_delete.parent
        if to_delete.parent == self.nil:
            self.root = curr
        elif to_delete == to_delete.parent.left:
            to_delete.parent.left = curr
        else:
            to_delete.parent.right = curr

        # case 0: delete node is RED, do nothing
        if to_delete.color == BLACK:
            self.fixAfterDelete(curr)


    def fixAfterDelete(self, node):
        # case 5: node is root, end while and make it BLACK
        # case 6: color is RED, end while and make it BLACK
        while (node != self.root and node.color == BLACK):
            if node == node.parent.left:
                sibling = node.parent.right
                # case 1: sibling is RED, change to case 2/3/4
                if sibling.color == RED:
                    sibling.color = node.parent.color
                    node.parent.color = RED
                    self.leftRotate(node.parent)
                    sibling = node.parent.right

                # case 2: sibling is B, sibling's 2 child is B
                if sibling.left.color == BLACK and sibling.right.color == BLACK:
                    sibling.color = RED
                    node = node.parent

                else:
                    # case 3: sibling is B, sibling's right is B, left is R, change to case 4
                    if sibling.right.color == BLACK:
                        sibling.color = RED
                        sibling.left.color = BLACK
                        self.rightRotate(sibling)
                        sibling = node.parent.right

                    # case 4: sibling is B, sibling's right is R
                    sibling.color = node.parent.color
                    node.parent.color = BLACK
                    sibling.right.color = BLACK
                    self.leftRotate(node.parent)
                    # in case 4, special case is Root changed, need to re-color the root
                    node = self.root

            else:
                sibling = node.parent.left
                # case 1: sibling is RED, change to case 2/3/4
                if sibling.color == RED:
                    sibling.color = node.parent.color
                    node.parent.color = RED
                    self.rightRotate(node.parent)
                    sibling = node.parent.left

                # case 2: sibling is B, sibling's 2 child is B
                if sibling.left.color == BLACK and sibling.right.color == BLACK:
                    sibling.color = RED
                    node = node.parent

                else:
                    # case 3: sibling is B, sibling's left is B, right is R, change to case 4
                    if sibling.left.color == BLACK:
                        sibling.color = RED
                        sibling.right.color = BLACK
                        self.leftRotate(sibling)
                        sibling = node.parent.right

                    # case 4: sibling is B, sibling's left is R
                    sibling.color = node.parent.color
                    node.parent.color = BLACK
                    sibling.left.color = BLACK
                    self.rightRotate(node.parent)
                    # in case 4, special case is Root changed, need to re-color the root
                    node = self.root

        node.color = BLACK


# Note: change root in rotate function
    def rightRotate(self, node):
        if node == self.root:
            self.root = node.left

        parent = node.parent
        left = node.left
        left_right = left.right

        left.parent = parent
        if parent != self.nil:
            if parent.left == node:
                parent.left = left
            elif parent.right == node:
                parent.right = left

        left.right = node
        node.parent = left
        node.left = left_right
        left_right.parent = node


    def leftRotate(self, node):
        if node == self.root:
            self.root = node.right

        parent = node.parent
        right = node.right
        right_left = right.left

        right.parent = parent
        if parent != self.nil:
            if parent.left == node:
                parent.left = right
            elif parent.right == node:
                parent.right = right

        right.left = node
        node.parent = right
        node.right = right_left
        right_left.parent = node


    def find(self, x):
        return self._find(self.root, x)

    def _find(self, current, x):
        while current != self.nil:
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
            if current.left != self.nil:
                current = current.left
            else:
                return current

    def findMax(self):
        return self._findMax(self.root)

    def _findMax(self, current):
        while True:
            if current.right != self.nil:
                current = current.right
            else:
                return current
    
    def inOrderWalk(self):
        current = self.root
        self._inOrderWalk(current)
        print "\n" 

    def _inOrderWalk(self, current):
        if current.left != self.nil:
            self._inOrderWalk(current.left)
        if current != self.nil:
            print (current.key, current.color),
        if current.right != self.nil:
            self._inOrderWalk(current.right)
