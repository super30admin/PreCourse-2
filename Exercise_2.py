# Python program for implementation of Quicksort Sort 
# Time Complexity: O(n log n) on average
# Space Complexity: O(log n) due to recursion stack
# Quicksort is a divide-and-conquer algorithm. It picks an element as pivot and partitions the array around the picked pivot.

def partition(arr, low, high):
    # Choose the last element as pivot
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    arr[i+1], arr[high] = arr[high], arr[i+1]  # Place pivot in correct position
    return i + 1

# Function to do Quick sort 
def quickSort(arr, low, high): 
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
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
    print("%d" % arr[i], end=" ")
print()
  
 
