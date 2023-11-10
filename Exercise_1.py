# Time Complexity : O(logN)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
   #first running while loop until left index is less than or equal to right
   while l <= r:
     #finding a midpoint by taking left and right index value and dividing by 2
     mid = (l + r) // 2
     #if target x is equal to mid point then directly returning mid
     if arr[mid] == x:
       return mid
     #if mid is less than x then x is on the right side so assigning left as mid+1
     elif arr[mid] < x:
        l = mid + 1
     #else x is on left side and assigning right as mid-1
     else:
        r = mid - 1
 
   return -1
 
    
 
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
