# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

"""
    Binary Search takes O(log n) time becuase 
    after every iteration half of the given input is ignored.
    where n is total numbers the input array
"""
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l <= r:
    mid = (l + r) // 2

    if x == arr[mid]:
      return mid
    elif x < arr[mid]:
      r = mid - 1
    else:
      l = mid + 1
    
  return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}") 
else: 
    print("Element is not present in array")
