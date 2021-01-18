# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1

# Recursive Approach:
# 1. Get middle index of the array
# 2. x == arr[mid] return mid
# 3. x > arr[mid] recurse over right half
# 4. x < arr[mid] recurse over left half

# Iterative approach
# 1. Repeat while low <= high
#   1.1 Get middle index of the array
#   1.2 x > arr[mid] low = mid + 1
#   1.3 x < arr[mid] high = mid - 1
#   1.4 else return mid

def binarySearch(arr, l, r, x): 
  
  #write your code here
  # Iterative approach
  while l <= r:
    mid = ( l + r ) // 2
    if x > arr[mid]:
      l = mid + 1
    elif x < arr[mid]:
      r = mid - 1
    else:
      return mid
  return -1
  
  # Recursive approach
  # if (r >= l):
  #   mid = (l + r) // 2
  #   if (x > arr[mid]):
  #     return binarySearch(arr, mid + 1, r, x)
  #   if (x < arr[mid]):
  #     return binarySearch(arr, l, mid - 1, x)
  #   if (x == arr[mid]):
  #     return mid
  # else:
  #   return -1 
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 3
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
