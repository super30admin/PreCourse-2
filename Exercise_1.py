# Time Complexity : O(log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : None

def binarySearch(arr, l, r, x):
    #searching while there are elements between l and r
    while l <= r: 
      # pick the midpoint
      mid = (l + r) // 2
      # if x is larger, ignore left half
      if arr[mid] > x:
        r = mid - 1
      # if x is smaller, ignore right half
      elif arr[mid] < x:
        l = mid + 1
      # if we found x at mid, return its index
      else:
         return mid
    # x was not found in the array
    return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result)
else: 
    print ("Element is not present in array")
