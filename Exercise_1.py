# Time Complexity : O(logn)
# Space Complexity : O(1) as l, r, mid take constant space
# Did this code successfully run on Leetcode : LC 704 yes
# Any problem you faced while coding this : NA

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    
    if x == arr[l]:
      return l
  
    while l <= r: 
      mid = (l + r)// 2
      #write your code here
      if (x == arr[mid]):
        return mid
      elif (x < arr[mid]):
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
    print ("Element is present at index" + result)
else: 
    print ("Element is not present in array")
