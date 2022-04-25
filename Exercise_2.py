# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    p_ind = low
    p = arr[p_ind]
    # l += 1
    while low < high:
        while low < len(arr) and arr[low] <= p:
            low += 1
        while arr[high] > p:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    arr[p_ind], arr[high] = arr[high], arr[p_ind]
    return high
  
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        partition_index = partition(arr, low, high)
        quickSort(arr, low, partition_index - 1)
        quickSort(arr, partition_index + 1, high)
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
