# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    pivot = arr[high]
    # pointer to track pivot position
    pivotIndex = 0
    for i in range(high):
        # swap smaller elements with pointer and move forward
        if arr[i] <= pivot:
            arr[i], arr[pivotIndex] = arr[pivotIndex], arr[i]
            pivotIndex += 1
    # put pivot in the right position
    arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]
    return pivotIndex


def quickSortIterative(arr, low, high):
    stack = [(low, high)]
    while stack:
        low, high = stack.pop()
        pivotIndex = partition(arr, low, high)
        if pivotIndex - 1 > low:
            stack.append((low, pivotIndex - 1))
        if pivotIndex + 1 < high:
            stack.append((pivotIndex + 1, high))
    return arr


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
