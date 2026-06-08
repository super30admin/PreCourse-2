# Time Complexity  : O(n log n) average, O(n^2) worst case (when array is already sorted)
# Space Complexity : O(log n) for recursion call stack
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None

# Python program for implementation of Quicksort Sort

# Pick the last element as pivot.
# Use two pointers i and j to move all elements smaller than pivot to the left.
# Place pivot in its correct position.
# Recursively sort left and right halves.

def partition(arr, low, high):
    pivot = arr[high]                   # pick last element as pivot
    i = low - 1                         # i = wall, starts before the array (small zone is empty)

    for j in range(low, high):                  # j scans every element except pivot
        if arr[j] <= pivot:                     # current element is smaller than pivot
            i += 1                              # push wall forward
            arr[i], arr[j] = arr[j], arr[i]     # swap small element into left zone

    arr[i+1], arr[high] = arr[high], arr[i+1]   # place pivot right after small zone
    return i + 1                                # return pivot's correct index so quickSort can split


def quickSort(arr, low, high):
    if low < high:                                  # more than 1 element → keep sorting
        pivot_index = partition(arr, low, high)     # place pivot, get its index
        quickSort(arr, low, pivot_index - 1)        # sort left side of pivot
        quickSort(arr, pivot_index + 1, high)       # sort right side of pivot


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
