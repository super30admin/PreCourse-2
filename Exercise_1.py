# Time Complexity : O[log(n)]
# Space Complexity : O(1)

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  if arr[l] > x or arr[r] < x:
    return -1
  while l <= r:
    m = int((l + r)/2)
    if arr[m] == x:
      return m
    elif arr[m] < x:
      l = m + 1
    elif arr[m] > x:
      r = m - 1
  return -1

  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 1
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index " + str(result))
else: 
    print("Element is not present in array")
