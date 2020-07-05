# Python code to implement iterative Binary  
# Search.

  
# It returns location of x in given array arr  
# if present, else returns -1

# TIME COMPLEXITY: O(lg n) - at each call the search space is divided so at the max the while loop will run O(lg n) times.
# SPACE COMPLEXITY: O(1) - no extra space is used.
def binarySearch(arr, l, r, x):

    #write your code here
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        elif arr[mid] < x:
            l = mid + 1

    return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 8
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
