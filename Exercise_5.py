# Time Complexity : O(NlogN)
# Space Complexity : O(logN)
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
  #write your code here
      size = h - l + 1
      stack = [0] * size
    
      top = -1
    
      top = top + 1
      stack[top] = l
      top = top + 1
      stack[top] = h
    
      while top >= 0:
    
          h = stack[top]
          top = top - 1
          l = stack[top]
          top = top - 1
    
          p = partition(arr, l, h)
    
          if p - 1 > l:
              top = top + 1
              stack[top] = l
              top = top + 1
              stack[top] = p - 1
    
          if p + 1 < h:
              top = top + 1
              stack[top] = p + 1
              top = top + 1
              stack[top] = h

