# Time Complexity: O(log n), where n is the number of elements in the array.
# Space Complexity: O(1), constant space as it uses only a few variables for indexes and no extra data structures.

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  # Calculate the middle index
  while l<=r:
    mid = l+(r-l)//2
    # If the middle element is the target, return its index
    if arr[mid]== x:
       return mid
    # If the target is greater, ignore the left half
    elif arr[mid]< x:
       l=mid+1
    # If the target is smaller, ignore the right half
    else:
       r=mid-1
  return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
