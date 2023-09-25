# Python program for implementation of Quicksort

# Time Complexity: O(n^2)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : Did not know this approach, learnt while completing the assignment

# swap function
def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


# This function is same in both iterative and recursive
def partition(arr, low, high):
    pivot_idx = low
    pivot = arr[pivot_idx]

    while low < high:
        while arr[low] <= pivot and low < len(arr) - 1:
            low += 1
        while arr[high] > pivot:
            high -= 1

        if low < high:
            swap(low, high, arr)

    swap(pivot_idx, high, arr)
    return high


def quickSortIterative(arr, low, high):
    # Initialize a stack with the boundaries of the initial subarray
    stack = [(low, high)]

    while stack:
        low, high = stack.pop()  # Pop the top subarray from the stack

        partition_idx = partition(arr, low, high)  # Partition the subarray

        if partition_idx - 1 > low:
            # Push left subarray boundaries
            stack.append((low, partition_idx - 1))

        if partition_idx + 1 < high:
            # Push right subarray boundaries
            stack.append((partition_idx + 1, high))


# Driver code to test the implementation
arr = [11, 9, 29, 7, 2, 15, 28]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" "),
