# Python program for implementation of Iterative Quicksort
# Time Complexity: Average case O(n log n), Worst case O(n^2)
# Space Complexity: O(log n)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : Required some time to revisit partitioning logic and stack usage


def partition(arr, l, h):
    # Choose the last element as pivot
    pivot = arr[h]
    i = l - 1  
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  
    # Place pivot at the correct position
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * size  # Initialize stack of required size
    top = -1

    # Push initial values of l and h onto stack
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

        # Partition the array and get pivot index
        p = partition(arr, l, h)

        # If there are elements on left side of pivot, push left subarray to stack
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        # If there are elements on right side of pivot, push right subarray to stack
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h

arr = [4, 3, 5, 2, 1, 6, 0, 7]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("% d" % arr[i])
