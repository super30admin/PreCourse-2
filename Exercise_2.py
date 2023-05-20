# Python program for implementation of Quicksort Sort 
#Time Complexity : O(n log n) in avg case  andd O(n^2) in worst case.
#Space Complexity: O(n log n)
# give you explanation for the approach
def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # Increment index of the smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot with the element at the correct position
    return i + 1  # Return the partitioning index


def quickSort(arr, low, high):
    if low < high:
        # Partition the array into two parts
        partition_index = partition(arr, low, high)

        # Recursive calls to sort the sub-arrays
        quickSort(arr, low, partition_index - 1)
        quickSort(arr, partition_index + 1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
