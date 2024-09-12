# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):

    #write your code here
    pivot_index = low
    pivot = arr[pivot_index]
    N = len(arr)

    while low < high:

        # Find first element from left strictly greater than pivot
        while low < N and arr[low] <= pivot:
            low += 1
      
        # First first element from right smaller or equal to pivot
        while arr[high] > pivot:
            high -= 1

        # if low and high has not crossed
        if low < high:
            # Swap
            arr[low], arr[high] = arr[high], arr[low]
    
    # Swap high with pivot_index and return high
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return high

# Function to do Quick sort 
def quickSort(arr,low,high):
    #write your code here
    if low < high:
        pivot_index = partition(arr, low, high) 
        quickSort(arr, low, pivot_index-1)
        quickSort(arr, pivot_index+1, high)
    
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
