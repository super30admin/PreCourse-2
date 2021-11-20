# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[l]
    i = l
    j = h
    while i <= j:
        #moving one pointer to right
        while arr[i] < pivot:
            i += 1
        #moving other pointer to left
        while arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j -= 1
    if i > j:
        arr[l],arr[i] = arr[i],arr[l]
    return i


def quickSortIterative(arr, l, h):
