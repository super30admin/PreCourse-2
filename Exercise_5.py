# Python program for implementation of Quicksort

# Time Complexity: Best, Average Case: O(n log n), Worst Case: O(n^2)
# Space Complexity: O(log n) due to the iterative stack space used by the algorithm

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[l]
    i = l
    j = h
    while i < j:
        while i <= h and arr[i] <= pivot:
            i += 1
        while j >= l and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quickSortIterative(arr, l, h):
    # Stack for storing l and h
    stack = []
    # Push initial values of l and h
    stack.append((l, h))
    # Keep popping from stack while it's not empty
    while stack:
        l, h = stack.pop()
        if l < h:
            p = partition(arr, l, h)
            # Push left subarray bounds
            stack.append((l, p - 1))
            # Push right subarray bounds
            stack.append((p + 1, h))
