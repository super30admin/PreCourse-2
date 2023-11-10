# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
      import math
      #write your code here
      # check base case
      if r>=1:
            mid = int((math.ceil(l + r) / 2))
            if arr[mid] == x:
                  return mid
            
            if x <  arr[mid]:
                  return binarySearch(arr, 0, mid - 1, r, x)
            if x > arr[mid]:
                  return binarySearch(arr, mid+1, len(arr)-1, x) 
                  
      else:
         return None     


      mid = math.ceil((l + r) / 2)

  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index {}".format(result)) 
else: 
    print("Element is not present in array")
