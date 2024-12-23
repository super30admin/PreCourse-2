# Python program for implementation of Quicksort
# Time Complexity - O(n log n)
# Space Complexity - O(log n)

# same as exercise 2
def partition(arr, l, h):
    pivot = arr[h]  # Choose the last element as the pivot
    i = l - 1  # Index for the smaller element
    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    arr[i + 1], arr[h] = arr[h], arr[i + 1]  # Place pivot in the correct position
    return i + 1

def quickSortIterative(arr, l, h):
    # Creating auxiliary stack
    size = h - l + 1
    stack = [0] * size

    # Initialize top of stack
    top = -1

    # Push initial values of l and h to the stack
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    # popping from stack while it is not empty
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        # Set pivot element at its correct position
        p = partition(arr, l, h)

        # If there are elements on the left side of the pivot,
        # push left side to stack
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        # If there are elements on the right side of the pivot,
        # pushing right side to stack
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h

# driver code
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    print("Given array is")
    print(arr)
    quickSortIterative(arr, 0, n - 1)
    print("Sorted array is")
    print(arr)

