# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSortIterative(arr, low, high):
    size = high - low + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    while top >= 0:

        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        pivot = partition(arr, low, high)

        if pivot - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = pivot - 1

        if pivot + 1 < high:
            top = top + 1
            stack[top] = pivot + 1
            top = top + 1
            stack[top] = high

arr = [5,4,3,2,1]
print("Before: ", arr)
quickSortIterative(arr, 0, len(arr)-1)
print ("After: ", arr)

