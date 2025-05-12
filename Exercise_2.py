# Time Complexity 
#    Avg - o(nlogn) and worst case is o(n^2)
# Space Complexity
#    Recursive call stack - o(logn)


def partition(arr, low, high):
    """
    Partitions the array around a pivot element.

    Args:
        arr (list): The input array.
        low (int): The starting index of the array.
        high (int): The ending index of the array.

    Returns:
        int: The index of the pivot element after partitioning.
    """
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot element
    return i + 1


def quickSort(arr, low, high):
    """
    Recursively sorts the array using Quicksort.

    Args:
        arr (list): The input array.
        low (int): The starting index of the array.
        high (int): The ending index of the array.
    """
    if low < high:
        pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
