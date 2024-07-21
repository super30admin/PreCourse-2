
# // Time Complexity : O(log n)
# // Space Complexity : O(1) maintaining only constants
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach
""" Implemented basic binary search by computing mid as (l+r) //2, compared arr[mid] with target element x,
if mid element is same returned mid else checking if mid element is greater than target then assigning r to mid -1
else assigning l to mid+1 to search the right side of the array. Returning -1 if no if element is not found"""

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while (l <= r):
     mid = (l + r) // 2
     if arr[mid] ==  x:
        return mid
     elif arr[mid] > x:
        r = mid - 1
     else:
        l = mid + 1
  return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index %d" % result)
else: 
    print ("Element is not present in array")
