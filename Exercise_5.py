# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = (l - 1)  # Index of smaller element
  pivot = arr[h]  # pivot

  for j in range(l, h):

    # If current element is smaller than or equal to pivot
    if arr[j] <= pivot:
        # increment index of smaller element
        i = i + 1
        arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return (i + 1)


def quickSortIterative(arr, l, h):
  #write your code here
  size = h - l + 1
  stack = [0] * (size)

  # initialize top of stack
  top = -1

  # push initial values of l and h to stack
  top = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h

  # Keep popping from stack while is not empty
  while top >= 0:

    # Pop h and l
    h = stack[top]
    top = top - 1
    l = stack[top]
    top = top - 1

    # Set pi as partitioning index, arr[p] is now
    # at right place
    pi = partition(arr, l, h)

    # If there are elements on left side of pi
    if pi - 1 > l:
        top = top + 1
        stack[top] = l
        top = top + 1
        stack[top] = pi - 1

    # If there are elements on right side of pi
    if pi + 1 < h:
        top = top + 1
        stack[top] = pi + 1
        top = top + 1
        stack[top] = h

