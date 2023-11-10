# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  pivot = arr[high]
  i = low-1
  j = low
  while j<high:
    if arr[j] <= pivot:
      i += 1
      arr[i],arr[j]=arr[j],arr[i]
    j += 1
  arr[i+1],arr[high] = arr[high],arr[i+1]
  return i+1

def quickSortIterative(arr, l, h):
  #write your code here
  # Did not understood how to appoach the problem. Need to look online for this one.

