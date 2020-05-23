"""
// Time Complexity :  O(log n), where n is the number of elements
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
"""

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l<=r:
    mid = l + (r-l)//2 #getting the middle index
            
    if arr[mid]==x:
      return mid
    elif x > arr[mid]: #if x is greater than the mid value, then we update l to mid+1 to consider the second half of the array
      l = mid+1
    elif x < arr[mid]: #if x is smaller than the mid value, then we update r to mid-1 to consider the second half of the array
      r = mid-1
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
