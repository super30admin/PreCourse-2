# Time complexity : O(n log(n)). At every step, we split the array into two halves 
  # and check if the element is present in that half
# Space complexity : O(1). Only left and right pointers are used additionally

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  # At every time step, we need to make a decision whether to check the right
  # sub array or left sub array. Check the element at the center of the array.

  mid = (l+r)//2
  if arr[mid] == x:
    return mid
  elif arr[mid] > x:
     # Search the left sub array
     r = mid - 1
     return binarySearch(arr, l, r, x)
  else:
     # Search in the right sub array
     l = mid + 1
     return binarySearch(arr, l, r, x)
  return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
print(result)
  
if result != -1: 
    print(f"Element is present at index {result}")
else: 
    print("Element is not present in array")
