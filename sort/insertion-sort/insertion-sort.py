#!/usr/local/bin/python

def insertion_sort (arr):
    # no for (i=0;i<xx;i++) in python
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > value):
# When human sorted their card, they will not compare and insert it everytime
# Real human will only compare and insert it in the last right place
# so it's more like a linked node, instead of a array
            arr[j+1] = arr[j]
            # no j-- in python
            j = j - 1
        arr[j+1] = value

array = [8,6,1,3,2,7,9,5,4]
print "Before sort:"
print array
insertion_sort(array)
print "After sort:"
print array


