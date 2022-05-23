"""
Time Complexity : O( n*log(n) )
Not sure
Space Complexity : O(n)
"""


def partition(arr, lower, higher):

  pivot = arr[lower]
  pivot_position = lower
  i = lower + 1
  j = higher

  while i < j:

    while arr[i] <= pivot and i < higher:
      i += 1
    while arr[j] > pivot and j > lower:
      j -= 1

    if i < j:
      arr[i], arr[j] = arr[j], arr[i]

  arr[pivot_position], arr[j] = arr[j], arr[pivot_position]
  return j


def QuickSortIterative(arr, lower, higher):

  stack = [None] * (higher - lower + 1)
  top = -1
  top = top + 1
  stack[top] = lower
  top = top + 1
  stack[top] = higher

  while top >= 0:

    # Pop h and l
    higher = stack[top]
    top = top - 1
    lower = stack[top]
    top = top - 1

    pivot = partition(arr, lower, higher)

    if pivot - 1 > lower:
      top = top + 1
      stack[top] = lower
      top = top + 1
      stack[top] = pivot - 1

    if pivot + 1 < higher:
      top = top + 1
      stack[top] = pivot + 1
      top = top + 1
      stack[top] = higher

array = [15,9,14,7,1,5,6]
print("Original array = ", array)
QuickSortIterative(array,0,len(array)-1)
print("Sorted array = ", array)
