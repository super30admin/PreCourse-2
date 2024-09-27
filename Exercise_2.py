# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    pivot=arr[low]
    lo=low+1
    hi=high

    while lo<=hi:
        while arr[hi]>pivot:
            hi=hi-1
        while lo<=hi and arr[lo]<=pivot:
            lo=lo+1
        if lo<=hi:
            arr[lo],arr[hi]=arr[hi],arr[lo]
            lo=lo+1
            hi=hi-1
    arr[low],arr[hi]=arr[hi],arr[low]
    return hi
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if(low<high):
        q=partition(arr,low,high)
        quickSort(arr,low,q-1)
        quickSort(arr,q+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
