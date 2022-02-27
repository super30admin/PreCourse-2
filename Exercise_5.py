# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
from syslog import LOG_WARNING


def partition(arr, l, h):
  pivot = arr[h]
  i = l-1
  for j in range(l,h):
      if arr[j] <= pivot:
          i = i+1
          (arr[i],arr[j]) = (arr[j],arr[i])
      (arr[i+1],arr[h]) = (arr[h],arr[i+1])
  return i+1


def quickSortIterative(arr, l, h):
  length = h - l +1
  stack = [0] * length
  top = -1
  top = top+1
  stack[top] = l
  top = top+1
  stack[top] = h
  while top >=0:
    h = stack[top]
    top = top - 1
    l = stack[top]
    top = top - 1
    part_index = partition(arr,l,h)
    if part_index - 1 < l:
      top = top+1
      stack[top] = l
      top = top+1
      stack[top] = part_index - 1
    if part_index + 1 > h:
      top = top+1
      stack[top] = part_index + 1
      top = top+1
      stack[top] = h

