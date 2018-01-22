#!/usr/bin/python

def quick_sort(array):
    sub_sort(array, 0, len(array)-1)

def partition(array, start, end):
    i = start
    current = start
    for current in range(start, end):
        if (array[current] < array[end] and current > i):
            tmp = array[i]
            array[i] = array[current]
            array[current] = tmp
            i = i+1

    tmp = array[end]
    array[end] = array[i]
    array[i] = tmp
    return i

def sub_sort(array, start, end):
    if (start < end):
        q = partition(array, start, end)
        sub_sort(array,start,q-1)
        sub_sort(array,q+1,end)


A = [4,2,5,1,9,6,8,3,0,7]
print "Before sort:"
print A
quick_sort(A)
print "After sort:"
print A



    
