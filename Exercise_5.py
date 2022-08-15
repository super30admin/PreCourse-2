# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
"""
Description:
This is the iterative version of QuickSort
The idea is to use a stack to keep track of sub-arrays to be sorted.
The first element of the stack is the index of the first element of the sub-array.
The second element of the stack is the index of the last element of the sub-array.
While the stack is not empty, we pop the top two elements from the stack and sort the sub-array.
Partition the array around the pivot and push the sub-array indices to the stack.

Time Complexity: O(n log n)
Time Complexity for quicksort: O(n^2)(Worst Case when array is already sorted or reverse sorted)
Space Complexity: O(log n)
"""
from collections import deque


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    while low <= high:
        if arr[low] <= pivot:
            i += 1
            arr[i], arr[low] = arr[low], arr[i]
        low += 1

        arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1


def quickSortIterative(arr, l, h):

    stack = deque()
    stack.append([l, h])

    while stack:
        l, h = stack.pop()
        p = partition(arr, l, h)
        if p-1 > l:
            stack.append([l, p-1])
        if p+1 < h:
            stack.append([p+1, h])


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
