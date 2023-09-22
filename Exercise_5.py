# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[h]
    i, j = l, h - 1
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
    stack = [(l, h)]
    while stack:
        start, end = stack.pop()
        pivot=partition(arr, start, end)
        if pivot-1 > start:
            stack.append((l,pivot-1))
        if pivot + 1 < end:
            stack.append((pivot+1,h))


# Driver code to test above
arr = a = [10, 7, 8, 9, 1, 5] 
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for l in range(n):
    print("%d" % arr[l]),


