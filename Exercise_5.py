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
  stack = []

  stack.append((l, h))

  while stack:
      l, h = stack.pop()

      pivot_index = partition(arr, l, h)

      if pivot_index - 1 > l:
          stack.append((l, pivot_index - 1))

      if pivot_index + 1 < h:
          stack.append((pivot_index + 1, h))

