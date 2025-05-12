# Python code to implement iterative Binary Search. 
# Author : Akaash Trivedi
# Time Complexity :
# Space Complexity :
# Did this code successfully run on Leetcode : Leetcode #704
# Any problem you faced while coding this : No
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  while l<=r:
    mid = l + r // 2
    # Can be founf without adding l and r
    # mid = l + (r - l) // 2

    if arr[mid] == x:
        return mid  
    
    if arr[mid] < x:
      l = l+1
    elif arr[mid] > x:
      r = r-1
    else:
      return mid

  return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index ",result) 
else: 
    print("Element is not present in array")
