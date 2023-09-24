# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

#Time Complexity:  O(n log n)
#Space Complexity: O(1)

def partition(arr, low, high):
    # Choose the rightmost element as the pivot
    pivot = arr[high]
    
    # Initialize the index of the smaller element
    i = low - 1

    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i = i + 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap arr[i+1] and arr[high] (the pivot)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the index of the pivot
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        # Find the partition index
        partition_index = partition(arr, low, high)

        # Recursively sort elements before and after the partition
        quickSort(arr, low, partition_index - 1)
        quickSort(arr, partition_index + 1, high)

# Driver code to test the quicksort implementation
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)

print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])

  
 
