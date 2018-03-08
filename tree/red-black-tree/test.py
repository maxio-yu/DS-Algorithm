#!/usr/bin/python

from red_black_tree import RBTree

tree = RBTree()
tree.insert(1)
tree.inOrderWalk()
tree.insert(2)
tree.inOrderWalk()
tree.insert(3)
tree.inOrderWalk()
tree.insert(5)
tree.inOrderWalk()
tree.insert(6)
tree.inOrderWalk()
tree.insert(7)
tree.inOrderWalk()
tree.insert(9)
tree.inOrderWalk()

print ("init tree")
tree.inOrderWalk()

print ("delete 2:")
tree.delete(2)
tree.inOrderWalk()

print ("insert 4:")
tree.insert(4)
tree.inOrderWalk()

tree.delete(5)
tree.inOrderWalk()

print ("insert 8:")
tree.insert(8)
tree.inOrderWalk()

