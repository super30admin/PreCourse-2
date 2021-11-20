# Python code to implement iterative Binary  
# Search. 

# It returns location of x in given array arr  
# if present, else returns -1

# / Time Complexity : o(log(n))
# // Space Complexity : o(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this :

import math


def binarySearch(arr, l, r, x):
    # write your code here
    left = l
    right = r

    middle = int(math.ceil(left + right) / 2)

    while right - left >= 0:
        if arr[middle] == x:
            return middle
        elif arr[middle] < x:
            left = middle+1
            middle = int(math.ceil(left + right) / 2)
        else:
            right = middle-1
            middle = int(math.ceil(left + right) / 2)

    else:
        return -1


# Test array 
arr = [2, 3, 4, 10, 40]
x = 2

# Function call 
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print "Element is present at index % d" % result
else:
    print "Element is not present in array"
