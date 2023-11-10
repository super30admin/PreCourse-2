# Python program for implementation of Quicksort
# T.C O(nlogn)
# S.C O(logn)
# This function is same in both iterative and recursive
def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1

  while low < high:
      if arr[low] < pivot:
          i += 1
          arr[i], arr[low] = arr[low], arr[i]
      low += 1
  # print(i + 1, high)
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i + 1


def quickSortIterative(arr, l, h):
  #write your code here
  stack = [(l, h)]

  while stack:
    xl, xh = stack.pop(0)
    if xl > xh:
      continue
    part = partition(arr, xl, xh)
    stack.append((xl, part - 1))
    stack.append((part + 1, xh))

  print(arr)

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1)