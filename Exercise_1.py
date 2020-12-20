# Python code to implement iterative Binary  
# Search. 
# Time Complexity : O(n) = log n
# Space Complexity : O(n) = n
# Did this code successfully run on Leetcode : I was not aware that I had to do this. Will do this soon.
# Any problem you faced while coding this : No problems


# Your code here along with comments explaining your approach

import math
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  while l <= r:
    mid = int(math.floor((l+r)/2))
    if arr[mid] == x:
      return mid
    else:
      if arr[mid] > x:
        r = mid-1
      else:
        l = mid + 1
  return -1


  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 3
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) #O(n) = log n 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
