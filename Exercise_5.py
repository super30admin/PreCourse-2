# Python program for implementation of Quicksort

# This function is same in both iterative and recursive


def partition(arr, l, h):
    i = l - 1
    pivot = arr[h]

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quickSortIterative(arr, low, high):
    size = high - low + 1
    stack = [0] * size
    top = -1

    top += 1
    stack[top] = low
    top += 1
    stack[top] = high

    while top >= 0:

        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1

        p = partition(arr, low, high)

        if p - 1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = p - 1
        if p + 1 < high:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = high


#
if __name__ == "__main__":
    arr = [4, 3, 5, 2, 1, 3, 2, 3]
    print("Given array:", arr)
    quickSortIterative(arr, 0, len(arr) - 1)
    print("Sorted array", arr)
