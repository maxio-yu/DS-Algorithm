#!/usr/bin/python

def stooge_sort(array):
    sub_sort(array, 0, len(array)-1)

def sub_sort(array, start, end):
    if (array[start] > array[end]):
        tmp = array[start]
        array[start] = array[end]
        array[end] = tmp

    if (start+1 >= end):
        return
    else:
        k = (end-start+1)/3
        sub_sort(array, start, end-k)
        sub_sort(array, start+k, end)
        sub_sort(array, start, end-k)

A=[5,3,8,4,0,1,9,2,7,6]
print 'before sort'
print A
stooge_sort(A)
print 'after sort'
print A

