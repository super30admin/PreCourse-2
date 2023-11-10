# Time Complexity : O(N log(N))
# Space Complexity : O(log(N))

# Exercise 5 : Iterative Quick Sort
# Python program for implementation of Quicksort iteratively

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  #setting pivot to l pointer initially
  pivot_index = l
  pivot = arr[pivot_index]

  #base condition, perform loop while l<h, when l overtakes h we will escape while loop and swap h and pivot element
  while l < h:
      # perform check while l does not exceed length of array and till we find element that is greater than pivot
      while l < len(arr) and arr[l] <= pivot:
          l += 1
      #perform check till we find element that is ler than pivot
      while arr[h] > pivot:
          h -= 1
      #if the l pointer overtakes h the last time, we will stop decrementing or incrementing, and swap both elements respectively
      if l < h:
          arr[l], arr[h] = arr[h], arr[l]
  #once l overtakes h, we will swap the pivot element with h, and now we have pivot element sorted
  arr[h],arr[pivot_index] = arr[pivot_index], arr[h]
  #we simply return the value of the h element that we swapped, so we can proceed to partition
  return h


def quickSortIterative(arr, l, h):
  size = h - l + 1
  stack = [0] * size

  #initialize top of stack
  top = -1

  #push values of l and h to stack
  top = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h

  #keep popping while stack not empty
  while top >= 0:

    h = stack[top]
    top = top - 1
    l = stack[top]
    top = top - 1

    p = partition(arr, l , h)

    #if elements are present on left side, then push left side to stack
    if p - 1 > l:
      top = top + 1
      stack[top] = l
      top = top + 1
      stack[top] = p - 1

    #if elements are present on right side, then push right side to stack
    if p + 1 < h:
      top = top + 1
      stack[top] = p + 1
      top = top + 1
      stack[top] = h

