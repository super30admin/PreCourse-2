#Time Complexity : O(n^2)
#Space Complexity : O(n)
#Did this code successfully run on Leetcode : No, I did not run it on leetcode
#Any problem you faced while coding this : 


#Your code here along with comments explaining your approach

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #This function chooses the pivot as last element
    # here we take the last element and modify the list such that all the elements less than
    # pivot occurs to left of it and all the elements larger than pivot occurs right of it
    i = (low-1)
    p = arr[high]
    
    for j in range(low, high):
        if arr[j] <= p:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return(i+1)

# Function to do Quick sort 
def quickSort(arr,low,high):
    # if the list has only one element we return it
    if len(arr) == 1:
        return arr
    #else when low pointer is less than high pointer, we partition the list at pivot and 
    #recursively call the quick sort on both the sub parts
    if low < high:
        p = partition(arr,low,high)
        
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)
    
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 

 
