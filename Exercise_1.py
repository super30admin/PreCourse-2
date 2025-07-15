# Python code to implement iterative Binary  
# Search.
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None

# It returns location of x in given array arr  
# if present, else returns -1

def binarySearch(arr, l, r, x):
    while l<=r:
        mid = (l+r)//2 #Finds the middle index
        # Check if x is present at mid
        if arr[mid]==x:
            return mid+1
        # If x is greater, ignore left half
        elif arr[mid]>x:
            r = mid - 1
        # If x is smaller, ignore right half
        else:
            l = mid+1
    return -1  #Element is not present in array
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
