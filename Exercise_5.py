# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

def swap (arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

# from geeks for geeks
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1
  
  for j in range(l, h):
    if arr[j] <= pivot:
      i = i + 1
      swap(arr, i, j)
  
  swap(arr, i+1, h)
  return i+1
  


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

if __name__ == "__main__":
  arr = [4, 3, 5, 2, 1, 3, 2, 3]
  n = len(arr)
  quickSortIterative(arr, 0, n-1)
  print ("Sorted array is:")
  for i in range(n):
    print ("%d" %arr[i]),
