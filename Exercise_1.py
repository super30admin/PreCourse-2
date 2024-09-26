# Time Complexity :O(Log(n))
# Space Complexity :O(1)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : forgot the = in line 16 once :'D


# Your code here along with comments explaining your approach
# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  start = l
  end = r
  while start <= end:
    mid = (start+end)//2
    if arr[mid] == x:
      return mid
    elif arr[mid] > x:
      end = mid-1
    else:
      start = mid+1
  return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 2
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result )
else: 
    print( "Element is not present in array" )
