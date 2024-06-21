# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  i = low-1
  x=arr[high]

  for j in range(low, high):
    if arr[j]<=x:
      i=i+1
      arr[i],arr[j]=arr[j],arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i+1
def quickSortIterative(arr, l, h):

  size =high-low+1
  stack=[0]*size
  top=-1
  top=top+1

