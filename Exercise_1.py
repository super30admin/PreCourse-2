# Python code to implement iterative Binary  
# Search. 
# O(log n) where n is the input size
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  
  while l<=r:
    #(r-l/2) instead of r to reduce the bounds
    midElementIndex = l+((r-l)//2)
    if x>arr[midElementIndex]:
      l = midElementIndex+1
    elif x<arr[midElementIndex]:
      r = midElementIndex-1
    else:
      return midElementIndex
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