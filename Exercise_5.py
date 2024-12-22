# Time Complexity:
#     Best case: O(n log n)
#     worst case: O(n^2)

# Space Complexity: O(n)

# Python program for implementation of Quicksort

# Approach:
# This is iterative quick sort, implemented using stack.
# Stack stores the low and high values of the array.
# The partition function is same as the recursive quick sort.
# The partition function is called until the stack is empty.
# Once the stack is empty, the array is sorted.

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[l]
  i = l 
  j = h
  while i < j:
      while arr[i] <= pivot and i < h:
          i += 1
      while arr[j] > pivot and j > l:
          j -= 1
      if i < j:
          arr[i], arr[j] = arr[j], arr[i]
  arr[l], arr[j] = arr[j], arr[l]
  return j

def quickSortIterative(arr, l, h):
  #write your code here

  stack = []

  stack.append(l)
  stack.append(h)

  while stack:
    h = stack.pop()
    l = stack.pop()

    p = partition(arr, l, h)

    if p - 1 > l:
      stack.append(l)
      stack.append(p - 1)

    if p + 1 < h:
      stack.append(p + 1)
      stack.append(h)