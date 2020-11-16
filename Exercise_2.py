# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
  

  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if len(arr) == 1:
        return arr
        
    if low < high:
        mid = partition(arr, low, high)
        quickSort(arr, low, mid-1)
        quickSort(arr, mid+1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
