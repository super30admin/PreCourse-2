def partition(arr, low, high):
    # Choose a pivot (in this case, the last element)
    pivot = arr[high]
    
    # Index of the smaller element
    i = low - 1
    
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            # Swap arr[i+1] and arr[j]
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap arr[i+1] and arr[high] to place pivot in its correct position
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort elements before and after the pivot
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
 
  
 
