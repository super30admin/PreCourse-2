# Author: Vineet Khanna

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive


def partition(arr, l, h):
    pivot = arr[h]
    #starting pointer from 1st element
    p = l

    for i in range(l,h):
        if arr[i]<= pivot:
            arr[i], arr[p] = arr[p], arr[i]
            p+=1
    arr[p], arr[h] = arr[h], arr[p]
    return p

def quickSortIterative(arr, l, h):
  #write your code here
    if l < h:
        p = partition(arr, l, h)
        #left half
        quickSortIterative(arr, l, p - 1)
        #right half
        quickSortIterative(arr, p + 1, h)

a = [99, 879, 2133, 121, 12341, 1, 3324, 3445]
quickSortIterative(a, 0, len(a) - 1)

print(a)
