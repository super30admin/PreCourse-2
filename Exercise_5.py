# Python program for implementation of Quicksort
from collections import deque
# This function is same in both iterative and recursive
def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1
    arr[end], arr[pIndex] = arr[pIndex], arr[end]
    return pIndex

def quickSortIterative(arr):
    stack = deque()
    start = 0
    end = len(arr)-1
    stack.append((start, end))
    while stack:
        start,end = stack.pop()
        pivot = partition(arr, start, end)
        if pivot-1 > start:
            stack.append((start, pivot-1))
        if pivot+1 < end:
            stack.append((pivot+1, end))
if __name__ == '__main__':
    arr = [9,-3,5,2,6,8,-6,1,3]
    quickSortIterative(arr)
    print(arr)
  #write your code here

