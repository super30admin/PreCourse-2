# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

# Your code here along with comments explaining your approach

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):  # we are dividing the array into two halves, left and right with a mid value.
  
  #write your code here
    while r >= l: 
      mid = (r+l) // 2

      if arr[mid] < x: # if search element is more than the mid element, then we will look on right side
        l = mid+1

      elif arr[mid] > x: #if search element is more than the mid element, then we will look on left side
        r = mid-1
      
      else: # or else the search element is the middle element only
        return mid
    
    return -1 # if not found return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result)
else: 
    print ("Element is not present in array")
