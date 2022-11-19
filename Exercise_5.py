# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
# It returns location of x in given array arr  
# if present, else returns -1 
# // Time Complexity : Best - O(nlog(n)), Worst - O(n^2)
# // Space Complexity : O(log(n))
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

def partition(arr, l, h):
  #write your code here
  i = l - 1 
  x = arr[h]
  for j in range(l , h):
      if arr[j] <= x:
          i += 1
          arr[i],arr[j] = arr[j],arr[i]
  arr[i+1],arr[h] = arr[h],arr[i+1]
  return i+1


def quickSortIterative(arr, l, h):
  #write your code here
  size = h - l + 1
  st = [0] * size
  top = -1
  # push initial values
  top += 1
  st[top] = l
  top += 1
  st[top] = h
  # pop from stack
  while top >= 0:
      # Pop
      h = st[top]
      top -= 1
      l = st[top]
      top -= 1
      # Set pivot element at its correct position
      m = partition(arr,l,h)
      # elements on the left
      if m-1 > l:
          top += 1
          st[top] = l
          top += 1
          st[top] = m - 1
      # elements on the right
      if m+1 < h:
          top += 1
          st[top] = m + 1
          top += 1
          st[top] = h


