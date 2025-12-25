# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  # Choose the rightmost element as pivot
  pivot = arr[h]
  
  # Index of smaller element (indicates right position of pivot)
  i = l - 1
  
  for j in range(l, h):
      # If current element is smaller than or equal to pivot
      if arr[j] <= pivot:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]
  
  # Place pivot at its correct position
  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return i + 1


def quickSortIterative(arr, l, h):
  #write your code here
  # Create an auxiliary stack
  stack = []
  
  # Push initial values of l and h to stack
  stack.append((l, h))
  
  # Keep popping from stack while it is not empty
  while stack:
      # Pop l and h
      l, h = stack.pop()
      
      # Set pivot element at its correct position
      p = partition(arr, l, h)
      
      # If there are elements on left side of pivot, push left side to stack
      if p - 1 > l:
          stack.append((l, p - 1))
      
      # If there are elements on right side of pivot, push right side to stack
      if p + 1 < h:
          stack.append((p + 1, h))

