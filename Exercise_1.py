# Time Complexity: O(log n)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode: yes
# Any problem you faced while coding this: no

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  #write your code here

  while l <= r:
    mid = l + (r - l) // 2

    # Check if x is at mid
    if arr[mid] == x:
        return mid

    # If x is greater, ignore left half
    elif arr[mid] < x:
        l = mid + 1

    # If x is smaller, ignore right half
    else:
        r = mid - 1

  # Element wasn't found
  return -1
     
  
    
  
# Test array 
arr = [ 2, 3, 4 , 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}, human-readable index {result + 1}") 
else: 
    print("Element is not present in array")
