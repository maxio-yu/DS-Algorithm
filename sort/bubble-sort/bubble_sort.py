#!/usr/bin/python

def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(len(array)-1, i, -1):
            if (array[j] < array[j-1]):
                tmp = array[j]
                array[j] = array[j-1]
                array[j-1] = tmp

A = [4,2,5,1,9,6,8,3,0,7]
print "Before sort:"
print A
bubble_sort(A)
print "After sort:"
print A

