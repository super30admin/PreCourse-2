# Python program for implementation of Quicksort
# time complexity O(nlogn)
# Space complexity O(1)

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
      if arr[j] <= pivot:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i + 1


def quickSortIterative(arr, low, high):
  #write your code here
  if low >= high:
        return

  # Create an auxiliary stack to store the lower and upper bounds of the array segments
  size = high - low + 1
  stack = [0] * size
  
  # Initialize the top of the stack
  top = -1
  
  # Push the initial values of low and high to the stack
  top += 1
  stack[top] = low
  top += 1
  stack[top] = high
  
  # Keep popping from the stack while it's not empty
  while top >= 0:
      # Pop high and low
      high = stack[top]
      top -= 1
      low = stack[top]
      top -= 1
      
      # Set pivot element at its correct position in the sorted array
      pivot_index = partition(arr, low, high)
      
      # If there are elements on the left side of the pivot, push the left side to the stack
      if pivot_index - 1 > low:
          top += 1
          stack[top] = low
          top += 1
          stack[top] = pivot_index - 1
      
      # If there are elements on the right side of the pivot, push the right side to the stack
      if pivot_index + 1 < high:
          top += 1
          stack[top] = pivot_index + 1
          top += 1
          stack[top] = high

