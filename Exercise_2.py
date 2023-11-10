# Python program for implementation of Quicksort Sort

"""
Time Complexity:
- Average case: O(n log n)
- Worst case: O(n^2) 

Space Complexity:
- Average case: O(log n)
- Worst case: O(n)
"""

def partition(arr, low, high):
    pivot = arr[high]
    partition_index = low

    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i], arr[partition_index] = arr[partition_index], arr[i]
            partition_index += 1

    arr[partition_index], arr[high] = arr[high], arr[partition_index]

    return partition_index


def quickSort(arr, low, high):

    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Driver code to test the above functions
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)

quickSort(arr, 0, n - 1)

print("Sorted array is:")
for i in range(n):
    print(arr[i], end=" ")
