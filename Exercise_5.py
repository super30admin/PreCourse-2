#Time Complexity : O(n log n) on average, O(n^2) in worst case
#Space Complexity : O(log n) on average, O(n) in worst case

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[h]
    j = l - 1
    for i in range(l, h):
        if arr[i] < pivot:
            j = j+1
            arr[j], arr[i] = arr[i], arr[j]
    arr[h], arr[j+1] = arr[j+1], arr[h]
    return j+1

def quickSortIterative(arr, l, h):
    stack = []
    stack.append((l, h))
    while stack:
        low, high = stack.pop()
        if low < high:
            r = partition(arr, low, high)
            stack.append((low, r-1))
            stack.append((r+1, high))
