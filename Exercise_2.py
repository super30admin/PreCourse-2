# Python program for implementation of Quicksort Sort 
# Time Complexity: O(n log n) average case, O(n^2) worst case
# Space Complexity: O(log n) average case, O(n) worst case (due to recursive calls)

# Function to partition the array
def partition(arr, low, high):
    pivot = arr[high]  # Pivot element
    i = low - 1  # Index of smaller element
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to perform Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Driver code to test above functions
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" ")
