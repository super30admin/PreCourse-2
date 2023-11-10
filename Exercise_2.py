# Time Complexity : 0(n*log(n))
# Space Complexity :O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :No

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

def partition(arr,low,high): 
    p = arr[high] # Selecting the Last Element as Pivot
    lower = 0 # Pointer pointing to lower part/Values less than the pivot 
    for j in range(high):
        if(arr[j]<p): # Elements less than pivot is shifted the lower part of the array
            (arr[lower],arr[j])=(arr[j],arr[lower])
            lower+=1 # Extending lower part of array 
    (arr[lower],arr[high])=(arr[high],arr[lower]) # Swapping pivot so that left of pivot has small elements than itself and right has elements greater than the pivot.
    
    return lower # Returned the pivot  


# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if(low<high):
        p=partition(arr,low,high) 
        quickSort(arr,low,p-1) #Sorting Left of Pivot and Right of pivot seperately 
        quickSort(arr,p+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 
