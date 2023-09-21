# Python program for implementation of Quicksort
# Time Complexity : O(nlogn)
# Space Complexity : O(n) n , is the length of stack
# Did this code successfully run on Leetcode : LC 912 yes
# Any problem you faced while coding this : Never coded quick sort iterative, just learnt, thanks

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here

  #can pick any element as pivot 
  # I picked last one
  p = arr[h]

  # pointer to keep trck of the element greater than pivot
  j = l - 1

  # compare each one with pivot
  for i in range(l, h):

    # swap element less than pivot with greater tracked by j 
    if arr[i] <= p:
      j += 1
      arr[i], arr[j] = arr[j], arr[i]
  
  # finally swap  pivot with greater than pivot tracked by j
  arr[j+1], arr[p] = arr[p], arr[j+1]

  # return the partition point
  return j+1

def quickSortIterative(arr, l, h):
  #write your code here

    # Create a stack
    size = h - l + 1
    stack = [0] * (size)
  
    # top of stack
    top = -1
  
    # push l and h to stack
    stack[top + 1] = l
    stack[top + 1] = h
  
    # Loop and pop from stack while is not empty
    while top >= 0:
  
        # Pop h and l
        h = stack[top]
        l = stack[top - 1]
        top -= 1
  
        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h)
  
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            stack[top + 1] = l
            stack[top + 1] = p - 1
  
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            stack[top + 1] = p + 1
            stack[top + 1] = h


