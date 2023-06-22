# Python program for implementation of Quicksort

# Time Complexity : O(n^2)
# Space Complexity : O(logn)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : No


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
  #write your code here
  stack = [(low, high)]

  while stack:
      low, high = stack.pop()
      pivot_index = partition(arr, low, high)

      if pivot_index - 1 > low:
          stack.append((low, pivot_index - 1))

      if pivot_index + 1 < high:
          stack.append((pivot_index + 1, high))
