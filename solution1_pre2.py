# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : O log(n)
#Space Complexity : O(1)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : no

def binarySearch(arr, l, r, x): 

  mid = 0
  #Check base case
  while l <= r:
    mid = (l+r) // 2  #find mid
    if arr[mid] == x: #compare mid value & target value
        return mid
    elif arr[mid]  < x: #check mid less than target value
        l = mid + 1
    else:
        r = mid - 1. # if mid is greater than target r is changed.
  return -1
        
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")