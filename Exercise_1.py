"""
# Time Complexity : O(log N)

# Space Complexity : O(1)

# Did this code successfully run on Leetcode : N/A, performed local testing

# Any problem you faced while coding this : No

"""

# Your code here along with comments explaining your approach


# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  while l <= r:
     mid = (l + r)//2 #check the middle element

     if arr[mid] == x: #target has been found
        return mid
     elif arr[mid] > x: #target is smaller than current element, move left
        r = mid - 1
     else:
        l = mid + 1 #target is larger than current element, move right

  return -1 #target was not present in array
  
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 50
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
