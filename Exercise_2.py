
# Time complexity: O(n log n)
# Space complexity: O(log n)

# The approach is to use the partition function to place the pivot in its correct position,
# and then recursively sort the sub-arrays on either side of the pivot.
def partition(arr, low, high):
    # Select the rightmost element as pivot
    pivot = arr[high]
    # Index of smaller element (initially -1)
    i = -1

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # Partition the array
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
