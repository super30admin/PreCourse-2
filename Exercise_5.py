# Author : Akaash Trivedi
# Time Complexity : O(n log n) 
# Worst n^2
# Space Complexity : O(lon n)
# worst O(n)
# Did this code successfully run on Leetcode : Leetcode #912
# Any problem you faced while coding this : No

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  i = l
  j =h-1
  pivot = arr[h]

  while i<j:
    while i<h and arr[i] < pivot:
      i += 1
    while j > l and arr[j] >= pivot:
      j -= 1
      if i < j:
        arr[i], arr[j] = arr[j], arr[i]

  if arr[i] > pivot:
    arr[i], arr[h] = arr[h], arr[i]

  return i

def quickSortIterative(arr, l, h):
  stack = [(l,h)]

  while stack:
    l, h = stack.pop()
    if l < h:
      p = partition(arr, l, h)
      if p - 1 > l:
        stack.append((l, p - 1))

      if p + 1 < h:
        stack.append((p + 1, h))

