"""
Time Complexity : O( n*log(n) )
Not sure
Space Complexity : O(n)
Did this code successfully run on Leetcode : N/A
Any problem you faced while coding this : Finding that stack is to be used was very much challenging task.
                                          Also, setting fixed size to that stack because python used dynamic
                                          memory allocation.
"""
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  '''
  using same logic as used in normal Quick sort
  :param arr: array
  :param l: lower bound
  :param h: higher bound
  :return: position of pivot
  '''
  pivot = arr[l]
  pivot_position = l
  i = l + 1
  j = h

  while i < j:

    while arr[i] <= pivot and i < h:
      i += 1
    while arr[j] > pivot and j > l:
      j -= 1

    if i < j:
      arr[i], arr[j] = arr[j], arr[i]

  arr[pivot_position], arr[j] = arr[j], arr[pivot_position]
  return j


def quickSortIterative(arr, l, h):
  '''
  Using stack here.
  In iterative approach, we store position of left side and right side in stack.
  Like pivot is at position 3, then left side will be 0,2 and right side will be 4, <size of array>
                                                (lower, higher bound)
  stack will have lower and higher bound positions of left and right side and we will pop one by one and
  apply partition function untill stack becomes empty(top = -1).
  :param arr: array
  :param l: lower bound
  :param h: higher bound
  :return: None
  '''

  stack = [None] * (h - l + 1)
  print(stack)

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

    pivot = partition(arr, l, h)
    #print(arr[p])

    if pivot - 1 > l:
      top = top + 1
      stack[top] = l
      top = top + 1
      stack[top] = pivot - 1

    if pivot + 1 < h:
      top = top + 1
      stack[top] = pivot + 1
      top = top + 1
      stack[top] = h

arr = [10, 7, 8, 9, 1, 5]
print("old array = ", arr)
quickSortIterative(arr,0,len(arr)-1)
print("New sorted array = ", arr)