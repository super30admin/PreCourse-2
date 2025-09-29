# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : No, but remember to increment/decrement mid index

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def recursiveBinarySearch(arr, l, r, x): 
  midIndex = int((l+r)/2)
  if arr[midIndex] == x:
    return midIndex
  if arr[midIndex] > x:
    return binarySearch(arr, l, midIndex-1, x)
  else:
    return binarySearch(arr, midIndex+1, r, x)
  
def binarySearch(arr, l, r, x): 
  while l <= r:
    midIndex = int((l+r)/2)
    if arr[midIndex] == x:
      return midIndex
    if arr[midIndex] > x:
      r = midIndex-1
    else:
      l = midIndex+1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 4
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index %d" % result)
else: 
    print("Element is not present in array")
