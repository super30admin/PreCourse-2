# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    p = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= p: #shifts all the elements less than pivot to left
            i += 1
        while i <= j and arr[j] >= p: #shifts all the elements greater than pivot to right
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i] #shifting done here
        else:
            break
    arr[low], arr[j] = arr[j], arr[low] #swaping of pivot and the jth element, point where pivot is correctly placed
    return j
  #write your code here


def quickSortIterative(arr, l, h):
  #write your code he