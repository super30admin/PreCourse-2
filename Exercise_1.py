# Time Complexity : O(logn)
# Space Complexity :O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Used the white board to design the algo and psuedo code which helped to solve it on first try


# Your code here along with comments explaining your approach
# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  #write your code here
  while l <= r:
      '''Setting the mid point'''
      m = (l+r)//2
      '''
        If the mid point is the target return the mid point
        If the mid point is on the left of the target move the left to the right of midpoint
        If the mid point is on the right of the target move the right to the left of the midpoint
      '''
      if arr[m] == x:
          return m
      elif arr[m] < x:
          l = m+1
      else:
          r = m-1

  '''Return -1 since the element hasn't been found'''
  return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result) 
else: 
    print("Element is not present in array")
