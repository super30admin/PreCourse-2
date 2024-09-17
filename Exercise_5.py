# Python program for implementation of Quicksort
from collections import deque
# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = l
  pivot = arr[h]
  for j in range(l,h):
      if arr[j]<=pivot:
          arr[i],arr[j]=arr[j],arr[i]
          i = i + 1
  arr[i],arr[pivot] = arr[pivot],arr[i]
  return i



def quickSortIterative(arr, l, h):
  #write your code here
  stack = deque()

    start = l
    end = h
    stack.append((start, end))

    while stack:
        start, end = stack.pop()
        pivot = partition(arr, start, end)
        if pivot - 1 > start:
            stack.append((start, pivot - 1))
        if pivot + 1 < end:
            stack.append((pivot + 1, end))
