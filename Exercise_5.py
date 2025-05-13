# Time Complexity: O(n^2)
# Space Complexity: 
# Did this code successfully run on Leetcode: yes
# Any problem you faced while coding this: no

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1  

  for j in range(l, h):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i] 

  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return i + 1


def quickSortIterative(arr, l, h):
  size = h - l + 1
  stack = [0] * size

  # Initialize top of stack
  top = -1

  top += 1
  stack[top] = l
  top += 1
  stack[top] = h

  # Pop from stack while it's not empty
  while top >= 0:
    # Pop h and l
    h = stack[top]
    top -= 1
    l = stack[top]
    top -= 1

    p = partition(arr, l, h)

    # If elements on the left of pivot, push to stack
    if p - 1 > l:
      top += 1
      stack[top] = l
      top += 1
      stack[top] = p - 1

    # If elements on the right of pivot, push to stack
    if p + 1 < h:
      top += 1
      stack[top] = p + 1
      top += 1
      stack[top] = h

if __name__ == '__main__':
  arr = [4, 3, 7, 6, 2, 1, 9]
  n = len(arr)
  print("Original array:")
  print(arr)
  quickSortIterative(arr, 0, n - 1)
  print("Sorted array:")
  print(arr)