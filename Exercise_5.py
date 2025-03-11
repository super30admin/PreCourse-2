# Python program for implementation of Quicksort
# Time Complexity: O(n log n) on average, O(n^2) in the worst case
# Space Complexity: O(n) due to stack usage in iterative implementation

def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1  # Pointer for smaller element
    
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than pivot
    
    arr[i + 1], arr[h] = arr[h], arr[i + 1]  # Swap pivot to correct position
    return i + 1

def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * size  # Stack to simulate recursion
    
    top = -1
    
    # Push initial values to stack
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h
    
    # Keep popping from stack while it is not empty
    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        
        p = partition(arr, l, h)
        
        # If there are elements on the left side of pivot, push them to stack
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1
        
        # If there are elements on the right side of pivot, push them to stack
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h
