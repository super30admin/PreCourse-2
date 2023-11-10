# Time Complexity : O(log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
from xml.dom import minidom


def binarySearch(arr, l, r, x): 
  
  #write your code here
  i = l
  j = r
  while i <= j:

    # Find middle index
    mid = (i + j) // 2

    # If x is found at mid, then return mid
    if arr[mid] == x:
      return mid 

    # If x is smaller than the element at mid, then ignore the right half of arr
    elif arr[mid] > x:
      j = mid - 1
      
    # If x is greater than the element at mid, then ignore the left half of arr
    else:
      i = mid + 1
  
  # If x is not found in arr, return -1
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
