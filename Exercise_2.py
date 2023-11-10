# Time Complexity : O(nlog(n))
# Space Complexity : O(n), n recrusive calls
# Did this code successfully run on Leetcode : Yes,
# Any problem you faced while coding this : no

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 

# Function to do Quick sort 
def quickSort(arr,low,high): 
   if len(arr) == 1: 
       return arr; 
   if low < high:
       j = partition(arr, low, high)
       quickSort(arr, low, j-1)
       quickSort(arr, j+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
