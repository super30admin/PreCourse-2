# Time Complexity: O(n log n) on average
# Space Complexity: O(log n) due to recursion stack

def partition(arr, low, high):
    """
    This function takes the last element as pivot, places the pivot element at its correct position in sorted array, 
    and places all smaller (smaller than pivot) to the left of pivot and all greater elements to the right of pivot.
    
    :param arr: List[int], the array to be sorted
    :param low: int, the starting index of the partition
    :param high: int, the ending index of the partition
    :return: int, the index of the pivot element in the sorted array
    """
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than the pivot

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap the pivot element with the element at i+1
    return i + 1

def quickSort(arr, low, high):
    """
    The main function that implements QuickSort.
    
    :param arr: List[int], the array to be sorted
    :param low: int, the starting index of the array to be sorted
    :param high: int, the ending index of the array to be sorted
    """
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)

        # Recursively sort elements before partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print(arr[i], end=" ")
