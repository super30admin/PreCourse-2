# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l <= r:
        # Calculate the mid index to avoid overflow
        mid = l + (r - l) // 2  
        
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        
        # If x is smaller, ignore the right half
        elif arr[mid] > x:
            r = mid - 1
        
        # If x is larger, ignore the left half
        else:
            l = mid + 1
    
  # Element is not present in array
  return -1 
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 30
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
