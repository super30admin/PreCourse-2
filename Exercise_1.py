# Time Complexity : O(1)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  # using two pointers to keep track for start and end
  # check middle, if middle is not x, ckeck if mid is less than 
  # or grater than x
  l = 0
  r = len(arr) - 1
  while l <= r:
    mid = (l+r)//2
    if mid > x:
      mid = r - 1
    elif mid < x:
      mid = l
    else:
      return mid
  return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
