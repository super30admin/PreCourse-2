# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  #write your code here
  while l <= r:
      mid = l + (r - l) // 2  # Calculate the middle index

      if arr[mid] == x:  # If the element is found at the middle index
          return mid
      elif arr[mid] < x:  # If the element is greater, search the right half
          l = mid + 1
      else:  # If the element is smaller, search the left half
          r = mid - 1
  return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 45
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result )
else: 
    print("Element is not present in array")
