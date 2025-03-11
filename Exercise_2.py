# Python program for implementation of Quicksort Sort
# Time Complexity: O(n log n) on average, O(n^2) in the worst case
# Space Complexity: O(log n) due to recursion stack

def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than pivot
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot to correct position
    return i + 1

# Function to do QuickSort
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partitioning index

        quickSort(arr, low, pi - 1)  # Sort left partition
        quickSort(arr, pi + 1, high)  # Sort right partition

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:", arr)