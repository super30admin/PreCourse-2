# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):

    index = low - 1  # low - Starting Index , partition Index
    pivot = arr[high] # last element as pivot , high - End Index
  
    for i in range(low,high):

        if arr[i] <= pivot: # check if current element is smaller than or equal to pivot
            index = index + 1
            arr[index], arr[i] = arr[i], arr[index]
    #swap the last element, return partition index
    arr[index+1], arr[high] = arr[high], arr[index+1] 
    return (index+1) 

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if len(arr) == 1: 
        return arr 
    if low < high: 
        partitionIndex = partition(arr, low, high) 
  
        quickSort(arr, low, partitionIndex-1) 
        quickSort(arr, partitionIndex+1, high) 
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
