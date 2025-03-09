# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[l]
  i = l
  j = h

  while i < j:
      while arr[i] <= pivot and i < h:
          i += 1
      while arr[j] > pivot:
          j -= 1
      if i < j:
          arr[i], arr[j] = arr[j], arr[i]
  arr[l], arr[j] = arr[j], arr[l]
  return j


def quickSortIterative(arr, l, h):
  #write your code here
  stack = [0] * (h - l + 1)
  top = -1

  top = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h

  while top >= 0:
    # Pop h and l
    h = stack[top]
    top = top - 1
    l = stack[top]
    top = top - 1

    # partition() will now pick the pivot element at the right place and return the index
    p = partition(arr, l, h)

    # if elements on the left side of pivot, then push left side
    if p - 1 > l:
      top = top + 1
      stack[top] = l
      top = top + 1
      stack[top] = p - 1

    # if elements on the right side of pivot, then push right side
    if p + 1 < h:
      top = top + 1
      stack[top] = p + 1
      top = top + 1
      stack[top] = h
