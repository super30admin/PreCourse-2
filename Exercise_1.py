# Time Complexity:
# - Best Case: O(1) - When the target element is at the middle position of the array
# - Average Case: O(log n) - Each iteration divides the search space in half
# - Worst Case: O(log n) - When the target element is not in the array or at either extreme
#
# Space Complexity:
# - O(1) - Constant space complexity as we only use a fixed number of variables
#   regardless of input size. No recursion stack or additional data structures needed.

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  while l <= r :
    mid = l + (r - l)//2

    # Check if x is present at mid
    if arr[mid] == x:
      return mid
    
    # If x is greater, ignore left half
    elif arr[mid] < x:
      l = mid + 1 

    # If x  is smallerr, ignire left half
    else:
      r = mid - 1

  # If we reach here, then the element was not present 
  return - 1 
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print (f"Element is present at index = {result} ")
else: 
    print ("Element is not present in array")
