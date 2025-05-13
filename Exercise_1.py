# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1
"""
Time Complexity: O(log(n))

Space Complexity: O(1)
"""

def binarySearch(arr, l, r, x):
      if r<l:
          raise ValueError("Improper Index passed")
      if len(arr)==0:
            raise ValueError("Array empty")
      while l<=r:
        mid = (l+r)//2 
        element = arr[mid]
        if element==x:
              return mid 
        if element < x:
              l = mid+1
        else:
              r = mid-1 
      
      return -1

def safeBinarySearch(arr, l, r, x):
    if arr!= sorted(arr):
      raise ValueError("Array must be sorted for Binary search")
    return binarySearch(arr, l, r, x)



      
# Test array 
arr = [2, 3, 4, 10, 40]
x = 10

# Function call 
result = safeBinarySearch(arr, 0, len(arr)-1, x)
  
if result != -1: 
    print("Element is present at index %d" % result) 
else: 
    print("Element is not present in array")

arr = [1, 2, 4, 6, 8, 10]
x = 20

# Function call 
result = safeBinarySearch(arr, 0, len(arr)-1, x)
  
if result != -1: 
    print("Element is present at index %d" % result) 
else: 
    print("Element is not present in array")
    
arr = [2, 4, 1, 6, 8, 10]
x = 6

result = safeBinarySearch(arr, 0, len(arr)-1, x)
  
if result != -1: 
    print("Element is present at index %d" % result) 
else: 
    print("Element is not present in array")
  

