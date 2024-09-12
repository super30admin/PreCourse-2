# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(array,start,end):
    #write your code here
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def quickSortIterative(arr, l, h):
  #write your code here
    return

