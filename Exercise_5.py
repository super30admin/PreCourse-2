# Python program for implementation of Quicksort

# Time Complexity : O(n * log n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : N/A, no Leetcode link
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Code uses a stack to manage subarrays which need to be sorted. 
# The stack keeps track of subarray ranges through pairs of indices (l, h). 
# The function initializes the stack and pushes the initial range of the entire array onto it. 
# A loop repeatedly pops subarray ranges from the stack,applies the partition function to find the pivot’s position, 
# and pushes subarray ranges onto the stack for further processing. 
# This loop continues until the stack becomes empty, indicating that all subarrays have been sorted.

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivotElem = arr[h]
  i = l - 1
  
  for j in range(l, h):
    if arr[j] <= pivotElem:
      i = i+1
      arr[i], arr[j] = arr[j], arr[i]
    
  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return i + 1


def quickSortIterative(arr, l, h):
  #write your code here
  sizeLen = h - l + 1
  stack = [0] * (sizeLen)

  top = -1
  
  top = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h

  while top >= 0:
    h = stack[top]
    top = top - 1
    l = stack[top]
    top = top - 1

    p = partition( arr, l, h )

    if p-1 > l:
      top = top + 1
      stack[top] = l
      top = top + 1
      stack[top] = p - 1

    if p+1 < h:
      top = top + 1
      stack[top] = p + 1
      top = top + 1
      stack[top] = h



