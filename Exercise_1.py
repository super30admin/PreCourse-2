# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 


# Time Complexity : O(1)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No problem 


# Your code here along with comments explaining your approach : Divide and Conquer Approach

def binarySearch(arr, l, r, x): 
  
  mid = 0

  while l <= r:
    mid = (r + l) // 2

    if arr[mid] < x:
      l = mid + 1
 
    elif arr[mid] > x:
      r = mid - 1
 
    else:
      return mid
 
  return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40, 199, 200, 201, 1000 ] 
x = 201
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index", str(result) )
else: 
    print ("Element is not present in array")
