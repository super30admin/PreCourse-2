# Time Complexity: O(nlogn)
# Space Complexity: O(n)
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
  stack = []
  stack.append((l, h))
  while stack:
      l, h = stack.pop()
      if l < h:
          p = partition(arr, l, h)
          if p - 1 > l:
              stack.append((l, p - 1))
          if p + 1 < h:
              stack.append((p + 1, h))

