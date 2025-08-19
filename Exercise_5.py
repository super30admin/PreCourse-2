# Python program for implementation of Quicksort (Iterative)
# Time and Space complexity: 
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# This function is same in both iterative and recursive versions
def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1

    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * size

    # initializeing top of stack
    top = -1

    # Pushing initial values of both l and h onto stack
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    # Continue to pop while stack is not empty
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        p = partition(arr, l, h)

        # If there are elements on left side of pivot, push left side to stack
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        # If there are elements on right side of pivot, push right side to stack
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h


# Driver code
if __name__ == "__main__":
    arr = [4, 2, 6, 9, 3]
    n = len(arr)
    quickSortIterative(arr, 0, n - 1)
    print("Sorted array is:")
    for i in range(n):
        print(arr[i], end=" ")
