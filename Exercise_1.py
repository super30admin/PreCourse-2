"""
Leetcode: https://leetcode.com/problems/binary-search/ (similar) - not submitted
TC - O(NlogN), SC - O(1)
Challenge - assigning l, r and midpoints could get sensitive and program could go in loop.
"""


# Python code to implement iterative Binary
# Search. 

# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1

    return -1


# Test array 
arr = [2, 3, 4, 10, 40]
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
