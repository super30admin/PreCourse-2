"""
Time complexity of Binery Search algorithm is O(log(n)),
Space complexity is O(1)
"""

# Python code to implement iterative Binary
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    while r >= l:
        m = (r+l)//2
        if arr[m] < x:
            l = m + 1
        elif arr[m]>x:
            r = m - 1
        else:
            return m
    else:
        return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 2
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
