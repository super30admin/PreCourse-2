# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1
"""
Time complexity - O(log n)
Space complexity O(1)
"""
def binarySearch(arr, l, r, x):
    """
    Approach --
    Since the list is sorted, find mid-value of the list
    if the key value is less than mid, search on the left of mid
    if the key value is greater than mid, search on the right of mid
    """
    while l <= r:
        # find mid
        mid = (l + r)//2

        # check if target value is equal to
        # mid-value of arr
        if arr[mid] == x:
            return mid

        # check if mid-value is greater than target val
        # if yes, search on the left of mid
        if arr[mid] > x:
            #search on the left of mid
            r = mid - 1
        else:
            # search on the right of mid
            l = mid + 1

    return -1

    # Time O(n) complexity - Linear search
    # for i in range(len(arr)):
    #     if arr[i] == x:
    #         return i
    # return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
