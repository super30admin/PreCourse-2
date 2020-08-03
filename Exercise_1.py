# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 


def binarySearch(arr, left, right, x): 
  #write your code here

  while left <= right:
    mid = (left+right)//2

    if x == arr[mid]:
      return mid
    
    if x > arr[mid]:
      left = mid + 1
    
    elif x<arr[mid]:
      right = mid - 1
  return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 20
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result) 
else: 
    print("Element is not present in array")
