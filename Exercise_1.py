## Time Complexity : O(N)
## Space Complexity : O(N)
## Did this code successfully run on Leetcode : Yes
## Any problem you faced while coding this : Paranthesis missing error while executing the solution.
##
##
## Your code here along with comments explaining your approach

# Python code to implement iterative Binary
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    if l <= r:
        mid = (l + r) // 2
        mid_value = arr[mid]

        if mid_value == x:
            return mid  # Target found, return the index
        elif mid_value < x:
            return binarySearch(arr, mid + 1, r, x)  # to look in the right half
        else:
            return binarySearch(arr, l, mid - 1, x)  # to look in the left half

    return -1  # Target not found
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result)
else: 
    print ("Element is not present in array")
