# Python program for implementation of Quicksort


# This function is same in both iterative and recursive
def partition(arr, l, h):
    # write your code here
    i = l
    j = h - 1
    pivot = arr[h]

    while i <= j:
        while i <= h and arr[i] < pivot:
            i += 1

        while j >= l and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[h] = arr[h], arr[i]
    return i


def quickSortIterative(arr, l, h):
    # write your code here
    # Create a stack to store the subarray start and end indices
    size = len(arr)
    stack = [0] * size

    # top of stack
    top = -1

    # initial subarray (0 to n-1) to stack
    top += 1
    stack[top] = 0
    top += 1
    stack[top] = size - 1

    # popping from stack until it is empty
    while top >= 0:

        # Pop high and low
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1

        # Partitioning array and get the pivot index
        pivot_index = partition(arr, low, high)

        # elements on the left side of the pivot, push left subarray to stack
        if pivot_index - 1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = pivot_index - 1

        # elements on the right side of the pivot, push right subarray to stack
        if pivot_index + 1 < high:
            top += 1
            stack[top] = pivot_index + 1
            top += 1
            stack[top] = high


def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Given array is:")
    printArray(arr)
    n = len(arr)
    quickSortIterative(arr, 0, n - 1)

    print("Sorted array is:")
    printArray(arr)


# time complexity for quicksort is O(n log n) and O(n) for partition
# space complexity is O(n) for the space used by the stack
