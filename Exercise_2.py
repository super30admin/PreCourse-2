# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# Time Complexity : O(nlogn)
# Space Complexity : O(1)
def partition(arr,low,high):
    #write your code here
    pivot = low
    value = arr[pivot]
    print(arr)
    while low < high:
       
        while low < len(arr) and arr[low] <= value:
            low +=1
            
        while arr[high] > value:
            high -=1
            
        if low < high:
            arr[low],arr[high] = arr[high], arr[low]
            
    arr[high], arr[pivot] = arr[pivot], arr[high]
    
    return high
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low < high:
        par = partition(arr,low,high)
        
        quickSort(arr,low,par-1)
        quickSort(arr,par+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
