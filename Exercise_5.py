# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    # write your code here
    start = l
    pivot = arr[h]
    for current in range(l, h):
        if arr[current] < pivot:
            arr[start], arr[current] = arr[current], arr[start]
            start = (start + 1)
    arr[start], arr[h] = arr[h], arr[start]
    return start


def quickSortIterative(arr, l, h):
    # write your code here
    size = h-l+1
    stack = [0]*(size)

    top = -1

    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:

        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        pivot_index = partition(arr, l, h)

        if pivot_index - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = pivot_index - 1

        if pivot_index + 1 < h:
            top = top + 1
            stack[top] = pivot_index + 1
            top = top + 1
            stack[top] = h


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])