# Python program for implementation of Quicksort
# Time Complexity: O(n log n) on average
# Space Complexity: O(log n) for stack (worst case O(n))
# This is the iterative version using an explicit stack

def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i + 1

def quickSortIterative(arr, l, h):
    # Create an explicit stack for storing subarray bounds
    size = h - l + 1
    stack = [0] * size
    top = -1
    # Push initial values of l and h to stack
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h
    # Keep popping from stack while not empty
    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        p = partition(arr, l, h)
        # If elements on left of pivot, push left side to stack
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1
        # If elements on right of pivot, push right side to stack
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h

# Example usage
data = [4, 3, 7, 6, 5, 2, 1]
n = len(data)
quickSortIterative(data, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print(data[i], end=" ")
print()

