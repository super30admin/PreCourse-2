# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
"""
TC => O(n logn) where n = len(arr)
SC => O(1)
 """
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l <= r:
    mid = l + (r - l)//2
    if arr[mid] == x:
      return mid
    elif x < arr[mid]:
      r = mid - 1
    else:
      l = mid + 1
  return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 5
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index " , result )
else: 
    print("Element is not present in array")
