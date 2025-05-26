# Python code to implement iterative Binary Search. 
# It returns location of x in given array arr  
# if present, else returns -1 

# At each step, divide the search space in half.
# The maximum number of steps required to find an element in an array of size N is log(N).
# Time complexity: O(log⁡N)
# Space complexity is: O(1): uses a few integer variables, no extra memory is used

def binarySearch(arr, l, r, x): 
    while l <= r: 
        mid = l + (r - l) // 2
  
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1 
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1 
  
    # Element is not present in array 
    return -1
  
    
  
# # Test array 
# arr = [ 2, 3, 4, 10, 40 ] 
# x = 10
  
# # Function call 
# result = binarySearch(arr, 0, len(arr)-1, x) 
  
# if result != -1: 
#     print "Element is present at index % d" % result 
# else: 
#     print "Element is not present in array"
