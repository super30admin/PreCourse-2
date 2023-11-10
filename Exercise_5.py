# Python program for implementation of Quicksort
"""
    time complexity: O(nlog(n))
    space complexity: O(n)
"""


# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = l
    j = h-1
    pivot = arr[h]
    while i < j:
        while i < h and arr[i] < pivot:
            i += 1
        while j > l and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[h] = arr[h], arr[i]
    return i


def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * size
    top = 0
    stack[top] = l
    top += 1
    stack[top] = h

    while top >= 0:
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1
        position = partition(arr, low, high)

        if position-1 > low:
            top += 1
            stack[top] = low
            top = top + 1
            stack[top] = position - 1
        if position + 1 < high:
            top += 1
            stack[top] = position + 1
            top = top + 1
            stack[top] = high


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])

