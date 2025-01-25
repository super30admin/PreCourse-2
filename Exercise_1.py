# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  # write your code here
  # tc O(log n), sc O(1).
  left, right = 0, len(nums) - 1

  while left <= right:
      mid = left + ((right - left) // 2)
      if nums[mid] == target:
          return mid
      if nums[mid] > target:
          right = mid - 1
      else:
          left = mid + 1
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
