# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    i = low

    for j in range(low, high):
        if arr[j] <= arr[high]:
            arr[j], arr[i], = arr[i], arr[j]
            i += 1

    arr[high], arr[i] = arr[i], arr[high]

    return i


def quickSortIterative(arr, low, high):
    stack = [0] * (high - low + 1)
    stack[0] = low
    stack[1] = high
    top = 1

    while top >= 0:
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1

        pivot = partition(arr, low, high)

        if pivot - 1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = pivot - 1

        if pivot + 1 < high:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = high

if __name__ == '__main__':
# Driver code to test above
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSortIterative(arr,0,n-1)
    print("Sorted array is:")
    print(arr)

