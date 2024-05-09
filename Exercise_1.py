# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : O(logn) because we divide the array by half to search it
# Space Complexity : O(1) Constant Space
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
def binarySearch(arr, l, r, x): 
  
  #write your code here
  # Left is 0 and right is the last index
  # Check if target greater than the greatest element in the array. Binary search assumes array is sorted
  if arr[r] < x:
      return -1
  # Check if the element is not the first or last one
  if arr[l] == x:
      return l
  elif arr[r] == x:
      return r
  while l <= r:
      # Split array into two and search each half separately. Repeat till target is found
        mid = l + (r - l) // 2
        if arr[mid] == x:
            # Element is in the middle
            return mid
        elif arr[mid] < x:
            # Search the right half is the middle value is less than the target.
            l = mid + 1
        else:
            # Search the left half is the middle value is more than the target
            r = mid - 1
  # Element is not present in array
  return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 130
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result)
else: 
    print ("Element is not present in array")
