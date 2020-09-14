# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  # Time Complexity : O(log n)
  # Space Complexity : O(1)
  #write your code here
  mid_point = (l+r)//2

  if(l==r and arr[l]!=x):
    return -1
  if(arr[mid_point]==x):
    return mid_point
  elif(arr[mid_point]<x):
    return binarySearch(arr, mid_point+1, r, x)
  else:
    return binarySearch(arr, l, mid_point, x)    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
