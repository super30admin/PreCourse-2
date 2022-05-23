# Author: Vineet Khanna
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    # Picking first element as pivot, can pick any.
    pivot = arr[high]
    #starting pointer from 1st element
    p = low

    for i in range(low,high):
        if arr[i]<= pivot:
            arr[i], arr[p] = arr[p], arr[i]
            p+=1
    arr[p], arr[high] = arr[high], arr[p]
    return p
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if len(arr) == 1:
        return arr
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr,low,p-1) 
        quickSort(arr, p+1, high)
    return arr 
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1)
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
