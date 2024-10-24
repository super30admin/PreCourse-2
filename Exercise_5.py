# Python program for implementation of Quicksort

# Function to do partition
def partition(arr, low, high):
    # We choose the last element as pivot
    pivot = arr[high]

    # Index of the smaller element, initially set to the start
    i = low - 1

    # Traverse through all elements except the pivot
    for j in range(low, high):
        # If the current element is smaller than the pivot
        if arr[j] < pivot:
            i = i + 1  # Increment the index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Swap the pivot element with the element at i + 1 to place it in the right position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1  # Return the partitioning index (pivot's final position)


def quickSortIterative(arr, l, h):
    # Create an explicit stack to simulate recursion
    size = h - l + 1
    stack = [0] * size

    # Initialize the stack
    top = -1

    # Push the initial values of l and h to the stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # Keep popping from stack while it is not empty
    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in sorted array
        p = partition(arr, l, h)

        # If there are elements on the left side of the pivot, push them to the stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on the right side of the pivot, push them to the stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


# Driver code to test above
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    print("Given array is:")
    print(arr)

    quickSortIterative(arr, 0, n - 1)

    print("Sorted array is:")
    print(arr)