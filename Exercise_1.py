# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# We check if the target is the mid element each time, if lesser than mid element - we focus search on left side of the middle element otherwise right side of the middle element 
def binarySearch(arr, l, r, x): 
  while l <= r: 
    # find the mid element using this dynamic formula incase search start index is different from 0
    mid = l + (r-l) // 2
    if x == arr[mid]:
      return mid 
    elif x > arr[mid]:
      l = mid + 1
    else: 
      r = mid - 1           
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
