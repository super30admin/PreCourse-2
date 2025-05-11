# Python program for implementation of Quicksort Sort 

# Time Complexity : O(n log n), worst case O(n^2)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : N/A, no Leetcode link
# Any problem you faced while coding this : No
  
# give you explanation for the approach

# Start with rightmost element as pivot
# Move elements so that elements smaller than pivot are on left and largere than pivot are on right
# Return pivot idx and apply the operation recursively to left and right sub-arrays based on pivot 

def partition(arr,low,high):
  
  
    #write your code here
    pivotElem = arr[high]
    
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivotElem:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
