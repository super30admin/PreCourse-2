"""
Time Complexity : O(nlog(n)) when pivot is accuretly(always middle element) picked and O(n^2) when array is sorted 
Space Complexity : O(n) - recursive stack space 
"""
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    piv = arr[high]
    i = low - 1 
    
    for j in range(low, high):
        if arr[j] < piv:
            i += 1 
            arr[i], arr[j] = arr[j], arr[i]
    arr[high], arr[i+1] = arr[i+1], arr[high]
    return i + 1

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low >= high:
        return 
    
    pivot = partition(arr, low, high)
    
    quickSort(arr,low, pivot - 1)
    quickSort(arr,pivot + 1, high)
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i], end = " "), 
  
 
