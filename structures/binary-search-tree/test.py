#!/usr/bin/python

from binary_search_tree import BSTree

tree = BSTree()
tree.insert(5)
tree.insert(2)
tree.insert(3)
tree.insert(8)
tree.insert(7)
tree.insert(1)
tree.insert(9)

print ("init tree")
tree.inOrderWalk()

print ("delete 2:")
tree.delete(2)
tree.inOrderWalk()

print ("insert 4:")
tree.insert(4)
tree.inOrderWalk()

print ("delete 5 which is root:")
tree.delete(5)
tree.inOrderWalk()

print ("insert 7.5:")
tree.insert(7.5)
tree.inOrderWalk()

