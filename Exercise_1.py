# Python Code to implement iterative Binary 
# Search

# It returns location of x in given array arr  
# if present, else returns -1
# Time Complexity : For element search O(logn)
# Space Complexity : O(1) 
#  Did this code successfully run on Leetcode : Yes
#  Any problem you faced while coding this : No problem faced


# Your code here along with comments explaining your approach
# Binary Seach with iterative method
# Continuously divide the array in half and reduce the search space
def binarySearch(arr, l, r, x):
  # Checking the condition that left is less thn right
  while l <= r:
    # Finding the midpoint
    mid = l + (r - l)//2
    # Return the target element if directly in the midpoint
    if arr[mid] == x:
      return mid
    elif x > mid:
      l = mid + 1
    else:
      r = mid - 1
  return -1
arr = [ 2, 3, 4, 10, 40] 
x = 45 
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
if result != -1: 
    print("Element is present at index % d" % result) 
else: 
    print("Element is not present in array")