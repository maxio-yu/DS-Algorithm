class BSTreeNode(object):
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
    def hasLeftChild(self):
        return self.left
    def hasRightChild(self):
        return self.right
    def isLeftChild(self):
        return self.parent and self.parent.left == self
    def isRightChild(self):
        return self.parent and self.parent.right == self
    def isLeaf(self):
        return self.left == None and self.right == None
