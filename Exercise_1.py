# // Time Complexity :  O(log₂ n)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : NO

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

def binarySearch(arr, l, r, x): 
  while(l<=r):
     # TO find index of mid element
     mid = (l+r) // 2
     # Comparing target wrt middle element
     if arr[mid] == x:
        return mid
     # Search operation on left part of sorted half
     elif arr[mid] > x:
        r = mid - 1
      # Search operation on right part of sorted half
     else:
        l = mid + 1
      # If no target is found 
  return -1
     
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print("Element is not present in array")
