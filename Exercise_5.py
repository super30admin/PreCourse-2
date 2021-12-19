# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot_element = arr[h]
  i = l - 1
  for j in range (l, h):
    if(arr[j] <= pivot_element):
        i += 1
        arr[i], arr[j] = arr[j], arr[i]
  arr[i +1], arr[h] = arr[h], arr[i + 1]
  return i + 1


def quickSortIterative(arr, l, h):
  #write your code here
  if l < h:
    idx = partition(arr, l, h)
    quickSort(arr, l, idx - 1)
    quickSort(arr, idx +1, h)

