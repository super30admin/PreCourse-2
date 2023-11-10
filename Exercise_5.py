# Time complexity: O(n*n)
# Space complexity: O(n)

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = l-1
  pivot = arr[h]                           # Initial pivot is the last element.
  for j in range(l, h):
      if arr[j] <= pivot:
          i+=1
          arr[i], arr[j] = arr[j], arr[i]     # Swapping elements.
          
  arr[i+1], arr[h] = arr[h], arr[i+1]       # Swapping the pivot element.
  return i+1

def quickSortIterative(arr, l, h):
  #write your code here
  stack = [0] * (h-l+1)
  top = 0
  stack[top] = l
  top += 1
  stack[top] = h
  while top >= 0:
    h = stack[top]
    top -= 1
    l = stack[top]
    top -= 1
    pivot = partition(arr, l, h)
    if pivot-1 > l:
      top += 1
      stack[top] = l
      top += 1
      stack[top] = pivot-1
    if pivot+1 < h:
      top += 1
      stack[top] = pivot+1
      top += 1
      stack[top] = h
  

