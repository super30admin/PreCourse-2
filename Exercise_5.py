# Time Complexity : 
# Average and Best case: O(n log n), where n is the number of elements in the array
# Worst case: O(n^2), happens when the pivot selection is poor 
# Space Complexity : O(log n)

# Python program for implementation of Quicksort
# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[h]
  i = l - 1

  for j in range(l, h):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return i + 1

def quickSortIterative(arr, l, h):
  stack = [(0, len(arr) - 1)]

  while stack:
    l, h = stack.pop()

    if l < h:
      p = partition(arr, l, h)
      # Push left and right subarrays to stack
      stack.append((l, p - 1))
      stack.append((p + 1, h))