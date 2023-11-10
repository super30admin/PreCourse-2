# Time Complexity : Best - Ω(nlog(n)), Average - θ(nlog(n)), Worst - O(n^2)
# Space Complexity : Although it is an in-place sort, but if we consider recursion stack, Worst space complexity - O(n), Average and Best space complexity - O(log(n))
# Did this code successfully run on Leetcode : Couldn't find the problem in LeetCode
# Any problem you faced while coding this : No

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):

    #write your code here
    # Let the last element in the subarary be the pivotelement
    pivotelement = arr[high]
    pivotindex = low
    # Move all elements in the subarray which are less than or equal to the pivotelement to the starting of the array
    for i in range(low, high):
        if arr[i] <= pivotelement:
            arr[pivotindex], arr[i] = arr[i], arr[pivotindex]
            pivotindex += 1
    # Move the pivotelement to the pivotindex and return the pivotindex, pivotelement is now at it's correct place
    arr[pivotindex], arr[high] = arr[high], arr[pivotindex]
    # At this point all the elements to left of pivotindex are <= pivotelement and those at right are > pivotelement
    # Return the pivotindex
    return pivotindex
 

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low >= high:
        return
    # The element at pivotindex is already at its correct place
    pivotindex = partition(arr, low, high)
    # Sort the part of arr to the left of the pivotindex
    quickSort(arr, low, pivotindex-1)
    # Sort the part of arr to the right of the pivotindex
    quickSort(arr, pivotindex+1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
