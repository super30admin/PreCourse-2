
# T.C : O(nlogN)
# Swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Partition function


def partition(arr, l, h):
    # select pivot
    pivot = arr[h]

    # smaller element index
    i = l - 1

    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    # Move pivot after smaller elements and return its position
    swap(arr, i + 1, h)
    return i + 1

# Iterative QuickSort


def quickSortIterative(arr, l, h):
    # Create an auxiliary stack
    stack = [0] * (h - l + 1)

    # Initialize top of stack
    top = -1

    # Push initial values of l and h to stack
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    # Keep popping from stack while it is not empty
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        # Set pivot element at its correct position
        pivot = partition(arr, l, h)

        # If there are elements on the left of the pivot, push them to the stack
        if pivot - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = pivot - 1

        # If there are elements on the right of the pivot, push them to the stack
        if pivot + 1 < h:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = h


# Driver code
if __name__ == "__main__":
    arr = [4, 7, 2, 9, 3, 6, 1, 5]
    n = len(arr)
    print("Original array:", arr)
    quickSortIterative(arr, 0, n - 1)
    print("Sorted array:", arr)
