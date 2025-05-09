# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1
  for j in range(l, h):
      if arr[j] < pivot:
          i += 1
          arr[j], arr[i] = arr[i], arr[j]
      
  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return i + 1


def quickSortIterative(arr, l, h):
  #write your code here
  numLen = h - l + 1
  stack = []
  stack.append([l, h])

  while stack:
    l, h = stack.pop()
    if l >= h:
      continue

    pivotIndex = partition(arr, l, h)
    stack.append([pivotIndex + 1, h])
    stack.append([l, pivotIndex - 1])
arr = [10, 7, 8, 9, 1, 5]
arr = [3,9,2,6,2,4,3,1] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print(arr)


