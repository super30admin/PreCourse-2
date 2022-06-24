# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
from tempfile import tempdir


def partition(arr,low,high):
    pivot = arr[high]
    ptr = low
    for i in range(low,high):
        if(arr[i]<pivot):
            temp = arr[i]
            arr[i] = arr[ptr]
            arr[ptr] = temp
            ptr+=1
    arr[ptr], arr[high] = arr[high], arr[ptr]
    return ptr
            
  
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if(len(arr)==1):
        return arr
    if(low<high):
        pt = partition(arr, low, high)
        quickSort(arr, low, pt-1)
        quickSort(arr, pt+1, high)
    return arr

    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
