# Time Complexity : 0(log(n))
# Space Complexity :O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :No

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  while(l<=r):          # Repeat while right pointer is always to the right of left pointer else we completed our search
    mid=(l+r)//2        # Computing mid of desired array
    if(arr[mid]==x):    # if mid matches with x return mid as index
      return(mid)
    elif(arr[mid]<x):   # Else if mid element is less than X, we search the remaining right half
      l=mid+1
    else:
      r=mid-1          # Else search the left half
  return(-1)           # Return if no element is found
      
  
    
  
# Test array 
arr = [2, 3, 4, 10, 40] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
