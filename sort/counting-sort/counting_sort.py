#!/usr/bin/python

def counting_sort(array):
    max = 0
    sort_array = [0 for x in range(len(array))]
    for i in range(len(array)):
        if (array[i] > max):
            max = array[i]

    count = [0 for x in range(max+1)]

    for i in range(len(array)):
        count[array[i]] = count[array[i]]+1

    for i in range(1,max+1):
        count[i] = count[i-1] + count[i]

    print count

    for i in range(len(array)):
        sort_array[count[array[i]]-1] = array[i]
        count[array[i]] = count[array[i]] - 1

    return sort_array


A = [4,2,4,5,1,0,9,6,8,3,0,7]
print "Before sort:"
print A
A = counting_sort(A)
print "After sort:"
print A

