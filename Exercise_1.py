# Time Complexity : O(log n)
# Space Complexity : O(1)

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  if len(arr)==0:
    return -1
  while l<=r:
    mid = (l+r)//2
    if arr[mid] == x:
      return mid
    elif x < arr[mid]:
      r = mid-1
    else:
      l = mid+1
  return -1
    
# Test array 
arr = [ 2, 3, 4, 10, 40, 60 ] 
x = 4
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index ",result) 
else: 
    print ("Element is not present in array")
