#Time Complexity : O(logn)
#Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  #write your code here
  l,r = 0,len(arr)-1
  while l <= r:
    mid = (l+r) // 2
    if arr[mid] == x:
      return mid
#Move the left pointer to mid + 1 to search in the right half of the array. 
    elif arr[mid]<x:
      l = mid+1
#Move the right pointer to mid + 1 to search in the left half of the array.
    elif arr[mid]>x:
       r = mid-1
  return -1 
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index", result)
else: 
    print("Element is not present in array")
