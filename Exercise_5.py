# Time Complexity:
#   Best Case: O(n log n)
#   Average Case: O(n log n)
#   Worst Case: O(n^2) [when the smallest or largest element is always picked as pivot]
# Space Complexity:
#   O(h) where h is the height of the stack (log n for balanced, n for worst case)

# Partition function (same as recursive QuickSort)
def partition(arr, l, h):
    pivot = arr[h]  
    i = l - 1  # Index of smaller element

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[h] = arr[h], arr[i + 1]  # Place pivot in the correct position
    return i + 1  # Return partitioning index


# Iterative QuickSort function
def quickSortIterative(arr, l, h):
    # Create an explicit stack for storing subarray start and end indices
    size = h - l + 1
    stack = [0] * size  # Stack to simulate recursion
    top = -1

    # Push initial values of l and h to stack
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    # Pop from stack while it's not empty
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        # Partition the array and get the pivot index
        p = partition(arr, l, h)

        # If elements on the left side of pivot, push them to stack
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        # If elements on the right side of pivot, push them to stack
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h

