#!/usr/bin/python

def select_sort(array):
    for i in range(0, len(array)):
        max_i = 0
        for j in range(0,len(array) - i):
            if (array[j] > array[max_i]):
                max_i = j
        array[-1-i],array[max_i] = array[max_i],array[-1-i]


A=[1,3,2,6,7,0,4,9,5,8]
print 'before sort:'
print A
select_sort(A)
print 'after sort:'
print A
