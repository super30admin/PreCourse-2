# Python program for implementation of Quicksort

def swap(index1, index2, arr):
    arr[index1], arr[index2] = arr[index2], arr[index1]  

# This function is same in both iterative and recursive
def partition(arr, l, h):
    #write your code here
    index = l
    pivot = arr[index]

    while l < h:
        while l < len(arr) and arr[l] <= pivot:
            l += 1
    
        while arr[h] > pivot:
            h -= 1
    
        if l < h:
            swap(l, h, arr)

    swap(index, h, arr)
    
    return h


def quickSortIterative(arr, l, h):
  #write your code here
  if l < h:
      index = partition(arr, l, h)
      quickSortIterative(arr, l, index - 1)
      quickSortIterative(arr, index + 1, h)

