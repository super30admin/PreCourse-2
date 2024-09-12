# Python code to implement iterative Binary search
# It returns location of x in given array arr  
# if present, else returns -1 
# Time Complexity --> O(log(N)) (partitioning array results in log N complexity)
# Space Complexity --> O(1) (only left right pointers used )

def binarySearch(arr, l, r, x): 

  while l <= r:
    middle_idx = (l + r) // 2

    if x < arr[middle_idx]:
      # element falls in the left side of middle index in the array
      r = middle_idx - 1

    elif x > arr[middle_idx]:
      # element is in the left side of array to middle index
      l = middle_idx + 1

    else:
      return middle_idx
  
  return -1
 
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x  = 10
# x = 45
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result )
else: 
    print("Element is not present in array")
