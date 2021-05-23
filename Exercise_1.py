# Python code to implement iterative Binary  
# Search. 
# Time complexity : O(logn)
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  # Loop till left less than right 
  while l<r:
    # mid point for each iteration to limit search space
    mid = (l+r)// 2
    if arr[mid] == x:
      # if mid element is equal to x
      return mid
    elif arr[mid] < x:
      # if x is greater than mid element, limit search space to right of mid
      l = mid +1
    else:
      # if x is smaller than mid element, limit search space to left of mid
      r = mid -1
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
