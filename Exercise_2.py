# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr, low, high):
    pivot = arr[high]  # Choosing the pivot element (last element)
    i = low - 1  # Index of smaller element
    
    #write your code here
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i = i + 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap arr[i] and arr[j]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap the pivot element with the element at (i + 1)
    return i + 1  # Return the position of pivot in the sorted array

  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)
        
        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" ")

 
