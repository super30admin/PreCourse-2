# Python program for implementation of Quicksort
from collections import deque
# This function is same in both iterative and recursive


def swap (A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(a, start, end):

    pivot = a[end]


    pIndex = start


    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, pIndex)
            pIndex = pIndex + 1


    swap(a, pIndex, end)

    # return `pIndex` (index of the pivot element)
    return pIndex


def quickSortIterative(a, start, end):
    stack = deque()

    # get the starting and ending index of a given list
    start = 0
    end = len(a) - 1

    # push the start and end index of the array into the stack
    stack.append((start, end))

    # loop till stack is empty
    while stack:


        start, end = stack.pop()

        # rearrange elements across pivot
        pivot = partition(a, start, end)


        if pivot - 1 > start:
            stack.append((start, pivot - 1))


        if pivot + 1 < end:
            stack.append((pivot + 1, end))


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),