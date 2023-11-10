# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : O(log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

def binarySearch(arr, l, r, x): 
  while l<=r:           #checking if entire array has been traversed or not
    mid=l+(r-l)//2      #find the middle element
    if arr[mid]==x:     #if element is found at mid return mid
      return mid
    elif x>arr[mid]:    #if element is higher than mid value, change left to mid+1 i.e perform binary search on right subarray
      l=mid+1
    else:               #if element is lower than mid value, change right to mid-1 i.e perform binary search on left subarray
      r=mid-1
  
  return -1

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index: ",result)
else: 
    print("Element is not present in array")
