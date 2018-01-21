#!/usr/local/bin/python

def merge_sort(array):
    sub_sort(array, 0, len(array)-1)

def sub_sort(array, start, end):
    if (start == end):
        return
    elif (start + 1 == end):
        if (array[start] > array[end]):
            tmp = array[start]
            array[start] = array[end]
            array[end] = tmp
    else:
        #Note: not end/2, not (end-start)/2
        sub_sort(array, start, (end+start)/2)
        sub_sort(array, (end+start)/2 + 1, end)
        merge(array, start, (end+start)/2, end)


def merge(array, start, end_start, end):
    first = array[start:end_start+1]
    i = 0
    last = array[end_start+1:end+1]
    j = 0
    for index in range(start, end+1):
        #Note: we need a sentinel card
        if (i == end_start - start + 1):
            array[index] = last[j]
            j = j + 1
        elif (j == end-end_start):
            array[index] = first[i]
            i = i + 1
        elif (first[i] < last[j]):
            array[index] = first[i]
            i = i + 1
        else:
            array[index] = last[j]
            j = j + 1


array = [8,6,1,3,2,7,9,5,4]
print "Before sort:"
print array
merge_sort(array)
print "After sort:"
print array
