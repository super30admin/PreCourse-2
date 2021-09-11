# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1
# // Time Complexity : O(Log n)
# // Space Complexity :O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this :No
# explanation : This code starts with calculating the middle element and after that
# we check if middle element equals the target.
# if target is less than middle we move the right pointer to mid - 1 else left to mid+1 
# we do this until we find the target element
def binarySearch(arr, l, r, x): 
  #write your code here
  while l<=r:
    mid = l + (r-l) //2
    print("mid=",mid)
    print("left=",l)
    print("right=",r)
    if arr[mid] == x:
      return mid
    elif arr[mid]>x:
      r = mid-1
    else:
      l = mid+1
  return -1

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 40
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
