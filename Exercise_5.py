# Time complexity: O(n log n)
# Space complexity: O(log n)

# Python program for implementation of Quicksort
def partition(arr, low, high):
    # Select the rightmost element as pivot
    pivot = arr[high]

    # Index of the smaller element within the current subarray
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_iterative(arr, low, high):
    if low >= high:
        return

    stack = [(low, high)]

    while stack:
        low, high = stack.pop()
        pivot_index = partition(arr, low, high)

        # Push subarrays containing at least two elements
        if low < pivot_index - 1:
            stack.append((low, pivot_index - 1))

        if pivot_index + 1 < high:
            stack.append((pivot_index + 1, high))