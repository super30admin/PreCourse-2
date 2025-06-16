# Time Complexity : O(n log n) on average, O(n^2) in worst case 
# Space Complexity : O(log n)  
# Python program for implementation of Quicksort Sort  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]  # choosing the last element as pivot
    i = low - 1  # index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # swap

    # Place pivot in the correct location
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if low < high:
        # pi is partitioning index
        partition_indix = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quickSort(arr, low, partition_indix - 1)
        quickSort(arr, partition_indix + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
