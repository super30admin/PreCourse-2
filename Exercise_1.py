"""
// Time Complexity : O(logn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None
// Your code here along with comments explaining your approach
Algorithm explanation
1) Iterate while low is less than or equal to right
2) compute mid:= (l + r) / 2
3) If arr[mid] = ele, then return mid
    Else if arr[mid] < ele, update l := mid + 1
    else update r = mid - 1
"""


# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  #write your code here
  while l <= r:
    mid = (l + r) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        l = mid + 1
    else:
        r = mid - 1
  return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 20

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1: 
    print("Element is present at index {}".format(result))
else: 
    print("Element is not present in array")
