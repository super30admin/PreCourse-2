# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[low]
    while low < high:
        # Find first element greater than or equal to pivot
        while low < high and arr[low] < pivot:
            low += 1

        # Find first element smaller than pivot
        while low < high and arr[high] > pivot:
            high -= 1

        # We want to find a position to insert our pivot at.
        # The idea of partition is to ensure all elements before pivot are smaller than it,
        # elements after pivot are greater than it.
        # If 'low' crosses 'high', we already have achieved our "partition" as explained above,
        # hence no need to swap, otherwise swap
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]

    # Swap the pivot and element at 'high' to place pivot element to it's correct position
    pivot, arr[high] = arr[high], pivot
    return high
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot)
        quickSort(arr, pivot + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]) 
 
