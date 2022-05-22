# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
from collections import deque


def partition(arr, l, h):
    # write your code here
    pivot = arr[h]
    i = l
    for j in range(l, h):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i = i + 1
    arr[i], arr[h] = arr[h], arr[i]
    return i


def quickSortIterative(arr, l, h):
    # write your code here
    stack = deque()
    stack.append((l, h))
    while stack:
        l, h = stack.pop()
        pivot = partition(arr, l, h)
        if pivot - 1 > l:
            stack.append((l, pivot - 1))
        if pivot + 1 < h:
            stack.append((pivot + 1, h))

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),