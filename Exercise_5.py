# Python program for implementation of Quicksort
# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[l]
    i = l + 1
    j = h
    while True:
        while i <= j and arr[i] <= pivot:
            i = i + 1
        while i <= j and arr[j] > pivot:
            j = j - 1
        if i <= j:
            arr[i], arr[j] = arr[j].arr[i]
        else:
            break
    arr[l], arr[j] = arr[j], arr[l]
    return j
    # write your code here

def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * (size)

    top = -1
    top = top + 1
    stack[top] = 1
    top = top + 1
    stack[top] = h

    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        pi = partition(arr, l, h)
        if pi - 1 > l:
            top = top + 1
            stack[top] = 1
            top + 1
            stack[top] = pi - 1

        if pi + 1 < h:
            top = top + 1
            stack[top] = pi + 1
            top = top + 1
            stack[top] = h

    # write your code here

