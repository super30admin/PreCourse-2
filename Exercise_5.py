# Python program for implementation of Quicksort
# Submitted by : Aryan Singh_RN12MAY2023
# Time Complexity : O(n logn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Not applicable
# Any problem you faced while coding this : No 

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[h]
  i = l - 1

  for j in range(l, h):
      if arr[j] <= pivot:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return i + 1


def quickSortIterative(arr, l, h):
    # Calculate the size of the array
    size = h - l + 1
    # Stack to store the indices of sub-arrays
    stack = [0] * size
    # Initialize the top of the stack to -1
    top = -1

    # Push the initial values of l and h onto the stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # Loop until the stack is empty
    while top >= 0:
        # Pop the top two elements from the stack
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Partition the sub-array around a pivot element
        p = partition(arr, l, h)

        # If there are elements to the left of the pivot, 
        # push the indices of the left sub-array onto the stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements to the right of the pivot, 
        # push the indices of the right sub-array onto the stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 