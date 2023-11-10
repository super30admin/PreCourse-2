# Time Complexity : O(log n) as we half the array in each iteration
# Space Complexity : O(1) auxiliary space complexity or constant space as no extra space is needed. Overall Space complexity is O(n) for the array
# Did this code successfully run on Leetcode : Code ran successfully.
# Any problem you faced while coding this : No problems


# Your code here along with comments explaining your approach

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l<=r: # While lower bound is less than or equal to higher bound we can continue search. Otherwise the element is not found
    mid = (l+r)//2 # Mid element is defined/updated each iteration with changing l and/or r value
    if arr[mid] > x:
      r = mid - 1 # If mid element is greated than target, then element can not be in right half, so we reduce the r value
    elif arr[mid] < x:
      l = mid + 1 # If mid element is less than target, then element can not be in left half, so we increase the l value
    else:
      return mid # Return mid as element is found if arr[mid] == x
  return -1

  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index " + str(result))
else: 
    print("Element is not present in array")
