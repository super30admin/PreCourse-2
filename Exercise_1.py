# Time Complexity : O(logN)  as we traverse only half of the given list in each iteration
# Space Complexity : O(1) as no extra space is used just variables like mid
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No



# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  
  while l <= r:
    mid = (l + (r - 1)) // 2
    
    if arr[mid] == x:
      return arr[mid]
    elif arr[mid] > x:
      r = mid - 1
    else:
      l = mid + 1
    
  return -1

    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
