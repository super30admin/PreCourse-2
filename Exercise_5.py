# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l -1 
  for j in range(l,h):
    if arr[j] < pivot:
        i += 1
        arr[i],arr[j] = arr[j], arr[i]
  i += 1
  arr[i], arr[h] = arr[h], arr[i]
  return i 


def quickSortIterative(arr, l, h):
    if l< h:
      pidx = partition(arr, l , h)
      quickSortIterative(arr, 0, pidx-1)
      quickSortIterative(arr, pidx+1, h)
