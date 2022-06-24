# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  swap_index = l
  pivot_index = l
  for i in range(pivot_index+1, h+1):
    if(arr[i]<arr[pivot_index]):
      swap_index+=1
      arr[swap_index], arr[i] = arr[i], arr[swap_index]
  arr[swap_index], arr[pivot_index] = arr[pivot_index], arr[swap_index]
  return swap_index


def quickSortIterative(arr, l, h):
  if(l<h):
    pivot_index = partition(arr, l, h)
    quickSortIterative(arr, l, pivot_index-1)
    quickSortIterative(arr, pivot_index+1, h)
  return arr

arr = [2,4,3,1,5]
print(quickSortIterative(arr,0, len(arr)-1))