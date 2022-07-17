# Time Complexity : O(n log n) for average case
# Space Complexity : O(log n)
# Did this code successfully run on Leetcode : 
# Any problem you faced while coding this : no

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
#-->selects the last element as pivot and compares each element with the pivot and places the smaller elements than the pivot to left 
# of pivot and larger elements to the right of pivot 

def partition(arr,low,high):
  
    pivot=arr[high]
    i=low-1
    #loop through all the elements to compare with the pivot
    for j in range(low, high):
        if arr[j]<pivot:
            i+=1
            (arr[i], arr[j])= arr[j], arr[i]    
    arr[i+1], arr[high]=arr[high], arr[i+1]    
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if low<high:
        pi=partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
