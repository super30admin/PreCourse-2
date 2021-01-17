# Python program for implementation of Quicksort

# Overall complexity: 
# Bestcase: O(nlogn)
# Worst case: O(n^2)
# Average case: O(nlogn)
# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = l -1
  # last element as pivot
  pivot = arr[h]
  for k in range(l,h):
    # if the element is less than the pivot then
    if arr[k] <= pivot:
      # increment i by 1
      i += 1
      # swap the elements
      arr[i], arr[k] = arr[k], arr[i]
  # swap the element at i+1 position with the pivot
  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return (i + 1)

def quickSortIterative(arr, l, h):
  #write your code here
  # size of the arr
  n = h - l - 1
  # initialize a stack of length n
  stack = [0] * n
  top = 0
  # initialize the first element as l
  stack[top] = l
  # increment the top index by 1
  top += 1
  # initialize the next element as h
  stack[top] = h

# check if stack is empty or not
  while top >= 0:
    h = stack[top]
    top -= 1
    l = stack[top]
    top -= 1

    # partition index
    p = partition(arr, l, h)

    # check if end of list is reached or not
    if p-1 > l:
      top += 1
      stack[top] = l
      top += 1
      stack[top] = p-1

    # check if end of list is reached or not
    if p+1 < h:
      top += 1
      stack[top] = p + 1
      top += 1
      stack[top] = h


