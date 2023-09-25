# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = l - 1  # index of smaller element
    pivot = arr[h]  # pivot

    for j in range(l, h):
        # If the current element is smaller or equal to the pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1

def quickSortIterative(arr, l, h):
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * size

    # Initialize top of stack
    top = -1

    # Push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # Keep popping from stack while the stack is not empty
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in sorted array
        p = partition(arr, l, h)

        # If there are elements on the left side of the pivot, push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on the right side of the pivot, push the right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

# Given the previous implementation of partition and quickSortIterative

def printArray(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Driver code
if __name__ == "__main__":
    arr = [4, 3, 5, 2, 1, 7, 6, 8]
    n = len(arr)

    print("Given array is:", end=" ")
    printArray(arr)

    quickSortIterative(arr, 0, n-1)

    print("Sorted array is:", end=" ")
    printArray(arr)
