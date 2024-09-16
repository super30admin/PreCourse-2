# Function to perform partitioning
def partition(arr, low, high):
    pivot = arr[low]  
    i = low  
    j = high  

    while i < j:

        while arr[i] <= pivot and i < high:
            i += 1
        
        while arr[j] > pivot and j > low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    
    arr[low], arr[j] = arr[j], arr[low]
    
    return j  

# Function to do QuickSort recursively
def quickSort(arr, low, high):
    if low < high:
        
        pindex = partition(arr, low, high)

        
        quickSort(arr, low, pindex - 1)

        
        quickSort(arr, pindex + 1, high)

# Driver code to test the QuickSort
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)

# Output the sorted array
print("Sorted array is:")
print(arr)
