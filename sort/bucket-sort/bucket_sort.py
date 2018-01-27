#!/usr/bin/python

def bucket_sort(array):
    upper = max(array)
#    bucket = [0 for x in range(0,upper+1)]
    bucket = [0] * (upper+1)
    for i in array:
        bucket[i] += 1

    curr = 0
    for j in range(len(bucket)):
        if (bucket[j] != 0):
            while (bucket[j]):
                array[curr] = j
                curr += 1
                bucket[j] -= 1


A = [4,2,7,1,3,4,5,6,9,0,2,5,2,6,8]

print 'before sort'
print A
bucket_sort(A)
print 'after sort'
print A
