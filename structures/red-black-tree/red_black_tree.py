#!/usr/bin/python

def RBTree(object):

    def __init__(self):
        self.root = None

    def insert(self, x):
        node = RBTreeNode(x, RED)
        if self.root == None:
            self.root = Node
        else:
            self._insert(self.root, node)

        self.fixAfterInsert(node)

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

    def fixAfterInsert(self, node):
        # Case 1: new node is root
        if self.root = node:
            node.color = BLACK
        # Case 2: new node's parent is BLACK
        if node.parent.color == BLACK:
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
                    self.leftRotate(node.parent.parent)
                # Case 4.2: parent is grand-parent's right child
                elif node.parent.parent.right == node.parent:
                    # case 4.2.1: node is left child
                    if node.parent.left == node:
                        self.rightRotate(node.parent)
                        node = node.right
                    # case 4.2.2: node is right child
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.rightRotate(node.parent.parent)


    def fixAfterDelete(self, node):
        return

    def leftRotate(self, node):
        parent = node.parent
        left = node.left
        left_right = left.right

        left.parent = parent
        if parent:
            if parent.left == node:
                parent.left = left
            elif parent.right == node:
                parent.right = right

        left.right = node

        node.parent = left
        node.left = left_right
        if left_right:
            left_right.parent = node


# only using 1 tmp 
#        left = node.left
#        left.parent = node.parent
#        if node.parent:
#            if node.parent.left == node:
#                node.parent.left = left
#            elif node.parent.right == node:
#                node.parent.right = left
#
#        node.parent = left
#
#        node.left = left.right
#        if left.right:
#            left.right.parent = node
#
#        left.right = node
        

    def rightRotate(self, node):

        parent = node.parent
        right = node.right
        right_left = right.left

        right.parent = parent
        if parent:
            if parent.left == node:
                parent.left = right
            elif parent.right == node:
                parent.right = right

        right.left = node

        node.parent = right
        node.right = right_left
        if right_left:
            right_left.parent = node

