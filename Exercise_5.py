# Time Complexity:
#   Best-case: O(n log n)
#   Average-case: O(n log n)
#   Worst-case: O(n^2)
# Space Complexity:
#   O(log n)

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
    top = -1
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        pivot_index = partition(arr, l, h)

        if pivot_index - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = pivot_index - 1

        if pivot_index + 1 < h:
            top += 1
            stack[top] = pivot_index + 1
            top += 1
            stack[top] = h


# Driver code
arr = [4, 2, 6, 9, 2]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:", arr)
