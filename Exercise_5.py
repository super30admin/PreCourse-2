# Python program for implementation of Quicksort
# iterative way

def partition(arr, low, high):
    i = (low - 1)
    x = arr[high]
    for j in range(low, high):
        if arr[j] <= x:
            # increment
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSortIterative(arr, low, high):
    # Creation of a stack
    size = high - low + 1
    stack = [0] * size
    # initialization
    top = -1
    # push initial values
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
    # pop from stack
    while top >= 0:
        # Pop
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
        # Set pivot element at its correct position
        p = partition(arr, low, high)
        # elements on the left
        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1
        # elements on the right
        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high


if __name__ == "__main__":
    # Driver code to test above
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSortIterative(arr, 0, n - 1)
    print("Sorted array is:")
    for i in range(n):
        print("%d" % arr[i], end=' ')
