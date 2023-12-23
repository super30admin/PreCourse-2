# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    # find the mid point
    mid = (l+r)//2

    while r >= l:
        if arr[mid] == x: # if element is present at mid
          return mid
        elif arr[mid] > x: # if element is present at left side array 
          r = mid - 1
        else: # if element is present at right side array 
          l = mid+1

        mid = (l+r)//2

    return -1

# Test array 
arr = [2, 3, 4, 10, 40] 
x = 10
l = 0
r = len(arr) - 1
  
# Function call 
result = binarySearch(arr, l, r, x) 
  
if result != -1: 
    print("Element is present at index", result)
    
else: 
    print("Element is not present in array")