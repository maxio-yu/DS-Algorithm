#!/usr/bin/python

# we suppose the max number is less than 100

def radix_sort(array):
    for i in xrange(0, 3):
        bucket = [[] for t in range(10)]
        for l in xrange(len(array)):
            radix = (array[l]/(10**i))%10
            bucket[radix].append(array[l])
            new = 0
            for x in bucket:
                if x:
                    for y in x:
                        array[new] = y
                        new = new+1


A=[5,55,12,43,88,23,67,1,2,3]
print 'before sort'
print A
radix_sort(A)
print 'after sort'
print A


