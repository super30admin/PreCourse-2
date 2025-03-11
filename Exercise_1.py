# Python code to implement iterative Binary Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1
# 
# Time Complexity: O(logn)
# Space Complexity: O(1)
 
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is smaller, ignore right half
        elif x < arr[mid]:
            r = mid - 1
        # If x is greater, ignore left half
        else:
            l = mid + 1
    return -1  # Element is not present in array
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index",result) 
else: 
    print ("Element is not present in array")
