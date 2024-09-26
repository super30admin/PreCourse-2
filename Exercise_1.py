# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

"""
Time - O(logn)
Space - O(1)
Idea - The algorithm split the list into half after every iteration and search efficiently
"""
def binarySearch(arr, l, r, x):
  if len(arr) < 2:
    if arr[l] == x:
      return l 

  while l < r:
    midpoint = (l + r) // 2

    if arr[midpoint] > x:
      r = midpoint - 1

    elif arr[midpoint] < x:
      l = midpoint + 1

    elif arr[midpoint] == x:
      return midpoint

  if arr[l] == x:
    return l
      
  return -1
    
       
    
    
  
  
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ]
#arr = [7] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index: ", result) 
else: 
    print("Element is not present in array")
