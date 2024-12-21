# T: O(log n), S: O(1)
# Python code to implement iterative Binary  
# Search. 
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  #write your code here
  # Using two pointer technique
  # Find mid 
  # Check if it's > or < target
  # Update the mid respectively
  while l <= r:
     m = (l + r) // 2
     if x > arr[m]:
        l = m + 1
     elif x < arr[m]:
        r = m - 1
     else:
        return m 
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
