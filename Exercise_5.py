# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    #write your code here
    i = l - 1
    pivot = arr[h]
    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1


# Using Stack DS to mimic recursive behavior.
def quickSortIterative(arr, l, h):
    #write your code here
    stack = []
    stack.append((l, h))

    while stack:
        low, high = stack.pop()
        if low >= high:
            continue

        pi = partition(arr, low, high)
        stack.append((low, pi - 1))
        stack.append((pi + 1, high))
