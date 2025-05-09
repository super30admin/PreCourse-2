# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l <= r:
    mid = l + (r-l)//2
    if arr[mid] == x: #If x is present at mid
      return mid
    elif arr[mid] < x: #If x is greater check only right half
      l = mid + 1
    else: #If x is smaller check only left half
      r = mid - 1
  return -1 #x is not there returing -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
