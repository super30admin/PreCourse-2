# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1

# Time Complexity: O(logn)
# Space Complexity: O(1)

import math

def binarySearch(arr, l, r, x): 
  
  #write your code here

    while r < l:
        return -1

    while r >= l:
        mid_index = math.floor((l + r) / 2)
        if x < arr[mid_index]:
            r = mid_index - 1
        elif x > arr[mid_index]:
            l = mid_index + 1
        elif x == arr[mid_index]:
            return mid_index
        else:
            return -1
    return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result)
else: 
    print ("Element is not present in array")
