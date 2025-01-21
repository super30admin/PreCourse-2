# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    if arr is None or len(arr) == 0: return -1

    while l <= r:
        mid = l + (r - l)//2

        if arr[mid] == x: return mid

        # search on the right side of mid
        if arr[mid] < x:
            l = mid + 1
        else:
            # search on the left side of mid
            r = mid - 1
    return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
