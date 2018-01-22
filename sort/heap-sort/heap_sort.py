#!/usr/bin/python

def max_heapify(array, i, size):
    l = 2*i+1
    r = 2*i+2
    largest = i
    if (l < size and array[l] > array[i]):
        largest = l
    else:
        largest = i

    if (r < size and array[r] > array[largest]):
        largest = r

    if (largest != i):
        tmp = array[i]
        array[i] = array[largest]
        array[largest] = tmp
        max_heapify(array, largest, size)


def build_max_heap(array):
    size = len(array)
    for i in range((size-3)/2, -1, -1):
        max_heapify(array, i, size)

def heap_sort(array):
    build_max_heap(array)
    for heap_size in range(len(array)-1, -1, -1):
        tmp = array[0]
        array[0] = array[heap_size]
        array[heap_size] = tmp
        max_heapify(array, 0, heap_size)


A = [3,1,6,9,7,4,8,2,0,5]
print 'Before sort'
print A
heap_sort(A)
print 'After sort'
print A


