# Python code to implement iterative Binary  
# Search. 
# Time Complexity : O(logn)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :no
# Your code here along with comments explaining your approach
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  while l <= r: # that means we have an error and exit the loop
    mid = (l + r) // 2 #to find the middle index
    if(arr[mid]==x): #this means elem is found at mid index
      return mid
    else:
        if arr[mid]>x: #if our mid elem > input elem we shift to left to mid-1
          r = mid-1
        else: #if our mid elem < input elem we shift to mid-1 to right
          l =mid+1
  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index",result) 
else: 
    print("Element is not present in array")
