# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

#Time complexity: O(log(N))
def binarySearch(arr, l, r, x):
  if l <= r:
    mid = (l + r) // 2
    # Target found, return index
    if arr[mid] == x:
      return mid
    # Target lesser than value at mid, search in left half
    elif arr[mid] > x:
      return binarySearch(arr, l, mid - 1, x)
    # Target greater than value at mid, search in right half
    else:
      return binarySearch(arr, mid + 1, r, x)

  # Target not found
  return -1
  
    
  
# Test array 
arr = [2, 3, 4, 10, 40] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
  print(f"Element is present at index {result}")
else: 
  print("Element is not present in array")


# Test array 2
arr = [2, 3, 4, 10, 40] 
x = 50
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
  print(f"Element is present at index {result}")
else: 
  print("Element is not present in array")


# Test array 3
arr = [2, 3, 4, 10, 40] 
x = 0
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
  print(f"Element is present at index {result}")
else: 
  print("Element is not present in array")


# Test array 4
arr = [2, 3, 4, 10, 40, 50] 
x = 3
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
  print(f"Element is present at index {result}")
else: 
  print("Element is not present in array")