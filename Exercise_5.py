# Python program for implementation of Quicksort
# Time Complexity: O(nlogn)

# This function is same in both iterative and recursive
def partition(arr, l, h):
  smallIdx = l - 1
  pivot = arr[h]

  for j in range(l, h):
    if arr[j] <= pivot:
      smallIdx += 1
      arr[smallIdx], arr[j] = arr[j], arr[smallIdx]
  arr[smallIdx + 1], arr[h] = arr[h], arr[smallIdx + 1]
  return smallIdx + 1
  

def quickSortIterative(arr, l, h):
  stack_len = h - l + 1
  stack = [0] * stack_len

  stack_first = -1
  stack_first += 1
  stack[stack_first] = l
  stack_first += 1
  stack[stack_first] = h

  while stack_first >= 0:
    h = stack[stack_first]
    stack_first -= 1
    l = stack[stack_first]
    stack_first -= 1
    pIdx = partition(arr, l, h)
    if pIdx-1 > l:
      stack_first += 1
      stack[stack_first] = l
      stack_first += 1
      stack[stack_first] = pIdx - 1
    if pIdx + 1 < h:
      stack_first += 1
      stack[stack_first] = pIdx + 1
      stack_first += 1
      stack[stack_first] = h
