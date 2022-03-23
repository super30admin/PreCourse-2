# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  # make sure the right and left pointers dont cross each other
  while l <= r:
    mid = (l+r) // 2
    print ("mid is", mid)
    # If x is greater than mid element, ignore left half
    if arr[mid] < x:
      print (arr[mid])
      l = mid + 1
 
    # If x is smaller than mid element, ignore right half
    elif arr[mid] > x:
      print (arr[mid])
      r = mid - 1
 
    # means x is present at mid
    else:
      return mid
 
    # If we reach here, then the element was not present
  return -1
 
 

 
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
