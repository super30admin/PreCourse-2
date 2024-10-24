# Function to do partition
def partition(arr, low, high):
    # We choose the last element as pivot
    pivot = arr[high]

    # Index of the smaller element, initially set to the start
    i = low - 1

    # Traverse through all elements except the pivot
    for j in range(low, high):
        # If the current element is smaller than the pivot
        if arr[j] < pivot:
            i = i + 1  # Increment the index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Swap the pivot element with the element at i + 1 to place it in the right position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1  # Return the partitioning index (pivot's final position)


# Function to perform QuickSort
def quickSort(arr, low, high):
    if low < high:
        # Get the partitioning index
        pi = partition(arr, low, high)

        # Recursively sort the elements before and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Driver code to test the above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
