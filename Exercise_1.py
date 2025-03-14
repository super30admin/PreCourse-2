# Python code to implement iterative Binary  
# Search. 
# Time Complexity : O(log N)
# Space Complexity :O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):

    while l <= r:

        mid = l + (r - l) // 2 # to find the mid point of the array

        # if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater we can ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller we can ignore right half
        else:
            r = mid - 1

    # when element is not present we come here
    return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index",result)
else: 
    print("Element is not present in array")
