# Implementation of iterative Quicksort

# This function is same in both iterative and recursive
from typing import Deque


def partition(arr, l, h):
  #write your code here
  i = l - 1
  pivot = arr[h]

  for j in range(l, h):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i+1], arr[h] = arr[h], arr[i+1]

  return i+1


def quickSortIterative(arr, l, h):
  #write your code here
  stack = Deque()

  start = 0
  end = len(arr) - 1

  stack.append((start, end))

  while stack:
    start ,end = stack.pop()

    pivot = partition(arr, start, end)

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
  

