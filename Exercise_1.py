# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : O(log n) 
#   - In each recursive call, the search space is reduced by half.
# Space Complexity : O(log n) 
#   - Due to recursion stack. Each recursive call adds a frame to the stack.
# Did this code successfully run on Leetcode : NA
# Any problem you faced while coding this : NA

def binarySearch(arr, l, r, x): 
  
  
    # low and high represent the current portion of the array we are looking at
    low = l
    high = r

    # if the current search space is valid
    if low <= high:
        # find the middle element
        mid = low + (high - low) // 2

        # if the middle element is what we are looking for, return its index
        if arr[mid] == x:
            return mid

        # if x is bigger than the middle, search in the right half
        if arr[mid] < x:
            return binarySearch(arr, mid + 1, high, x)

        # if x is smaller than the middle, search in the left half
        if arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
    else:
        # if we reach here, the element is not in the array
        return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 2
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print( "Element is not present in array")
