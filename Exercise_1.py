'''
// Time Complexity : O(log n) assuming that the list is sorted
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None 

we find the mid, compare the arr[mid] with the target. 
if arr[mid]==target we return mid else we shift our pointers L and R 
based on the value comparison between arr[mid] and target 
'''
# Python code to implement iterative Binary  
# Search. 
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  while l<=r:
    mid=(l+r)//2
    if arr[mid]==x:
      return mid
    elif arr[mid]>x:
      r=mid-1
    else:
      l=mid+1
  return -1
  #write your code here
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result) 
else: 
    print("Element is not present in array")
