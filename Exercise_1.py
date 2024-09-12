# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  if r >= l :
    bin = (l+r)//2
    if arr[bin] == x:
      return bin
    if arr[bin] > x :
      return binarySearch(arr,0,bin-1,x)
    else :
      return binarySearch(arr,bin+1,r,x)
  else :
    return -1
  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
