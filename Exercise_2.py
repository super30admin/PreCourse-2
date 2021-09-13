# Time complexity: O(n^2) worst case and O(n log n) average case
# Space complexity: O(n)

# Python program for implementation of Quicksort Sort
from collections import deque
# give you explanation for the approach


def partition(arr, low, high):
    # mark the low element as pivot for partitioning
    pivot = arr[low]
    start, end = low, high
    while start < end:
        # move the start pointer forward as long as the elements are less than/equal to the pivot element
        while start <= end and arr[start] <= pivot:
            start += 1
        # move the end pointer backward as long as the elements are greater than pivot
        while start <= end and arr[end] > pivot:
            end -= 1
        # swap start and end elements
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    # swap the end and the pivot(marked by arr[low])
    arr[end], arr[low] = arr[low], arr[end]
    return end


# Function to do Quick sort
def quickSort(arr, low, high):
    # retrieve partition index and call quick sort twice with each partition
    if low < high:
        partitionIndex = partition(arr, low, high)
        quickSort(arr, low, partitionIndex-1)
        quickSort(arr, partitionIndex+1, high)
    # return arr


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
