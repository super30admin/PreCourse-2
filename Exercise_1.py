# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  """
  Time complexity: o(log n)
  Space Complexity: o(1) -- Since I have implemented the iterative version 
  """
  
  l = 0
  r = len(arr) - 1
  while l <= r:
      mid = (l + r) // 2
    # if x is greater than mid, ignore left half
      if arr[mid] < x:
        l = mid + 1
      
      # if x is smaller ignore the right half
      elif arr[mid] > x:
        r = mid - 1
      # eliment is middle point
      else:
        return mid
  # if x is not present in array 
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
