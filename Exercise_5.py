# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = (l - 1)
    pivot = arr[h]

    for j in range(l, h):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)


def quickSortIterative(arr, l, high):
    size = high - l + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = high

    while top >= 0:

        high = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        p = partition(arr, l, high)


        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1


        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high

# T(n) = O(nlogn)
# S(n) = O(n)
