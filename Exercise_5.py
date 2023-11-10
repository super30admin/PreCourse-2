# Time Complexity : O(nlog(n)) 
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Python program for implementation of Quicksort 
  
# This function is same in both iterative and recursive
def partition(arr, l, h):
  i = ( l - 1 )
  x = arr[h]

  for j in range(l, h):
      if   arr[j] <= x:

          # increment smaller element index
          i = i + 1
          arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return (i + 1)
  
# Function to do Quick sort
def quicksort_iterative(arr, l, h):
  
  size = h - l + 1
  stack = [0] * (size)

  top = -1

  # push initial values
  top = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h
  
  # Keep popping
  while top >= 0:

      h = stack[top]
      top = top - 1
      l = stack[top]
      top = top - 1

      # Set pivot element
      # sorted array
      p = partition( arr, l, h )

      if p-1 > l:
          top = top + 1
          stack[top] = l
          top = top + 1
          stack[top] = p - 1

      if p + 1 < h:
          top = top + 1
          stack[top] = p + 1
          top = top + 1
          stack[top] = h

