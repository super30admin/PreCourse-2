# Python program for implementation of Quicksort

## Time complexity: Best O(n logn), Worst O(n^2)
## Space complexity: O(n)

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1



def quickSortIterative(arr, l, h):
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * size

    # Initialize top of stack
    top = -1

    # Push initial values of l and h to stack
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    # Keep popping from stack while is not empty
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        # Set pivot element at its correct position in sorted array
        p = partition(arr, l, h)

        # If there are elements on left side of pivot, then push left side to stack
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        # If there are elements on right side of pivot, then push right side to stack
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" ")
