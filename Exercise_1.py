# Time complexity is O(log n)
# Space complexity is O(1)

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    while l <= r:
        middle = (l + r) // 2

        # Check if x is present at mid
        if arr[middle] == x:
            return middle

        # If x is smaller, ignore right half
        elif arr[middle] > x:
            r = middle - 1

        # If x is greater, ignore left half
        else:
            l = middle + 1

    # If we reach here, the element was not present
    return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 4
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is available at index ",result)
else: 
    print ("Element is not present in array")
