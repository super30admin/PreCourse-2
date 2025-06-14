"""
# Time Complexity : 

# Time Complexity : O(nlog N), best and average cases, 
# O(n^2) worst case if array is skewed with pivot at one end already sorted

# Space Complexity : 
O(logN) for recursive call stack on average, O(N) worse case

# Did this code successfully run on Leetcode : N/A, performed local testing

# Any problem you faced while coding this : 
> did not know how to approach iterative stack approach, could not recall last time I solved this problem
> had to refer to implementation to understand how the ranges instead are pushed into the stack one by one

"""

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = h
  pivotVal = arr[h]

  i = l - 1

  for j in range(l, h):
    if arr[j] <= pivotVal:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[pivot] = arr[pivot], arr[i + 1]

  return i + 1



def quickSortIterative(arr, l, h):
  #write your code here
  stack = [0] * (h - l + 1)

  top = -1

  top += 1
  stack[top] = l
  top += 1
  stack[top] = h

  while top >= 0:
    h = stack[top]
    top -= 1
    l = stack[top]
    top -= 1

    p = partition(arr, l, h)

    if p -1 > l:
      top += 1
      stack[top] = l
      top += 1
      stack[top] = p - 1
    
    if p + 1 < h:
      top += 1
      stack[top] = p + 1
      top += 1
      stack[top] = h



