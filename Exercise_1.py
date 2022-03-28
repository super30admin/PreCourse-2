# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : O(nlogn)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

def binarySearch(arr, l, r, x): 
  while(l<r):
    #index average rounded off 
    mid = l+r//2

    #if element found, return the index
    if arr[mid] == x:
      return mid

    #if x less than element at mid, search prior arr portion else the other
    if x < arr[mid]:
      r = mid-1
    else:
      l = mid
  
  #if while condition fails and control reaches here, element not found and return -1
  return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index %d" % result) 
else: 
    print ("Element is not present in array")
