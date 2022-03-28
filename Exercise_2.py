# Time Complexity: O(n*n)
# Space Comlexity: O(n)

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    i = low-1
    pivot = arr[high]                           # Initial pivot is the last element.
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]     # Swapping elements.
            
    arr[i+1], arr[high] = arr[high], arr[i+1]       # Swapping the pivot element.
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if len(arr) == 1:
        return arr
    if low < high:
        pivot = partition(arr, low, high)       # Finding the pivot element
        quickSort(arr, low, pivot-1)            # For the left subarray.
        quickSort(arr, pivot+1, high)           # For the right subarray.
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
