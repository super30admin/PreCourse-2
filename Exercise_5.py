# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  i = l-1
  pivot = arr[h]
  for j in range(l,h):
    if arr[j]<=pivot:
      i=i+1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i+1], arr[h] = arr[h], arr[i+1]
  return i+1


  


def quickSortIterative(arr, l, h):
  if l<h:
    p = partition(arr, l, h)
    quickSortIterative(arr, l, p-1)
    quickSortIterative(arr, p+1, h)

