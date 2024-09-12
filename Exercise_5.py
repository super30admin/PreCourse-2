#Didnot understand how to implemetn Quicksort Iterative Part
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[high]
    i =low
    while i < len(arr):
        if arr[i] < pivot:
            (arr[i],arr[low]) = (arr[low],arr[i])
            low = low +1
        i+=1
    (arr[low],arr[high]) = (arr[high],arr[low])
    return low
  

def quickSortIterative(arr, l, h):
  while low < high:
      

