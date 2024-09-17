# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time complexity O(log n)
# Space complexity O(1)


def binarySearch(arr, l, r, x): 
  
  while l <= r:
    mid = (l + r)//2
    if x == arr[mid]:
      return mid
    elif x < arr[mid]:
      r = mid - 1
    elif x > arr[mid]:
      l = mid + 1

  return -1
  
    
  
# Test array 
arr = [ 0,1,2,3,4,5] 
x = 5
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}")
else: 
    print("Element is not present in array")
