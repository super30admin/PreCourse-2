# Time Complexity : O(log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Approach:
# 1. Initialize two pointers, l (left) and r (right), to mark the search boundaries.
# 2. While l <= r:
#    - Compute the middle index m = (l + r) // 2.
#    - If nums[m] is greater than the target, move r to m - 1 (search left half).
#    - If nums[m] is less than the target, move l to m + 1 (search right half).
#    - If nums[m] equals the target, return m (element found).
# 3. If the loop ends without returning, the element is not present → return -1.

# Python code to implement iterative Binary
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  l, r = 0, len(arr)-1
  while l <= r:
      m = (l + r) // 2
      if arr[m] > x:
          r = m - 1
      elif arr[m] < x:
          l = m + 1
      else:
          return m

  return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result)
else: 
    print ("Element is not present in array")
