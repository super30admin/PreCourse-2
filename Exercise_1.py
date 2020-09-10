# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

#recursive method
def binarySearch(arr, l, r, x):
  if l<=r:
    mid = (l+r)//2
    if arr[mid]==x:
      return mid
    elif arr[mid]>x:
      return binarySearch(arr,l,mid-1,x)
    else:
      return binarySearch(arr,mid+1,r,x)
  else:
    return -1
    
  
 #write your code here

"""iterative
def binarySearch(arr,l,r,x):
  l = 0
  r = len(arr)-1
  while(l<=r):
    mid = (l+r)//2
    if arr[mid]>x:
      r = mid-1
    elif arr[mid]<x:
      l = mid+1
    else:
      return mid
    
  return -1 """
 
  
  
    
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
