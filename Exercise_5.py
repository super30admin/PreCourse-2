# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  low_index = (l - 1)
  pivot = arr[h]
  
  for i in range(l, h):
      if arr[i] <= pivot:
          low_index = low_index + 1
          arr[low_index], arr[i] = arr[i], arr[low_index]
  arr[low_index+1], arr[h] = arr[h], arr[low_index+1]
  return (low_index+1)


def quickSortIterative(arr, l, h):
  #write your code here
  size = h - l + 1
  stack = [0] * (size)
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
    
    p = partition(arr, l,h)
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
      
# Driver code to test above 
arr = [10, 6, 3, 2, 5, 11, 1, 6, 0, 2] 
quickSortIterative(arr, 0, len(arr)-1) 
for i in range(len(arr)): 
    print('%d' % arr[i]), 
