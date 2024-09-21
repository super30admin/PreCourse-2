# Partition function for QuickSort
def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Index of smaller element

    # Traverse through all elements and rearrange elements around the pivot
    for j in range(low, high):
        if arr[j] < pivot:  # If current element is smaller than the pivot
            i += 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Place the pivot at the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the index of the pivot

# QuickSort function
def quickSort(arr, low, high):
    if low < high:
        # Find the pivot element such that elements smaller than pivot are on the left
        # and elements greater than pivot are on the right
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1)  # Recursively sort left subarray
        quickSort(arr, pi + 1, high)  # Recursively sort right subarray

# Driver code to test the above implementation
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
